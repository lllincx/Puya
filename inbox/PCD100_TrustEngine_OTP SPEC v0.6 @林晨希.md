## Version

| Version | Date         | Author | Note                         |
| ------- | ------------ | ------ | ---------------------------- |
| 0.1     | 2026 年 8 月 5 日 | 林晨希 | Copy from PT105              |
| 0.2     | 2026 年 8 月 5 日 | 林晨希 | Change addr to PCD100 config |
| 0.3     | 2026 年 8 月 6 日 | 林晨希       |  配合 PCD100 设计，初步修改 |
| 0.4 | 2026 年 8 月 6 日 | 林晨希 | 变更 page num 为 page type      |
| 0.5 | 2026 年 8 月 7 日 | 林晨希 | 根据 PCD100 中 flash 编程流程变更 |
| 0.6 | 2026 年 8 月 7 日 | 林晨希 | add erase stage in page type a program |

## Diagram

```
             (flash) WR
                 |
                 v
          +---------------+                      +---------------+
          |               | Power on / OBL Reset |               |
          |     Flash     |--------------------->|  TrustEngine  |
          |               |                      |               |
          +---------------+                      +---------------+
                 |                                      |
                 | Flash RD                             | TrustEngine RD
                 v                                      v
```

## Flash WR

### Page type A

#### 擦除

> 当某个页被 WRP 保护，它是不会被擦除的，此时 `WRPERR` 位被置位。

1) 检查 `FLASH_SR` 或 `FLASH_SECSR` 寄存器 `BSY` 位，确认没有正在进行的 Flash 操作
2) 向 `FLASH_KEYR` 或 `FLASH_SECKEYR` 寄存器依次写 KEY1 和 KEY2，解除 `FLASH_CR` 或 `FLASH_SECCR` 寄存器的保护
3) 置位 `FLASH_CR` 或 `FLASH_SECCR` 寄存器的 `PER` 位和 `EOPIE`（如果需要产生 `EOP` 中断）位
4) 向该页写任意数据（必须 64bit 数据）
5) 等待 `BSY` 位被清零
6) 检查 `EOP` 标志位被置位
7) 清零 `EOP` 标志
8) 清零 `FLASH_CR` 或 `FLASH_SECCR` 寄存器的 `PER` 位

#### 编程

> 上电复位后，根据加载的 `LCS [2:0]` 的值，决定 `model id, model key` 是否可编程

1) 检查 `FLASH_SECSR` 寄存器的 `BSY` 位，确认没有正在进行的 Flash 操作
2) 如果没有正在进行的 Flash 擦除或者编程操作，则软件读出该页的 128 个 word
3) 向 `FLASH_SECKEYR` 寄存器依次写 `KEY1` 和 `KEY2`，解除 `FLASH_SECCR` 寄存器的保护
4) 置位 `FLASH_SECCR` 寄存器的 `UPG` 位和 `EOPIE`（如果需要产生 `EOP` 中断）位
5) 向 OTP 区地址进行第 1 到第 63 个双 word 的编程操作（只接受 64bit 的编程）
6) 置位 `FLASH_SECCR` 寄存器的 `UPGSTRT`
7) 写第 64 个双 word
8) 等待 `BSY` 位被清零
9) 等待 `EOP` 拉高，软件清零
10) 如果不再有编程操作，则软件清除 `UPG` 位

> 当步骤 7 成功执行，则编程操作自动启动，同时 `BSY` 位被硬件置位。

#### 生效

数据不会立即生效，只有上电复位/OBL 复位后，OTP 数据被传入 TrustEngine IP 内部。

### Page type B

1) 检查 `BSY` 位，确认没有正在进行的 Flash 操作
2) 向 OTP 写入寄存器 `(FLASH_OTPWRO<x>)` 写入需要的值（若非字对齐写入，则忽略该操作）
	- OTP 写入寄存器 `(FLASH_OTPWRO<x>)` 与 OTP 内容对应关系见 sheet 6
	- 一次只能进行一个 OTP 修改
	- 写入内容只增，如果违反则静默失效

3) 置位 `OTPROSTRT` 位
4) 根据 sheet 6 中 OTP 写入寄存器 `(FLASH_OTPWRO<x>)` 与“写入地址”列的对应关系，向“写入地址”写任意 64bit 数据，触发正式的写操作。

|      | 异常情况        | 异常后果                   |
| ---- | --------------- | -------------------------- |
| 1    | 非 64bit 对齐写入 | 产生 HardFault              |
| 2    | 写入非指定地址  | 出现错误，不能正常执行操作 |

5. 等待 `BSY` 位被清零
6. 等待 `EOP` 拉高，软件清零

## Flash RD

1. 读取 sheet 1 中 addr 列对应地址
2. Page type B 需要进行 4bit->1bit 转换（4bit 全为 0 才是 0，如果有 1bit 为 1 则是 1）

> `userdatard0[7:0]=10101010`
>
> 读 sheet 1 中对应地址的结果为 `11110000111100001111000011110000`

## TrustEngine RD

1. 读取 sheet 2 中 addr 列对应地址
2. TrustEngine 读权限遵循 sheet 4

## Notes

flash 的读写权限遵从 sheet 5
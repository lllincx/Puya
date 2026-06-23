## 一

> HIO 有的地方看是 1，有的地方看是高阻

```
--HIO
++$root.top.u_dut_top.u_dut.HIO
```

## 二

> apb 总线上操作与 asic 不一致

asic 上会出现中断，为了保险需要做清除操作。
fpga 不出现中断是正常现象

## 三

> 其他位没有问题，ADDR[24]为 X 态。

上层连线问题。

## 四

> fmc 端口与 HIO 信号不一致

nor_flash_enable=0
需要配置 case cfg

```
cfg.sim_cmd<<"+NORFLASH_EN"
```

## 五

> 向 nor flash 写入数据时，nor flash 端口上信号正常。但读出时，读出内容为 X 态。

发现读出 flash 内部数据时，model 端口获取 model 内部 reg 数据的 assign 语句错误。
nor_flash_cs[1:0]需要个 HIO 端口连接，但目前只有一个，因此对没有使用的 nor1，没有配置 nor_flash_cs[1]，导致其为高阻状态。由于数据，地址线 nor0，nor1 共用，因此会影响 nor0 的信号输出。
将 nor_flash_cs[1]赋值恒定为 1。

## 六

> log 打印信息正常，但 flag 判断为错误。

error_flag 始终为非 0 恒定值
移除 error_flag 的 volatile 关键字

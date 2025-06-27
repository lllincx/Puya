# 参考文件

## SMC spec

Table 2-24 NAND flash address input example awaddr fields

| awaddr bits | Value       | Description            |
| ----------- | ----------- | ---------------------- |
| [31:24]     | Chip select | -                      |
| [23:21]     | 3'b011      | Three address cycles   |
| [20]        | 1           | End command required   |
| [19]        | 0           | Command phase transfer |
| [18:11]     | CMD2        | -                      |
| [10:3]      | CMD1        | -                      |
| [2:0]       | 3'b000      | Address alignment      |

![image.png|800](https://raw.githubusercontent.com/lllincx/IMG/master/20250626154200343.png)

> CMD1 为起始命令，CMD2 为结束命令。两者一般有其中一个

## NAND SPEC

### 9.2 编程操作

#### 9.2.1 页编程（80h-10h）

W29N01HV 的页编程命令将按页地址从低到高的顺序在块内连续编程。禁止乱序编程页。若需对页进行分区操作，W29N01HV 支持最多 4 次部分页编程，之后需执行擦除操作。注意：不支持在未擦除的情况下对单个比特位进行重复编程。

#### 9.2.2 串行数据输入（80h）

页编程操作首先向命令寄存器写入串行数据输入命令（80h），随后输入 4 个地址周期并加载数据。每个#WE 周期都会将串行数据载入数据寄存器。串行数据输入完成后，向命令寄存器写入编程命令（10h）。此时内部写状态控制器自动执行编程及校验算法。

编程启动后，可通过监测 RY/#BY 输出或状态寄存器第 6 位（该位状态与 RY/#BY 信号同步）来判断操作是否完成。在内部阵列编程期间（tPROG 周期内），RY/#BY 将保持低电平。页编程过程中仅支持两条命令：读状态（70h）和复位（FFh）。

当器件状态转为就绪时，状态寄存器第 0 位（1/00）显示编程操作结果：成功（位 0=0）或失败（位 0=1）（参见图 9-6）。命令寄存器将保持读状态模式直至接收到下一条指令。

![image.png|800](https://raw.githubusercontent.com/lllincx/IMG/master/20250626154634194.png)

# 代码

```C
//smc_nand_case
//WRITE PHASE
// Command phase: address
write wdata = 0x<<16 | 0x3a8<<0;

smc_nand_cmd(nand_addr_match, 0x5, 0x0, 0x0, 0x80, 0x0, wdata);
smc_nand_cmd(nand_addr_match, 0x5, 0x0, 0x0, 0x80, 0x0, 0);

//fsmc_func.c
//NAND command
void smc_nand_cmd(int chip_addr, int add_num, int end_req, int end_cmd, int start_cmd, int addr_align, int nand_addr){
unsigned int sys_addr;
sys_addr = chip_addr << 24 | add_num << 21| end_req << 20 | 0x0 << 19 | end_cmd << 11 | start_cmd << 3 | addr align << 0；
write_mem(sys_addr, nand_addr);
DSB();
ISB();


```



# 波形

![Snipaste_2025-06-26_15-42-47-modified.png|800](https://raw.githubusercontent.com/lllincx/IMG/master/Snipaste_2025-06-26_15-42-47-modified.png)
配置的 add_num=5[该配置与 nand 大小相关]
因此，`smc_nand_cmd(nand_addr_match, 0x5, 0x0, 0x0, 0x80, 0x0, wdata)`命令需要分两次传输地址，第一次传输低四位，第二次传输高位

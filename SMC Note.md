### **SRAM 时序参数详解**

#### **周转时间 (Turn Around Time)**

- **定义**：数据总线从**读取模式切换到写入模式**（或反之）时，控制器必须等待的最短时间
- **作用**：确保 SRAM 停止驱动总线后，控制器才开始驱动总线，避免冲突
- **典型场景**：发生在读操作结束（`OE#`置高）和写操作开始（`WE#`置低）之间

#### **页循环时间 (Page Cycle Time)**

- **定义**：在**页模式访问**中，行地址不变时完成**一次列访问**的最短时间
- **特点**：远小于标准读/写周期时间（省去了行激活时间）
- **应用场景**：突发式顺序数据访问（如缓存行填充）

#### **WE#断言延迟 (WE# Assertion Delay)**

- **定义**：`WE#`有效（低电平）到 SRAM 开始锁存输入数据的时间
- **要求**：数据必须在延迟时间后保持稳定（满足建立/保持时间）

#### **OE#断言延迟 (OE# Assertion Delay)**

- **定义**：`OE#`有效（低电平）到输出数据有效的延迟
- **核心参数**：地址访问时间（`tAA`），决定 SRAM 读取速度

#### **写循环时间 (Write Cycle Time)**

- **定义**：完成完整写操作的最短时间
- **关键子参数**：
  - `tAS`（地址建立时间）
  - `tWP`（写使能脉宽）
  - `tDS`/`tDH`（数据建立/保持时间）

#### **读循环时间 (Read Cycle Time)**

- **定义**：完成完整读操作的最短时间
- **关键子参数**：
  - `tAA`（地址访问时间）
  - `tOH`（地址保持时间）
  - `tOEH`（输出禁止时间）

---

### **NAND 时序参数详解**

#### **WE_n De-assertion 延迟**

- **参数**：`tWH`（WE# High Time）
- **值域**：10–15 ns
- **作用**：确保数据稳定锁存至 NAND 内部缓存

#### **配置状态读时间**

- **总耗时**：<1 μs
- **关键子参数**：
  - `tWB`（命令锁存到 BUSY 有效）：≤100 ns
  - BUSY 持续时间：100–500 ns

#### **配置 ID 读时间**

- **总耗时**：200–500 ns（5 字节 ID）
- **关键子参数**：
  - `tCLS/tALS`（CLE/ALE 建立时间）：≥12 ns
  - `tREA`（RE#到数据就绪）：10–30 ns

#### **BUSY 到 RE_n 时间**

- **核心参数**：`tRB`（BUSY 无效到 RE#有效）
- **值域**：≥50 ns
- **作用**：防止总线冲突

---

### **寄存器说明**

#### **opmode 寄存器**

> 每个支持的芯片都有一个  `opmode`  寄存器的实例。该寄存器是只读的，并且在复位状态下无法读取。  
> 这些寄存器的复位值取决于具体配置。您可以通过硬件连接（tie-off）为每个存储器接口的片选 0 设置存储器位宽，以支持从该芯片启动。所有其他片选的存储器位宽复位值即为所配置的位宽。顶层硬件连接设置地址匹配和地址掩码的复位值。`burst_align`  的复位值为二进制  `001`，所有其他字段复位为  `0`。

#### **地址比较与掩码配置**

> 返回此硬件连接的值。这是用于地址位 [31:24] 的比较值，以确定被选中的芯片。  
> 返回此硬件连接的值。这是用于地址位 [31:24] 的掩码，以确定必须选中的芯片。逻辑 1 表示该位用于比较。
>
> 当配置 SMC 执行同步传输时，这些位控制突发边界拆分：
>
> - `b000`：突发可跨任意地址边界
> - `b001`：在存储器突发边界拆分（32 拍连续）
> - `b010`：在 64 拍边界拆分
> - `b011`：在 128 拍边界拆分
> - `b100`：在 256 拍边界拆分
> - `b101-b111`：保留
>
> **注**：对 NAND 接口这些位保留。

#### **字节通道与突发控制**

> 此位影响字节通道选通输出（BLS）的置位时机：
>
> - `0`：BLS 时序等于片选时序（默认）
> - `1`：BLS 时序等于写使能时序（用于无 BLS 输入的 8 位存储器）
>
> 当置位时：
>
> - 存储器使用地址提前信号（`adv_n`）
> - 存储器使用突发地址提前信号（`baa_n`）
>
> 写操作突发长度选择：
>
> - `b000`：1 拍
> - `b001`：4 拍
> - `b010`：8 拍
> - `b011`：16 拍
> - `b100`：32 拍
> - `b101`：连续传输
> - `b110-b111`：保留
>
> **注**：对 NAND 接口所有上述位均保留。

#### **direct cmd 寄存器**

> 该只写寄存器向外部存储器传递命令，并控制用`set_cycles`和`set_opmode`寄存器的值更新芯片配置寄存器。  
> **复位或低功耗状态下不可写入**。

| 字段        | 功能说明                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------- |
| chip_select | 选择要更新的寄存器组：`b000-b011`=接口 0 片选 1-4；`b100-b111`=接口 1 片选 1-4            |
| cmd_type    | 命令类型：`b00`=UpdateRegs+AXI；`b01`=ModeReg；`b10`=UpdateRegs；`b11`=ModeReg+UpdateRegs |
| set_cre     | ModeReg 命令时映射到`cre`信号：`0`=低电平；`1`=高电平                                     |
| addr        | 根据 cmd_type 映射地址位[19:0]或匹配 wdata[15:0]                                          |

---

### **模块功能**

#### **Format Block**

> 格式转换模块接收来自 AXI 从接口和存储器管理器的访问请求。AR 和 AW 通道的请求采用轮询仲裁，管理器请求具有最高优先级。该模块将 AXI 传输映射为存储器传输，并通过命令 FIFO 传递给存储器接口。

#### **Memory Manager (2.1.4)**

> 跟踪并控制 SMC `aclk`域 FSM 状态，负责：
>
> - 更新`mclk<x>`域的寄存器值
> - 控制向存储器发出的直接命令
> - 通过 APB 接口管理低功耗模式进入/退出
> - 控制 AXI 低功耗接口（详见第 2-27 页）

#### **Memory Interface (2.1.5)**

> 支持 SRAM/NAND 两种接口类型，包含：
>
> - 命令/读数据/写数据 FIFO
> - 专用控制 FSM（SRAM 或 NAND）
> - EBI FSM（控制外部总线交互）
> - 可选 SLC ECC 模块（仅 NAND）  
>    **注**：存储器接口编号`x`=0/1，片选编号`n`=0-3。

#### **Pad Interface (2.1.6)**

> 为数据/控制信号提供寄存 I/O 接口，包含中断生成逻辑。

### 时钟与复位

#### AXI 时钟域

图片中提到 aclk 属于 AXI 时钟域，且仅在 SMC 处于低功耗模式时可停止。这确保了系统在正常运行时的稳定性。

#### 内存时钟域

内存时钟域包括除 aclk 外的所有时钟，需确保 mclk<×>信号与外部内存时钟速度同步。两个内存接口可异步运行，低功耗模式下可停止这些时钟。

#### 同步时钟

同步时钟通过移除同步寄存器减少读写延迟，但受外部内存时钟速度限制，可能影响系统性能。

---

#### 详细报告

以下是图片内容的完整翻译，涵盖了技术文档中关于时钟域的详细描述，确保所有术语和上下文准确无误。

##### 时钟域概述

图片内容首先将时钟分为三个主要时钟域：AXI 时钟域、内存时钟域和同步时钟的相关讨论。以下是逐部分的翻译：

- **AXI 时钟域**  
   aclk 属于该时钟域。仅当静态内存控制器（SMC）处于低功耗模式时，才能停止 aclk。这确保了在正常操作期间时钟的连续性。
- **内存时钟域**  
   除 aclk 外的所有时钟都属于内存时钟域。需确保 mclk<×>信号的时钟频率与外部内存时钟速度一致。mclk<×>n 是 mclk<×>的倒相版本。在实现两个内存接口的配置中，两个内存时钟域还可以彼此异步运行。当 SMC 处于低功耗模式时，可以停止内存时钟域的时钟。
  **注意**  
   <×>表示内存接口 0 或 1。有关时钟之间所需关系的详细信息，请参阅《PrimeCell 静态内存控制器（PL350 系列）集成手册》。
- **同步与异步操作**  
   可以通过固定 SMC 的 async<×>和 msync<×>引脚，使 aclk 和 mclk<×>时钟域相对于彼此同步或异步运行。当使用外部总线接口（EBI，PL220）时，SMC（PL353）和 SMC（PL354）的 mclk0 和 mclk1 时钟域必须以 1:1、n:1 或 1:n 的同步方式运行。
- **同步时钟的优点**  
   同步时钟的优点是通过移除时钟域之间的同步寄存器，可以减少读写延迟。然而，由于时钟之间的整数关系，受外部内存时钟速度对总线频率的限制，系统可能无法获得最大性能。

###### 技术术语解释

在翻译过程中，确保了以下术语的准确性：

- "clock domains" 翻译为 "时钟域"，符合技术文档的用语。
- "low-power mode" 翻译为 "低功耗模式"，与电子工程领域常用表达一致。
- "tie-off" 翻译为 "固定"，在电子设计中指将引脚设置为固定逻辑电平，符合上下文。

| 时钟域类型 | 主要特点                                                   | 操作限制                 |
| ---------- | ---------------------------------------------------------- | ------------------------ |
| AXI 时钟域 | 包含 aclk，仅在低功耗模式下可停止                          | 需确保正常运行时连续性   |
| 内存时钟域 | 包括 mclk<×>和 mclk<×>n，可异步运行，低功耗模式下可停止    | 需与外部内存时钟速度同步 |
| 同步时钟   | 通过移除同步寄存器减少延迟，但受总线频率和内存时钟速度限制 | 需权衡性能与延迟         |

以下是关于“独占访问”的完整中文解释：

---

### 独占访问？

**独占访问**（Exclusive Accesses）是在多主控系统（如遵循 AMBA AXI 协议规范的系统）中用于确保数据一致性的一种机制。特别是在多个主控器（如处理器或设备）访问共享内存或资源时，独占访问能够防止数据竞争，确保数据的完整性。这种机制尤其适用于实现同步原语，如锁或信号量，以协调对共享数据的访问。

#### 关键概念

1. **目的**  
   独占访问允许一个主控器对内存位置执行读-修改-写（read-modify-write）操作，而不会受到其他主控器的干扰。这确保了在操作过程中数据保持一致。

2. **两个阶段**

   - **独占读**（Exclusive Read）：主控器读取一个内存位置，并将其标记为“独占”。这表示它打算稍后修改该位置。系统开始监视该地址。
   - **独占写**（Exclusive Write）：同一个主控器尝试写回该内存位置。只有在自独占读以来没有其他主控器修改该位置时，写操作才会成功。

3. **响应类型**

   - **EXOKAY**：表示独占访问成功（读和写阶段均未受到干扰）。
   - **OKAY**：表示普通访问或独占访问失败（例如，由于干扰而导致独占写失败）。

4. **独占访问监视器**（Exclusive Access Monitors）

   - 这些硬件组件负责跟踪独占访问。每个监视器可以同时监视一个独占访问。
   - 监视器的数量是可配置的，具体取决于系统设计。

5. **失败处理**
   - 如果独占写失败（例如，另一个主控器修改了监视的地址），写操作将被中止，数据掩码（data mask）强制设置为**LOW**，以防止数据被写入。

#### 工作原理：地址监控

为了确保数据一致性，系统会将独占读时监视的地址与来自其他主控器的任何写地址进行比较。这种比较使用**位掩码**（bit mask）来确定监视的位置是否被修改。

- **位掩码生成**

  - 对于一个写事务，识别其访问的字节地址范围（例如，0x104–0x10B）。
  - 找到该范围内变化的最高位（例如，位 3）。
  - 在掩码中，将该位及以下所有位设置为**0**（不比较这些位）。
  - 将所有更高的稳定位设置为**1**（比较这些位）。
  - 例如，掩码为`b111111110000`（0xFF0）。

- **比较过程**

  - 将掩码应用于监视地址（例如，0x100）和写地址（例如，0x104）。
  - 如果掩码后的结果匹配（例如，两者都为 0x100），系统会认为写操作与监视地址重叠，独占写失败。

- **误报（False Negatives）**
  - 这种方法可能会保守地标记独占写为失败，即使写操作实际上没有修改监视的地址（例如，0x104–0x10B 不包括 0x100）。
  - 这种“误报”优先考虑安全性而非精确性，确保不会写入不一致的数据。

#### 示例解析（示例 2-1）

- **独占读**：一个主控器读取地址 0x100，并将其标记为监视。
- **干扰写**：另一个主控器写入 0x104–0x10B（一个 2 个 WORD 的突发写）。
- **独占写**：第一个主控器尝试写入 0x100。
- **监控过程**
  - 写范围 0x104–0x10B 的变化最高位为位 3。
  - 掩码：`b111111110000`（0xFF0）。
  - 监视地址：`0x100 & 0xFF0 = 0x100`。
  - 写地址：`0x104 & 0xFF0 = 0x100`。
  - 结果：匹配，因此独占写失败，尽管 0x100 实际上未被写入。

#### 突发类型处理

- 系统在计算写访问的地址范围时，始终将突发类型视为**INCR**（递增）。
- 这种保守的方法确保了安全性，即使实际突发类型为**WRAP**（环绕）或**FIXED**（固定），系统也会假设可能的最大地址范围，以防止遗漏边缘情况。

#### 重要性

独占访问在多主控系统中至关重要，可以防止竞争条件。例如：

- 一个处理器读取地址 0x100 的计数器（值为 5），并打算将其递增到 6。
- 如果没有独占访问，另一个处理器可能在第一个处理器写入 6 之前将 7 写入 0x100，导致数据不一致。
- 有了独占访问，系统会检测到第二个写操作，并使第一个处理器的写操作失败，促使其重试操作。

#### 总结

独占访问提供了一种强大的、硬件支持的方法，确保共享内存系统中的数据一致性。通过使用监视器和保守的地址比较，系统保证了安全的行为，即使偶尔会出现误报，也使其成为复杂并发环境中的理想同步机制。

---
NAND memory accesses
This section describes:
Two phase NAND accesses
NAND command phase transfers on page 2-18 NAND data phase transfers on page 2-19. Two phase NAND accesses
The SMC defines two phases of commands when transferring data to or from NAND flash.
Command phase
Commands and optional address information are written to the NAND flash. The command and address can be associated with either a data phase operation to write to or read from the array, or a status/ID register transfer.
Data phase Data is either written to or read from the NAND flash. This data can be
either data transferred to or from the array, or status/ID register
information.
The SMC uses information contained in the AXI address bus, either awaddr[ or araddr[ signals, to determine whether the AXI transfer is a command or data phase access.
This information contained in the address bus additionally determines: the value of the command
the number of address cycles the chip select to be accessed.
During a command phase transfer, the address to be written to the NAND memory is transferred to the SMC using the AXI write channel.
Note
The size of the AXI transfer for data phase transfers must be larger than the width of the memory interface.

|   |   |   |
|---|---|---|
|Table 2-2 NAND AXI address setup|   |   |
|AXI address|Command phase|Data phase|
|[31:24]|Chip address|Chip address|
|[23]|NoOfAddCycles_2|Reserved|
|[22]|NoOfAddCycles_1|Reserved|
|[21]|NoOfAddCycles_0|ClearCS|
|[20]|End command valid|End command valid a|
|[19]|0|1|
|[18:11]|End command|End commandb|
|[10:3]|Start command|[10] ECC Last  <br>[9:3] Reserved|
|[2:0]|Reservedc|Reservedc|

Table 2-2 lists the fields of awaddr[ and araddr[ signals that control a NAND flash transfer.
Table 2-2 NAND AXI address setup 

a.
For a read data phase transaction, the end command valid must be 0.
b.
End command data is ignored if end command valid is not true.
c. The bottom three bits of a NAND access determine the valid data byte lanes, in the same way as for a standard AXI access.
NAND command phase transfers
A command phase transfer is always performed as an AXI write. The AXI awaddr[ bus, and Table 2-2 contain the following information:
Address cycles
The number of address cycles can be any value from zero to seven. Generally, up to five cycles are used during an array read or write, but a maximum of seven enables support for future devices.
Start command
The NAND command is used to initiate the required operation, for example:
page read 

page program
random page read
status or ID register read.
End command
The value of the second command, if required. This command is executed when all address cycles have completed. For example, some NAND memories require an additional command, following the address cycles, for a page read.
End command valid
Indicates whether the end command must be issued to the NAND flash.
Each address cycle consumes eight bits of address information. This is transferred to the SMC through the AXI write channel.
Note
To ease system integration, the SMC supports the use of multiple AXI write transactions to transfer address information. The following restrictions apply in this case:
1.
The AXI address [31:3] bits must not change between transactions. The first transaction must be doubleword aligned.
2. 3.
All other address information must be the same, with the exception of transaction length.
Data must be transferred in incrementing, consecutive accesses, that is, not wrapping, fixed, or sparse.
4.
Extra or unused beats in the last transaction must have write strobes disabled.
5.
Total number of beats must be less than the write FIFO depth.
NAND data phase transfers
Transfers data to or from the NAND flash, and can be performed as either an AXI read or write, depending on the required operation. The araddr[] or awaddr[ ] bus, and Table 2-2 on page 2-18 contain this information:
End command
The value of a command that is issued following the data transfer. This is required by some memories to indicate a page program following input of write data.



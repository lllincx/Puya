### 工艺温度检测控制器（PTSC，process temperature sensor controler）

### 简介

数字工艺检测器（ DPD，Process Detector）用于检测器件由于制造波动和长期漂移所引起的工艺变化。数字温度传感器（DTS，Temperature Sensor）是一种高精度、低功耗的结温传感器。PTSC提供一个通用接口，使得可以通过 APB 总线以读写方式访问 DTS和DPD。

### 主要特性

- 一个数字工艺检测器，一个数字温度传感器
- 对于每个传感器：
	- 两个可编程硬件告警，可配置为上升触发或下降触发，并支持迟滞功能；
	- 状态寄存器可记录接收到的最小值和最大值；
- 一个带 IRQ 的上电定时器，用于支持手动操作。
- 测试访问模式（Test Access Mode），可将控制器的串行测试访问数据寄存器接入 IJTAG（IEEE-1687）类型的嵌入式测试网络。

### 功能描述

#### 框图

PTSC集成了一个APB接口，用于控制温度传感器和工艺检测器

#### 引脚和内部信号

PTSC内部输入输出信号

| 内部信号名   | 信号类型 | 描述  |
| ------------ | -------- | ----- |
| ptsc_pclk    | input    |  PTSC主时钟     |
| ptsc_prstn   |  input        | PTSC复位（异步，低有效） |
| AMBA APB bus |    input/output      |  APB总线接口     |
| ptsc_irq     |   output        |  中断     |
| ptsc_tm_te   |  input         | 测试模式使能，当该信号置为有效时，设计进入生产测试模式。此时，所有内部派生出的时钟和/或复位信号都会被旁路，改为直接由顶层端口驱动。 |
| JTAG TDR IF  |  input/output         |  JTAG TDR测试接口     |
|              | **工艺检测器接口**     |       |
| clk_pd | output | 工艺检测器SDA时钟 |
| rstn_pd | output | 工艺检测器SDA复位 |
| pd_sdi | output | 工艺检测器SDA从机数据输入 |
| pd_sdo |input | 工艺检测器SDA从机数据输出 |
|  | **温度传感器器接口** | |
| clk_ts | output | 温度传感器SDA时钟 |
| rstn_ts | output | 温度传感器SDA复位 |
| ts_sdi | output | 温度传感器SDA从机数据输入 |
| ts_sdo |input | 温度传感器SDA从机数据输出 |

#### 时钟与复位

##### PTSC时钟

PTSC 由 `ptsc_pclk` 时钟驱动。

PTSC集成了一个时钟合成器（Clock Synthesizer）。该时钟合成器用于产生：

- 从串行数据适配器（Slave Serial Data Adapter，SDA）所需的时钟和时序选通信号；
- 内嵌 TS 模块所需的时钟 `clk_ts`。
- 内嵌 PD 模块所需的时钟 `clk_pd`。

时钟合成器中的 `CLK_SYNTH_HI[7:0]` 和 `CLK_SYNTH_LO[7:0]` 计数器可以对 `ptsc_pclk` 时钟进行整数分频，从而产生PD时钟`clk_pd`或 TS 时钟 `clk_ts`，支持的频率分频比范围为 1/2～1/512。相关配置参见时钟合成器寄存器 `PTSC_TSCCLKSYNTHR`。

另外还使用独立的计数器生成与 `clk_pd,clk_ts` 对齐的时序控制选通信号。这些时序选通信号由主串行适配器使用，用于控制：

- 串行数据输入的采样时刻；
- 串行数据输出的保持时间。

系统时钟 `ptsc_pclk` 的频率由 RCC 决定。

必须正确配置 `CLK_SYNTH_HI[7:0]` 和 `CLK_SYNTH_LO[7:0]`:

- 使生成的 `clk_ts` 串行时钟处于 TS 的工作频率范围内，即 1～2 MHz。
- 使生成的 `clk_pd` 串行时钟处于 PD 的工作频率范围内，即 4～8 MHz。

TS 时钟频率定义为：
$$
clk\_<pd|ts>\ frequency = \frac{ptsc\_pclk\ frequency}{CLK\_SYNTH\_HI+CLK\_SYNTH\_LO + 2}
$$


**配置示例**

例如，当 `ptsc_pclk = 64.0 MHz`，且 PD 的工作频率范围为 4～8 MHz 时，可将 `CLK_SYNTH_HI[7:0]` 和 `CLK_SYNTH_LO[7:0]` 均配置为 `0x03`，从而将 `ptsc_pclk` 到 `clk_tpd`的分频比设置为 8:1。此时 `clk_pd = 64.0 MHz / 8 = 8 MHz`，位于允许的 4～8 MHz 工作频率范围内，同时可获得 50% 的 `clk_tpd 占空比。

当 `ptsc_pclk = 8 MHz` 时，应配置

```
CLK_SYNTH_LO[7:0] = 0x0
CLK_SYNTH_HI[7:0] = 0x0
CLK_SYNTH_HOLD[3:0] = 0x1
```

此时：

```
clk_pd = 4 MHz,占空比50%
```

`CLK_SYNTH_HOLD[3:0]` 的值必须根据串行数据通路的**最坏情况传播延迟**进行配置，同时不能超过所合成时钟的周期：
$$
CLK\_SYNTH\_HOLD[3:0]\le CLK\_SYNTH\_HI[7:0]+CLK\_SYNTH\_LO[7:0]+1
$$

##### DTS 复位

DTS 使用异步、低电平有效的 `ptsc_rstn` 输入进行复位。

当主复位信号 `ptsc_rstn` 拉低有效（asserted）时，整个 PTSC 都会被复位，包括所有 APB 内部寄存器，主控制器和内嵌PD和TS 模块。

当 `ptsc_rstn` 解除复位（de-asserted）后，APB 接口会在经过 3 个时钟周期的延迟后开始响应访问请求。

#### 串行数据适配器（Serial Data Adapter，SDA）

串行数据适配器（Serial Data Adapter，SDA）允许通过串行数据接口（Serial Data Interface，SDIF）对PD/ TS 模块进行配置和控制。SDA 的主要目的是尽量减少从 PTSC 布线到各个PD/ TS 模块所需的信号数量。

通常，一个主设备会向其所有处于激活状态的PTSC从设备发送数据。不过，也可以禁止对一个或多个从设备进行编程，从而为不同从设备应用不同的配置。为了节省功耗，还可以通过关闭其时钟并强制复位的方式，将PD/ TS 模块完全禁用。

串行数据接口还提供**环回（Loop-back）功能**（图中以红色表示），用于支持系统集成测试，而无需给内嵌的 TS 模块上电。

##### SDA 数据格式

串行数据流由以下字段组成：

- 高电平有效的起始位
- 3 位寄存器地址 `SDIF_ADDR[2:0]`
- 寄存器写/非读使能信号 `SDIF_WRN`
- 24 位数据字段 `SDIF_WDATA[23:0]`

输入和输出串行数据流的格式如图所示。

需要注意的是，串行数据流采用小端传输方式，即各个数据字段均按照最低有效位先传的顺序进行移位传输。

##### SDA 读

从 SDA 从寄存器读取数据时（`SDIF_WRN = 0`），SLV SDI 位流会移位输出到 SLV SDO，并延迟一个 `clk_pd/ts` 周期，同时寄存器读数据值通过 `SDIF_RDATA[23:0]` 输出。随后，该读数据值会在 PTSC 控制器的 `SDIF_RDATAR` 寄存器中可用。

##### SDA 写

向 SDA 从寄存器写入数据时（`SDIF_WRN = 1`），SLV SDI 位流会自动移位输出到 SLV SDO，同时：

```
SDIF_RDATA[23:0] = SDIF_WDATA[23:0]
```

随后，写数据的环回值会在对应的 PTSC 控制器 `SDIF_RDATAR` 寄存器中可用。

当 `SDIF_WRN = 1` 且 `SDIF_ADDR[2:0] = 0x3` 时，通过写入只读的 `SDATS_DR` 寄存器可以进入一种特殊环回模式。在该模式下，环回数据值还会被写入 PTSC 控制器的 PD/TS 数据寄存器 `SDIF_RDATAR`。向 PD/TS 数据寄存器写入环回数据时，SDA 的 `PD/TS_DATA[23:0]` 字段必须设置为 `0x0`。

`SDIF_RDATAR` 的环回功能可用于验证 PTSC 控制器与远端 PTSC 从设备之间串行数据传输的完整性。

特殊的 `SDIF_RDATAR` 环回功能还可用于在不启动内嵌 PD/TS 模块的情况下测试 PTSC 控制器的运行，例如发生故障或告警时。

当 PTSC 从设备被配置为自动数据恢复模式，即  `SDATS_CR` 寄存器中的 `PD/TS_AUTO` 位被置位时，环回功能会被禁用。

##### SDA 自动数据恢复

自动数据恢复通过 `SDATS_CR` 寄存器中的 `PD/TS_AUTO` 位使能。

在自动数据恢复模式下，`SDIF_SR` 寄存器中的 `SDIF_LOCK` 标志位置位，SDA 接口变为只写接口，所有 SDA 读请求都会被忽略。

在该模式下，每当有新的采样数据可用时，SLV 会自动将 `PD/TS_DATA[23:0]` 串行传输到 PTSC 控制器，同时设置：

```verilog
SDIF_ADDR[2:0]=0x3
SDIF_WRN=1
```

自动恢复的数据随后可在 PTSC 控制器的 `SDIF_RDATAR,SDIF_RDATA` 寄存器中读取。

##### SDA SDIF 编程

通过 PD/TS SDIF 控制寄存器 `SDIF_CFGR` 访问 SDA 从设备。访问时需要配置：`SDIF_WDATA[23:0],SDIF_ADDR[2:0],SDIF_WRN`，并置位 `SDIF_PROG` 。通常，一次 SDA 读或写请求可以通过一次 PTSC 寄存器写访问完成配置。发出编程请求后，`SDIF_SR` 寄存器中的 `SDIF_BUSY` 标志位会被置位。在当前访问完成之前，后续所有读写编程请求都会被忽略。

##### SDA 控制器操作

SDA 从控制器支持两种工作模式：手动模式（默认）和自动模式。在这两种模式下，内嵌的 PD/TS 模块均通过 `SDATS_CFGR` 寄存器进行配置。

在手动工作模式下，当 `SDATS_CR` 寄存器中的 `PD/TSAUTO` 位未置位时，内嵌的 PD/TS 模块直接通过 `SDATS_CR` 寄存器中的 `PD/TSPD`、`PD/TSRSTN`、`PD/TSRUN_ONCE`、`PD/TSRUN_CONT` 和 `PD/TSCLOAD` 字段进行控制。在手动模式下，用户需要确保 `PD`、`RSTN`、`CLOAD` 和 `RUN` 信号按照正确的顺序并在适当的时刻施加。转换结束时，PD/TS 模块的采样数据会被捕获到 SDA 从设备的 `SDATS_DR` 寄存器中。为了从从端 SDA 获取采样数据，用户必须轮询 `SDATS_DR` 寄存器，或者在读取 `SDATS_DR` 寄存器之前预留足够的时间，以确保转换已经完成。

在自动模式下，当 `SDATS_CR` 寄存器中的 `PD/TSAUTO` 位置位时，内嵌的 PD/TS 模块由从端 SDA 控制。当 `PD/TSSDATS_CR` 寄存器中的 `PD/TSRUN_ONCE` 或 `PD/TSRUN_CONT` 任一位置位时，从端 SDA 会按照规定的顺序控制驱动 PD/TS 模块的 `PD`、`RSTN`、`CLOAD` 和 `RUN` 信号，使 PD/TS 模块执行一次或多次转换。在该模式下，转换结束时，PD/TS 模块的采样数据会先被捕获到 SDA 从设备的 `SDATS_DR` 寄存器中，随后自动串行传输至 PTSC 控制器。

##### **SDA从寄存器**

串行数据适配器寄存器可通过 PTSC 控制器的 SDIF 接口进行访问

#### 告警

PTSC为每个传感器模块提供两个告警：告警 A（Alarm A） 和 告警 B（Alarm B）。告警支持可编程迟滞，并且可以配置为检测采样值的上升或下降。当迟滞阈值设置为与告警阈值相等时，告警被禁用，这也是默认状态。告警使能后，如果恢复得到的数据采样值达到或超过相应的上升或下降告警阈值，就会产生中断。一旦告警被触发，迟滞阈值会提供一个恢复窗口，在该窗口内告警不会再次触发。

##### 下降告警

当迟滞阈值大于告警阈值时，会形成下降告警。配置为下降告警后，当恢复得到的采样值大于或等于迟滞阈值时，告警进入就绪状态（armed）。进入就绪状态后，当恢复得到的采样值小于或等于告警阈值时，下降告警被触发。告警触发后会自动退出就绪状态，只有当采样值再次大于或等于迟滞阈值时，才会重新进入就绪状态。如果接收到无效采样值，例如检测到非预期的 fault 标志或 type 标志，告警也会退出就绪状态。

##### 上升告警

当迟滞阈值小于告警阈值时，会形成上升告警。配置为上升告警后，在以下情况下，告警会进入就绪状态：

1. 相关时钟合成器首次使能时，即进行初始转换时；
2. 恢复得到的采样值小于或等于迟滞阈值时；
3. 接收到无效采样值时，例如检测到非预期的 fault 标志或 type 标志。

进入就绪状态后，当恢复得到的采样值大于或等于告警阈值时，上升告警被触发。告警触发后会自动退出就绪状态，只有当采样值再次小于或等于迟滞阈值时，才会重新进入就绪状态。

#### 主要 APB 编程流程

本节给出了若干编程流程示例，用于配置PTSC、编程 SDA 寄存器，以及执行单次或连续温度转换。

##### 配置PTSC

1. 配置PTSC中断。

	1. 写 `PTSC_IRQ_EN` 寄存器。

		定时器仅用于传感器工作在旁路模式（bypass mode）时，因此该中断必须保持禁用。

	2. 写 `PTSC_PD/TS_IRQ_ENABLE` 寄存器。

		在极少数情况下，如果传感器模块报告故障，则恢复得到的数据值将被视为无效，并且所有已激活的报警都会被解除，直到故障被清除。当某个传感器模块首次报告故障时，会产生 fault IRQ。如果用户未清除该故障，则之后不会再产生新的故障中断。因此，建议始终使能该中断。

2. 配置PTSC告警。

	1. 写 `PTSC_PD/TS_ALARMA_CFG` 寄存器。

		当 `ALARM_THRESH` 不等于 `HYST_THRESH` 时，报警功能被使能。使能报警时，应确保同时使能对应的 IRQ。

	2. 写 `PTSC_PD/TS_ALARMB_CFG` 寄存器。

		当 `ALARM_THRESH` 不等于 `HYST_THRESH` 时，报警功能被使能。使能报警时，应确保同时使能对应的 IRQ。

3. 配置PTSC采样控制。

	1. 写 `PTSC_PD/TS_SMPL_CTRL` 寄存器。
		- 当置位 `SMPL_DISCARD` 时，PD/TS 数据样本会被暂时丢弃，但采样计数器仍会继续递增。
		- 当置位 `SMPL_CTR_HOLD` 时，采样计数器达到最大值后不会发生回卷。
		- 当置位 `SMPL_CTR_DISABLE` 时，采样计数器被禁用。

4. 对每个 PD/TS 实例写 `PTSC_PD/TS_HILO_RESET` 寄存器。

##### 配置 SDA 寄存器

1. 编程 SDA 寄存器。

	1. 读 `PTSC_PD/TS_SDIF_STATUS` 寄存器。

		`SDIF_LOCK` 标志必须为低，表示尚未使能 SDIF 自动模式。

		继续操作之前，需要确认串行数据接口处于空闲状态，即：`SDIF_BUSY = 0`

	2. 写 `PTSC_PD/TS_SDIF_CTRL` 寄存器，对远端从设备的 SDA 寄存器进行写操作。
	
		```text
	SDIF_PROG = 0x1
		SDIF_WRN  = 0x1
	SDIF_ADDR[2:0]：用于选择目标 SDA 寄存器。
		SDIF_WDATA[23:0]：提供要写入 SDA 寄存器的数据。
		```
	
		SDA 寄存器应按照以下顺序进行编程：

		```text
	PTSC_SDA_PD/TS_TIMERR
		PTSC_SDA_PD/TS_CFGR
	PTSC_SDA_PD/TS_CR
		```
	

> 如果在 `PTSC_SDA_PD/TS_CTRL` 寄存器中同时置位 `PD/TS_AUTO` 和 `PD/TS_RUN_ONCE` 或 `PD/TS_RUN_CONT`，则会启动传感器进行转换，并将 `SDIF_LOCK` 标志置位。一旦 `SDIF_LOCK` 被置位，SDA 寄存器将变为只写。
>
> `SDIF_WDATA[23:0]` 中的值也会反映到 `PTSC_PD/TS_SDIF_RDATA` 寄存器中。

2. 读取 SDA 寄存器值。

	1. 读 `PTSC_PD/TS_SDIF_STATUS` 寄存器。

		- `SDIF_LOCK` 标志必须为低，表示 SDIF 自动模式尚未使能。

		- 继续操作之前，需要确认串行数据接口当前未被占用，即：`SDIF_BUSY = 0`

	2. 写 `PTSC_PD/TS_SDIF_CTRL` 寄存器，以读取远端从设备的 SDA 寄存器。
	
	  ```text
	  SDIF_PROG = 0x1
	  SDIF_WRN  = 0x0
	  SDIF_ADDR[2:0]：用于选择要读取的 SDA 寄存器。
	  SDIF_WDATA[23:0]：读取操作中不使用该字段，因此可以写任意值。
	  ```
	
	
	> 一旦 `SDIF_LOCK` 标志被置位，SDA 寄存器将变为只写，此后所有读请求都会被忽略。
	>
	> 读出的数据 `SDIF_RDATA[23:0]` 同样会反映到 `PTSC_PD/TS_SDIF_RDATA` 寄存器中。
	
	3. 从 `PTSC_PD/TS_SDIF_RDATA` 寄存器读取 SDA 寄存器值。

##### 单次运行

1. 启动单次转换。

	1. 读 `PTSC_PD/TS_SDIF_STATUS` 寄存器。

		- 确认`SDIF_LOCK = 0`表示 SDIF 自动采样模式尚未使能。

		- 确认`SDIF_BUSY = 0`表示串行数据接口当前未被占用。
		
	2. 写 `PTSC_PD/TS_SDIF_CTRL` 寄存器。

		```text
		SDIF_PROG        = 0x1
		SDIF_WRN         = 0x1
		SDIF_ADDR[2:0]   = 0x0 （用于选择 PTSC_SDA_PD/TS_CR）
		SDIF_WDATA[23:0] = 0x000104 （用于置位PD/TS_AUTO和自清的PD/TS_RUN_ONCE)
		```
	
2. 等待采样结束中断请求

	1. 读 `PTSC_PD/TS_SDIF_DONE` 寄存器。
		
		检查 `SDIF_SMPL_DONE` 标志是否置位，以确认一个或多个 `SDATS_DR` 寄存器已经更新。
	2. 读 `PTSC_PD/TS_SMPL_CNT` 寄存器。
		
		每当 PD/`TS_DATA[23:0]` 更新时，`PTSC_PD/TS_SMPL_CNT` 中的采样计数器都会递增。
	3. 读 `PTSC_PD/TS_SDIF_RDATA` 寄存器。
		- 读取传感器的采样数据，类型和错误信息。
		- 如果 fault 位被置位，则该次采样数据不可靠，必须丢弃。
		- 读取 `SDATS_DR` 寄存器后，`SDIF_SMPL_DONE` 寄存器中的 `SDIF_SMPL_DONE` 标志会自动清零。

##### 连续运行

1. 启动连续转换。

	1. 读 `PTSC_PD/TS_SDIF_STATUS` 寄存器。

	  - 确认`SDIF_LOCK = 0`表示 SDIF 自动采样模式尚未使能。

	  - 确认`SDIF_BUSY = 0`表示串行数据接口当前未被占用。
	
	2. 写 `DTS_TSCSDIF_CR` 寄存器。

	  ```text
	  SDIF_PROG        = 0x1
	  SDIF_WRN         = 0x1
	  SDIF_ADDR[2:0]   = 0x0 （用于选择 PTSC_SDA_PD/TS_CR）
	  SDIF_WDATA[23:0] = 0x000108（用于置位PD/TS_AUTO和PD/TS_RUN_CONT)
	  ```
	
2. 等待采样结束中断请求

	1. 读 `PTSC_PD/TS_SDIF_DONE` 寄存器。
		
		检查 `SDIF_SMPL_DONE` 标志是否置位，以确认一个或多个 `SDATS_DR` 寄存器已经更新。
	2. 读 `PTSC_PD/TS_SMPL_CNT` 寄存器。
	
		每当 PD/`TS_DATA[23:0]` 更新时，`PTSC_PD/TS_SMPL_CNT` 中的采样计数器都会递增。
	
	3. 读 `PTSC_PD/TS_SDIF_RDATA` 寄存器。
	
		- 读取传感器的采样数据，类型和错误信息。
		- 如果 fault 位被置位，则该次采样数据不可靠，必须丢弃。
		- 读取 `SDATS_DR` 寄存器后，`SDIF_SMPL_DONE` 寄存器中的 `SDIF_SMPL_DONE` 标志会自动清零。

#### 中断

PTSC提供一个高电平有效的电平型硬件中断输出。该中断输出是所有内部传感器中断源以及公共延时定时器中断的逻辑或结果。

通过中断请求控制寄存器，可以方便地对中断进行使能、屏蔽以及查看中断状态。

来自各个传感器的中断会被合并为一个中断，其状态可以通过 `PTSC_PD/TS_IRQ_STATUS` 寄存器查看。

每个传感器模块都可以基于以下中断源产生中断：

- `irq_smpl`：表示对应传感器的采样数据已经更新。
- `irq_alarma`：表示对应传感器恢复得到的采样值已经达到或超过设定的 Alarm A 阈值。
- `irq_alarmb`：表示对应传感器恢复得到的采样值已经达到或超过设定的 Alarm B 阈值。
- `irq_fault`：表示对应的 传感器报告了故障。

当发生中断事件时，硬件会检测该事件的上升沿，并在中断源寄存器 `PTSC_PD/TS_IRQ_STATUS` 中置位对应的标志。

`PTSC_PD/TS_IRQ_STATUS` 中的各中断请求状态位分别与 `PTSC_PD/TS_IRQ_ENABLE` 寄存器中对应的中断使能位进行逻辑与，从而生成中断请求位。

随后，这些中断请求位进行逻辑或，并由 `ptsc_pclk` 时钟寄存后，生成送往 中断请求控制逻辑的中断输出。

一旦中断源位被置位，该位将保持置位状态，必须置位 `PTSC_PD/TS_IRQ_CLR` 寄存器中的对应位才能将其清除。

如果对应中断已经使能，清除该中断源位的同时也会清除相应的中断请求。

当以下标志被置位，或者 `PTSC_PD/TS_IRQ_TEST` 寄存器中的对应强制位被置位时，会触发中断事件。这些强制位允许软件手动产生中断，用于软件测试。

- `irq_smpl`：每当恢复得到一个新的 TS 数据样本时置位。
- `irq_alarma`：每当达到 Alarm A 阈值条件时置位。
- `irq_alarmb`：每当达到 Alarm B 阈值条件时置位。
- `irq_fault`：每当 传感器置位其 fault 输出时置位。

通常情况下，内部温度传感器会持续运行，并依靠 Alarm 中断来报告温度超出设定范围的情况。

对于这类持续运行的传感器，用户通常会禁用采用完成中断；只有在需要记录每一个采样数据时，才需要使能该中断。

PD/TS 中断

| 中断事件   | 事件标志          | 中断使能控制位 | 中断清除方式     |
| ---------- | ----------------- | -------------- | ---------------- |
| irq_smpl   | IRQ_STATUS_DONE   | IRQ_EN_DONE    | IRQ_CLEAR_DONE   |
| irq_alarma | IRQ_STATUS_ALARMA | IRQ_EN_ALARMA  | IRQ_CLEAR_ALARMA |
| irq_alarmb | IRQ_STATUS_ALARMB | IRQ_EN_ALARMB  | IRQ_CLEAR_ALARMB |
| irq_fault  | IRQ_STATUS_FAULT  | IRQ_EN_FAULT   | IRQ_CLEAR_FAULT  |
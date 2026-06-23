## 4.6 LPI 接口

DMAC 通过 LPI 接口为时钟和电源提供低功耗集成支持。Q-Channel 接口提供时钟静默（quiescence）能力，P-Channel 接口则允许在 DMAC 处于空闲且无活动进行时进行电源管理。DMAC 可通过活动指示信号请求电源和时钟。DMAC 根据当前内部状态接受或拒绝电源和时钟控制器的请求。

### 4.6.1 LPI 电源 P-Channel

电源 P-Channel 接口用于向 DMAC 请求电源静默。电源控制器驱动请求，DMAC 根据当前内部状态接受或拒绝该请求。DMAC 也可通过 `pactive` 信号为某项活动请求电源。

`pactive` 支持 10 位宽的活动指示，范围从 Off 到 Warm reset。但 DMAC 仅断言 Off、Full retention mode 和 On 三种指示。

DMAC 不支持强制断电。当请求发生且有活动正在进行时，DMAC 仅拒绝该请求并继续运行。该请求除 P-Channel 握手外，不会对操作产生任何影响。

### 4.6.2 LPI 时钟 Q-Channel

时钟 Q-Channel 接口用于向 DMAC 请求时钟静默。时钟控制器驱动请求，DMAC 根据当前内部状态接受或拒绝该请求。DMAC 也可通过 `qactive` 信号为某项活动请求时钟。

DMAC 不支持强制时钟关断。当请求发生且有活动正在进行时，DMAC 仅拒绝该请求并继续运行。该请求除 Q-Channel 握手外，不会对操作产生任何影响。

## 5.9 DMAC 电源管理与 DMAC 控制

本节描述 DMA-350 的电源管理与配置。

### 5.9.1 电源管理

DMA-350 具有独立的电源和时钟控制管理系统。

#### 5.9.1.1 电源 P-Channel

DMA-350 使用一个完整的 LPI P-Channel 进行电源管理。该功能的目的是在非活跃使用期间启用更低的功耗状态（移除供电），以降低功耗。电源 P-Channel 用于控制 DMAC 逻辑的电源状态。

通过 P-Channel 接口可请求以下四种电源状态，其他状态请求将被拒绝：

- On
- Warm reset mode
- Full retention mode
- Off

DMAC 在 P-Channel 接口下具有简单的电源管理场景：

- 当 DMAC **处于活跃状态**时，电源静默请求被拒绝，操作继续进行。
- **Warm reset mode** 请求会暂停所有正在进行的通道操作；从 Warm reset mode 退出并恢复到 On 状态后，通道操作将恢复。
- 当 DMAC **正在等待事件**时，进入 Full retention mode 的静默请求被接受，但 Off 状态请求被拒绝。
- 当 DMAC **处于非活跃状态**时，Off 状态请求被接受。进入 Off 状态前，FIFO 将被清空，寄存器值不予保留。

下图展示了支持的电源状态及其状态间的转换。

![image.png|600](https://pic.lllincx.cn/20260403151107389.png)

进入更低功耗模式（Full retention mode、Off）可通过配置寄存器 `NSEC_CTRL` 和 `SEC_CTRL` 的 `DISMINPWR` 字段禁用。该设置的效果为：如果 `DISMINPWR` 中设定的最低电源状态高于所请求的电源状态，且至少有一个通道分别被配置为 Non-secure 或 Secure，则该电源状态请求将被拒绝。

当 DMA 处于等待事件状态时进入 Full retention mode，可通过配置寄存器 `NSEC_CTRL` 和 `SEC_CTRL` 的 `IDLERETEN` 字段进行禁用和启用。该设置的效果为：如果 `IDLERETEN` 被设为 Disabled，所请求的状态为 Full retention mode，且至少有一个 Non-secure 或 Secure 通道（取决于 `IDLERETEN` 字段对应的安全属性）正在等待事件，则电源状态请求将始终被拒绝。

有关 P-Channel 握手机制的更多信息，请参阅 *AMBA® Low Power Interface Specification* 文档。

有关 P-Channel 接口信号，请参阅"信号描述"章节。

#### 5.9.1.2 时钟 Q-Channel

DMA-350 使用一个完整的 LPI Q-Channel 进行时钟管理。该功能的目的是在非活跃使用期间关断时钟以降低功耗。时钟 Q-Channel 用于控制 DMAC 逻辑的时钟开启与关断。

Q-Channel 接口控制 DMAC 的时钟管理：

- 当 DMAC **处于活跃状态**时，时钟静默请求被拒绝，操作继续进行。
- 当 DMAC **正在等待事件或处于非活跃状态**时，静默请求被接受，时钟可以被关断。

有关 Q-Channel 握手机制的更多信息，请参阅 *AMBA® Low Power Interface Specification* 文档。

有关 Q-Channel 接口信号，请参阅"信号描述"章节。

### 5.9.2 配置

DMA-350 可通过其配置寄存器进行设置。这些寄存器被划分为多个帧（frame），每个寄存器帧占用 256 字节的地址空间。

寄存器帧的布局如下图所示。
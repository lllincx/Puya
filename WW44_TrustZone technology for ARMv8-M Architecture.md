# 第 1 章 引言

适用于 ARMv8-M 的 ARM® TrustZone® 技术是一种可选的安全扩展（Security Extension），旨在为各类嵌入式应用提供提升系统安全性的基础。如果实现了该安全扩展，系统将默认以安全状态（Secure state）启动；若未实现，则系统始终处于非安全状态（Non-secure state）。TrustZone 技术使处理器能够识别并感知可用的安全状态。

## 1.1 安全世界与非安全世界

ARM TrustZone 技术使系统与软件可以被划分为安全（Secure）与非安全（Non-secure）两个世界。

安全世界的软件可以访问安全与非安全的存储与资源；非安全世界的软件只能访问非安全的存储与资源。该安全状态与现有的 Thread 模式和 Handler 模式是正交关系，因此在安全与非安全状态下都可以运行 Thread 与 Handler 模式。

> Thread 模式还可以分为特权（Privileged）或非特权（Unprivileged）。

带安全扩展的 ARMv8-M 架构是一项可选的架构扩展。若实现了该安全扩展，系统默认以安全状态启动；若未实现，系统将始终处于非安全状态。ARM TrustZone 技术并不覆盖安全性的全部方面，例如不包含密码学。

在采用 ARMv8-M 且实现 Security Extension 的设计中，与系统安全密切相关的组件应放在 Secure 世界。这些关键组件包括：

- 安全引导加载程序（Secure boot loader）
- 秘密密钥（Secret keys）
- Flash 编程支持（Flash programming support）
- 高价值资产（High value assets）

其余应用放在 Non-secure 世界。

Secure（可信）与 Non-secure（非可信）软件可以协同工作，但 Non-secure 应用不能直接访问 Secure 资源。对 Secure 资源的任何访问都必须通过由 Secure 软件提供的 API，并由这些 API 执行身份/权限校验以决定是否允许访问。采用这种安排，即使 Non-secure 应用存在漏洞，攻击者也无法拿下整颗芯片。

### 1.1.1 安全平台的安全性要求

要确保平台安全，安全设计不能只停留在处理器架构层面，而必须在整个系统层级做增强以满足安全需求。要求包括：

- 总线协议需扩展以支持安全属性（Secure/Non-secure 标记等）。
- 需要额外的系统组件来管理安全，例如为 Secure 与 Non-secure 外设管理访问权限。
- 调试架构必须具备安全感知能力，防止通过调试口或追踪功能接触到机密信息。
- 运行在 Secure 世界 的软件必须谨慎编写，避免引入漏洞。

### 1.1.2 ARM® TrustZone®（ARM®v8-M）与 ARM® Cortex®-A 处理器的关系

TrustZone 的概念并不新鲜：该技术已在 ARM Cortex-A 系列处理器上应用多年，如今已扩展覆盖到 ARMv8-M 处理器。
适用于 ARMv8-M 的 ARM TrustZone 技术与 Cortex-A 版本不同，其设计针对微控制器和低功耗 SoC 应用进行了优化。在这类应用中，低功耗、低内存占用和低延迟是关键因素。为获得最佳效果，ARMv8-M 的 TrustZone 并未复用 Cortex-A 的现有方案，而是自底向上重新设计。因此，ARMv8-M 架构中 TrustZone 的底层运行机制与 Cortex-A 处理器中的实现并不相同。

## 1.2 处理器的安全状态

从简化视角看，程序地址决定处理器所处的安全状态：要么是 Secure，要么是 Non-secure。

- 当处理器在非安全内存中执行程序代码时，处理器处于 Non-secure 状态。
- 当处理器在安全内存中执行程序代码时，处理器处于 Secure 状态。
- 当处理器处于 Secure 状态时，取指必须来自安全内存。

ARMv8-M 架构允许在 Secure 与 Non-secure 软件之间进行函数调用或分支跳转。但对 **Non-secure → Secure** 的转换施加了限制，确保只能通过有效的 Secure API 入口进行调用；当由从 Non-secure API 返回到 Secure 代码而触发转换时，同样适用这些限制。

> 从 Non-secure 切换到 Secure 状态时有一项特殊规定：转换处的第一条指令必须是 SG 指令，且执行 SG 指令时处理器必须处于 Non-secure 状态。

本节包含以下小节：

- 1.2.1 设计特性（见 1-16 页）
- 1.2.2 ARM®v8-M 的 TrustZone® 与 ARM® Cortex®-A 处理器中 TrustZone® 的实现差异（见 1-17 页）
- 1.2.3 ARM®v8-M 的 TrustZone® 与 ARM®v8-R 架构虚拟化方法的差异（见 1-17 页）

### 1.2.1 设计特性

- 非安全代码只能通过**有效入口**调用安全函数，入口数量不受限制。
- 跨安全域调用的切换开销低：Non-secure 调 Secure 仅额外一条 **SG** 指令；Secure 调 Non-secure 仅增加少量时钟周期。
- 执行安全代码期间仍可服务 **非安全中断**，对中断延迟影响最小；需要**压栈完整寄存器组**，而非仅由调用者保存寄存器。
- 处理器**默认以 Secure 状态启动**，便于实现可信根（例如安全启动）。
- 低功耗  
   — 无需为 Secure/Non-secure 分别设置独立寄存器组，同时仍能防止非安全中断处理程序窥探安全操作所用数据。
- 易用性  
   — 中断处理程序仍可用 C 编写；非安全软件可用标准 C/C++ 函数调用访问 Secure API。
- 高灵活性  
   — 允许 Secure 软件调用 Non-secure 函数（安全侧受保护中间件需访问非安全侧驱动时常见）。  
   — Secure 状态下也有特权/非特权执行级，因而可在安全侧承载多个软件组件并在其间提供保护机制。

### 1.2.2 ARMv8-M 的 TrustZone 与 ARM Cortex-A 处理器中 TrustZone 的实现差异

在高层概念上，ARMv8-M 的 TrustZone 与 Cortex-A 处理器中的 TrustZone 相似：处理器都具有 Secure 与 Non-secure 两种状态，Non-secure 软件只能访问 Non-secure 存储器。

ARMv8-M 的 TrustZone 以小型、节能系统为目标设计。不同于 Cortex-A，Secure 与 Non-secure（Normal）世界的划分基于内存映射，且状态转换在异常处理代码中自动发生。

具体实现差异包括：

- ARMv8-M 的 TrustZone 支持多个安全函数入口点；而在 Cortex-A 的 TrustZone 中，Secure Monitor 处理程序是唯一入口。
- 执行安全函数期间，仍可响应 Non-secure 中断。

因此，ARMv8-M 的 TrustZone 针对低功耗微控制器类应用做了优化：

- 许多具实时处理需求的微控制器应用强调确定性与低中断延迟，因此在运行安全代码时仍能服务中断至关重要。
- 允许 Secure 与 Non-secure 状态共享寄存器组，使 ARMv8-M 的功耗可与 ARMv6-M 或 ARMv7-M 相当。
- 状态切换开销低，便于 Secure 与 Non-secure 软件频繁交互（当安全固件含 GUI 库或通信协议栈等软件库时尤为常见）。

### 1.2.3 ARMv8-M 的 TrustZone 与 ARMv8-R 架构虚拟化方法的差异

ARMv8-M 的 TrustZone 也不同于 ARMv8-R 架构所支持的虚拟化方法。

在虚拟化系统中，各个虚拟化软件环境（虚拟机，VM）彼此隔离，VM 之间只能通过管理程序（hypervisor）、中断或共享内存进行交互。

因此，不同 VM 间的软件交互需要额外的执行周期与软件开销；这在高性能的 ARM Cortex-R 处理器上可以接受，但对资源受限的 ARM Cortex-M 应用并不理想。此外，虚拟化系统的内存占用往往显著更大，因为需要管理程序软件，且常包含多个操作系统。

## 1.3 内存系统与内存分区

整个 4GB 地址空间被划分为 Non-secure 和 Secure 两类内存区域。

Non-secure（NS）  
Non-secure 地址用于所有在器件上运行的软件可访问的内存与外设。  
Non-secure 事务来源于以 Non-secure 身份运行（或被视为 Non-secure）的主设备，或来源于 Secure 主设备访问 Non-secure 地址。Non-secure 事务**仅被允许**访问 Non-secure 地址，系统必须确保 Non-secure 事务被拒绝访问 Secure 地址。

Secure 空间进一步分为两类：

Secure（S）  
Secure 地址用于只有 Secure 软件或主设备才能访问的内存与外设。  
当目标是 Secure 地址时，Secure 事务来源于以 Secure 身份运行（或被视为 Secure）的主设备。

Non-secure Callable（NSC）  
NSC 是一种**特殊的 Secure 内存位置**。这是 ARMv8-M 处理器**唯一允许**存放 SG 指令的内存类型，借此使软件可以从 Non-secure 切换到 Secure 状态。引入 NSC 的目的，是把 SG 指令的功能**限制在 NSC 内存**中，避免普通 Secure 内存中的其它二进制数据（例如查找表）恰好与 SG 指令编码相同而被误当作进入 Secure 的入口。

本节包含以下小节：

- 1.3.1 NSC 内存区域（见 1-18 页）
- 1.3.2 归属单元（SAU 与 IDAU）（见 1-18 页）
- 1.3.3 分组的内部资源（见 1-19 页）
- 1.3.4 Secure 与 Non-secure 的 MPU（见 1-20 页）

### 1.3.1 NSC 内存区域

NSC 区通常存放由小型分支 veneer（入口点）组成的表。为防止 Non-secure 应用跳转到无效入口，提供了 Secure Gateway（SG）指令。

当 Non-secure 程序调用 Secure 侧的函数时：

- 该 API 的**第一条指令必须是 SG**。
- 这条 SG 指令**必须位于 NSC 区域**内，该区域由 SAU（Security Attribution Unit）或 IDAU（Implementation Defined Attribution Unit）定义。

引入 NSC 的原因，是为了防止其它二进制数据（例如查找表）因数值恰与 SG 指令操作码相同而被当作进入 Secure 状态的入口。通过区分 NSC 与 Secure 两种内存类型，含有二进制数据的 Secure 程序代码可以安全地放在 Secure 区而不直接暴露给 Non-secure 世界，只能通过 NSC 内存中的有效入口进行访问。

### 1.3.2 归属单元（SAU 与 IDAU）

微控制器或 SoC 的设计者将内存空间划分为 Secure 与 Non-secure 区域。部分区域由 SAU（可由软件配置）定义，或由连接在处理器 IDAU 接口上的器件特定控制逻辑来定义。该内存分区也用于把外设标定为 Secure 或 Non-secure。

SAU 可在 **Secure 状态**下编程，其编程者模型与 MPU 类似。SAU 的实现由设计人员配置：**SAU 总是存在**，但区域数量由设计人员决定。也可以由设计人员使用 **IDAU** 定义**固定**的内存映射，再用 **SAU** 对其中部分内存的**安全属性做覆盖**。

SAU 与 IDAU 还为每个内存区域定义了**区域号**。区域号为 **8 位**，供 **TT 指令**使用，以便软件确定内存对象的**访问权限与安全属性**。

### 1.3.3 分组的内部资源

若干内部资源在 Secure 与 Non-secure 状态之间是分组（banked）的。

- 处理器内的寄存器：  
   — **堆栈指针**在 Secure/Non-secure 间分组，便于分别使用各自的栈。  
   — **中断屏蔽寄存器**如 `PRIMASK`、`FAULTMASK`、`BASEPRI` 为分组寄存器。  
   — `FAULTMASK` 与 `BASEPRI` 仅在**带 Main Extension 的 ARMv8-M 架构**上提供。这样可复用现有软件，同时 Non-secure 软件**不能影响** Secure 软件的运行。  
   — **特殊寄存器 `CONTROL` 的位 0 与位 1**为分组位，Secure 与 Non-secure 软件可拥有不同的栈指针选择与特权设置。

此外，MPU、SysTick 计时器以及 SCB（系统控制块）中的部分寄存器也采用分组机制。  
例如，向量表偏移寄存器（VTOR）是分组的，使 Secure 与 Non-secure 的向量表彼此分离。软件通过原有地址访问这些寄存器时，将依据当前处理器状态访问到相应视图：Secure 访问看到 Secure 外设；Non-secure 访问看到 Non-secure 外设。Secure 软件也可以通过别名地址（alias）访问这些组件的 Non-secure 版本。

### 1.3.4 Secure 与 Non-secure 的 MPU

与早期 M 系列相同，MPU（内存保护单元）是可选的。根据应用需求可不实现 MPU 以降低面积/功耗，或只实现 Secure MPU、只实现 Non-secure MPU，或两者同时实现。  
Secure 与 Non-secure 的 MPU 区域数量可不同。处理器当前处于哪一安全状态，就由对应的 Secure/Non-secure MPU 对产生的总线访问进行查表与权限检查。

## 1.4 在 Secure 与 Non-secure 状态之间切换

带 Security Extension 的 ARMv8-M 架构允许 Secure 与 Non-secure 软件之间进行直接调用。

本节包含以下小节：

- 1.4.1 安全状态转换（见 1-22）
- 1.4.2 调用 Non-secure 软件（见 1-23）
- 1.4.3 通过异常与中断进行状态转换（见 1-23）

### 1.4.1 安全状态转换

在 ARMv8-M 处理器中，提供以下指令处理安全状态转换：Secure Gateway（SG）、Branch with exchange to Non-secure state（BXNS）以及 Branch with link and exchange to Non-secure state（BLXNS）。安全状态的转换见下图。

可用于状态转换的指令说明：

- **SG**：用于从 Non-secure 切换到 Secure，且必须作为 Secure 入口点的**第一条**指令。
- **BXNS**：由 Secure 软件用于分支或返回到 Non-secure 程序。
- **BLXNS**：由 Secure 软件用于调用 Non-secure 函数。

当且仅当入口点的第一条指令为 **SG**，且该入口位于 **NSC（Non-secure Callable）** 内存位置时，允许 Non-secure 直接调用 Secure API。

当 Non-secure 程序调用 Secure API 完成后，会通过 **BXNS** 返回到 Non-secure 状态。若 Non-secure 程序试图在没有有效入口的情况下跳转或调用某个 Secure 地址，将产生故障事件：在 ARMv8-M 架构中由 **Secure 状态下的 HardFault** 处理；在带 **Main Extension** 的 ARMv8-M 架构中由 **SecureFault** 异常处理。

### 1.4.2 调用 Non-secure 软件

带 Security Extension 的 ARMv8-M 架构也允许 Secure 程序调用 Non-secure 软件。此时，Secure 程序使用 BLXNS 指令调用 Non-secure 程序。状态转换期间，返回地址与部分处理器状态会被压入 Secure 栈，同时链接寄存器（LR）中的返回地址被设置为特殊值 FNC_RETURN。被调用函数的地址最低位（LSB）必须为 0。

Non-secure 函数通过跳转到 FNC_RETURN 地址来结束调用；这会自动从 Secure 栈弹出真实返回地址并回到调用方。该状态转换机制会自动隐藏 Secure 软件的返回地址。Secure 软件可在调用前选择性把部分寄存器值作为参数传递到 Non-secure 侧，并清理寄存器组中其余的安全数据。

### 1.4.3 通过异常与中断进行状态转换

状态转换也可以由异常与中断触发。每个中断都可配置为 Secure 或 Non-secure，由 NVIC_ITNS（Interrupt Target Non-secure）寄存器决定，该寄存器仅能在 Secure 世界编程。

对正在执行 Non-secure 或 Secure 代码时能否发生何种状态的中断没有限制。  
若到来的异常/中断与当前处理器状态相同，其异常进入序列几乎与现有 M 系列处理器一致，从而保持低中断延迟。主要差异出现在执行 Secure 代码期间发生 Non-secure 中断时：此时处理器会自动将所有 Secure 信息压入 Secure 栈并清除寄存器组内容，以避免信息泄露。

现有的中断特性（嵌套、向量化处理、向量表重定位等）均受支持。ARMv8-M 的 TrustZone 仍保持 M 系列的一贯低延迟；仅 Secure→Non-secure 中断因需要完整压栈 Secure 上下文而略微增加延迟。

该异常模型的增强也与 FPU 的惰性压栈（lazy stacking）配合：惰性压栈用于在异常序列中避免在不需要时保存浮点寄存器，以降低延迟。在 ARMv8-M 中，同样的思想用于避免保存 Secure 浮点上下文。当 Secure 软件使用了 FPU 而 Non-secure 中断处理程序未使用 FPU 时，将跳过对 FPU 寄存器的压栈/出栈，从而加快中断处理过程。

## 1.5 Test Target 指令

关于不同 Test Target 指令如何查询某一内存位置的安全状态的描述。  
为使软件能够确定某一内存位置的安全属性，使用 Test Target（TT）指令。  
TT 查询某一内存位置的安全状态和访问权限。  
Test Target Unprivileged（TTT）查询对该位置进行非特权访问时的安全状态和访问权限。  
Test Target Alternate Domain（TTA）和 Test Target Alternate Domain Unprivileged（TTAT）查询对该位置进行 Non-secure 访问时的安全状态和访问权限。  
这些指令仅在 Secure 状态下执行时有效；若在 Non-secure 状态下使用则为 UNDEFINED。  
在 Secure 状态下执行时，该指令的结果会扩展，返回该特定地址处 SAU（Security Attribution Unit） 与 IDAU（Implementation Defined Attribution Unit） 的配置信息。  
对于由 SAU 和 IDAU 定义的每个内存区域，都有一个与之关联的区域号，该区域号由 SAU 或 IDAU 生成。软件使用该区域号来确定一段连续内存是否具有共同的安全属性。  
TT 指令从一个地址值返回其安全属性与区域号，以及 MPU 的区域号。通过对某内存范围的起始地址和结束地址各执行一次 TT 指令，并确认二者具有相同的区域号，软件即可快速判断该内存范围（例如一个数据数组或数据结构）是否完全位于 Non-secure 空间。如下图所示：

> ARMv8-M 中的 MPU、SAU 和 IDAU 不允许区域重叠。

使用此机制，Secure 世界中为 API 提供服务的 Secure 代码可以判定由 Non-secure 软件传入的指针所引用的内存，是否具备该 API 所需的适当安全属性。这可防止 Non-secure 软件利用 Secure 软件中的 API 来读出或破坏 Secure 信息。  
作为 ARMv8-M 的 ARM TrustZone 技术的一部分，还提供栈上限检查功能。该功能可检测应用使用的栈超过预期的错误情形，这可能导致安全失效并带来系统故障的可能。对于带有 Main Extension 的 ARMv8-M 架构，所有栈指针都具有对应的栈上限寄存器。Non-secure 侧没有相应的 ARMv8-M 寄存器。Non-secure 程序可以使用 MPU（Memory Protection Unit） 来进行栈溢出防护。

# 第 2 章 安全

本章介绍适用于 ARMv8-M 的 TrustZone 技术的安全特性，并提供不同攻击场景的示例以及 TrustZone for ARMv8-M 如何防止这些攻击的方法。

## 2.1 由 ARM®v8-M 的 TrustZone® 技术所应对的安全需求

在嵌入式系统设计中，“安全”一词可能涵盖多种含义。多数嵌入式系统中的安全包括但不限于：

- **通信保护**  
   防止数据传输被未授权方窥视或拦截，并可能包括诸如密码学等技术。
- **数据保护**  
   防止未授权方访问存储在器件内部的机密数据。
- **固件保护**  
   防止片上固件被逆向工程。
- **运行保护**  
   防止关键操作被恶意地有意破坏。
- **防篡改保护**  
   在许多对安全敏感的产品中，需要防篡改特性以防止器件的运行或防护机制被绕过。

TrustZone 技术可直接应对嵌入式系统的部分安全需求：

- **数据保护**  
   敏感数据可存放于 Secure 内存空间，仅能被 Secure 软件访问。Non-secure 软件只能在通过安全检查或认证后，访问为 Non-secure 域提供服务的 Secure API。
- **固件保护**  
   预加载的固件可存放在 Secure 存储器中，以防被逆向和遭恶意攻击。ARMv8-M 的 TrustZone 技术也可配合其他防护技术使用。例如，器件级读出保护（业界常用技术）可与 ARMv8-M 的 TrustZone 配合，以保护最终产品的完整固件。
- **运行保护**  
   关键操作所需的软件可作为 Secure 固件预加载，相关外设可配置为仅允许 Secure 状态访问。这样即可防止来自 Non-secure 侧的入侵。
- **安全启动（Secure boot）**  
   安全启动机制让你对平台有信心，因为系统将始终从 Secure 存储器启动。

由于 ARMv8-M 的 TrustZone 技术只是安全域之间的屏障，有些安全需求**无法仅凭它**来满足。例如：

- **通信保护** 仍需密码学技术，可由软件实现或由硬件加速器辅助（如 ARM TrustZone CryptoCell 产品）。TrustZone 技术可协助此类技术的应用，例如将某些加密软件与硬件配置为仅在 Secure 状态下可访问。
- **防篡改** 若产品需要，仍需专门的设计技术与产品级方案（如电路板与机壳设计）。是否采用防篡改取决于系统需求与被保护资产的价值。

尽管如此，ARMv8-M 的 TrustZone 技术仍为系统级安全提供了更好的基础。最简单的例子是，可用其保护固件不被逆向，如下图所示：

### 2.1.1 物联网（IoT）产品的安全

面向下一代物联网（IoT）产品的高级微控制器常内建多种安全特性。将 TrustZone 技术与这些附加防护功能结合使用，可使安全特性仅通过**具备有效入口点的 API**被访问，如下图所示。

通过使用 TrustZone 技术来保护这些安全特性，设计者可以：

- 防止未受信任的应用直接访问与安全相关的关键资源。
- 确保对 Flash 映像的重编程仅在**通过认证与检查后**才被允许。

### 2.1.2 无线通信接口的安全

在另一类应用场景（例如集成了已认证无线协议栈的无线 SoC）中，TrustZone 技术可以保护**标准化的通信行为**（如无线通信流程）。借助 TrustZone 技术，可以确保用户自定义应用**无法破坏或使该认证失效**，如下图所示。

## 2.2 攻击类型

在讨论安全系统设计时，安全是一个常见话题。在为 ARMv8-M 开发 TrustZone 技术的过程中，已经考虑了多种攻击场景。这些攻击场景包括：

**软件访问**  
通过额外的系统级组件，可以将存储器划分为 Non-secure 与 Secure 空间，并可阻止 Non-secure 软件访问 Secure 存储器和资源。

**跳转到任意的 Secure 地址位置**  
SG 指令和 Non-secure Callable（NSC）内存属性确保从 Non-secure 到 Secure 的分支仅能发生在有效的入口点。

**二进制数据中意外出现的 SG 指令**  
NSC 内存属性确保只有打算作为入口点使用的 Secure 地址空间才能用于将处理器切换到 Secure 状态。若分支到未标记为 NSC 的地址处，而该处的二进制值恰好与 SG 指令的操作码相同，将导致产生 fault 异常。

**在调用 Secure API 时伪造返回地址**  
当执行 SG 指令时，函数的返回状态被存入链接寄存器（LR）中返回地址的最低位（LSB）。函数返回时，会将该位与返回状态进行检查，以防止从 Non-secure 侧调用的 Secure API 返回到一个伪造的、指向 Secure 地址的返回点。

**尝试使用 FNC_RETURN（函数返回码）切换到 Secure 侧**  
从**不可返回**的 Secure 代码（例如 Secure 引导加载程序）切换到 Non-secure 时，必须使用 **BLXNS** 指令以确保存在有效的返回栈，随后可利用该返回栈进入错误处理程序。  
这可防止恶意的 Non-secure 代码在 **Secure 栈中没有有效返回地址**时，试图通过 **FNC_RETURN** 机制将处理器切回到 Secure 代码并导致 Secure 软件崩溃。  
当从 Secure API 返回到 Non-secure 软件时，本建议不适用，因为此时可以使用 **BXNS** 指令返回。

**伪造 EXC_RETURN（异常返回码）以非法返回到 Secure 状态**  
当在执行 Secure 代码期间发生 Non-secure 中断时，处理器会自动将一个**签名值**加入到 Secure 栈帧中。若 Non-secure 软件试图利用异常返回来**非法切换到 Secure 侧**，则在异常返回时的签名检查会失败，从而检测到该错误。

**企图在 Secure 软件中制造栈溢出**  
在 ARMv8-M 的 Mainline 和 Baseline 子配置中，为 Secure 栈指针实现了**栈上限检查**功能。因此，故障异常处理程序能够检测并处理此类栈溢出。

### 2.2.1 安全需求与体系结构

在调试层面，体系结构同样处理安全需求。

**调试访问管理**  
在处理器上实现了调试认证信号，使设计人员能够分别控制在 Secure 和 Non-secure 状态下是否允许进行调试与追踪操作。  
AMBA 总线接口协议在总线事务中也支持旁带信号（sideband signals），从而使系统可以对传输进行过滤，防止调试器直接访问 Secure 存储器。

**调试与追踪管理**  
可设置调试认证信号，使处理器在 Secure 状态运行时禁用调试与追踪操作。
尽管体系结构已针对多种攻击场景进行设计，Secure 软件仍必须谨慎编写，并应利用安全特性（例如栈上限检查）来防止漏洞。ARM C 语言扩展（ACLE）已针对 ARMv8-M 架构进行了扩展。编写 Secure 软件的开发者应使用这些特性，使其开发工具能够为 ARMv8-M 设备生成代码镜像。

# 第 3 章 归属单元

微控制器或 SoC 设备的设计者将内存空间划分为 **Secure** 与 **Non-secure** 区域。部分区域由软件通过 **Secure Attribution Unit（SAU）** 定义，或由连接到处理器上 **Implementation Defined Attribution Unit（IDAU）** 接口的器件特定控制逻辑来定义。内存分区也用于将外设定义为 Secure 或 Non-secure。

## 3.1 SAU 与 IDAU

如果处理器包含 ARMv8-M 的 Security Extension，则由内部的 **SAU**（Secure Attribution Unit）或外部的 **IDAU**（Implementation Defined Attribution Unit）来确定每个地址所归属的安全状态。

SAU 的区域数量在处理器实现时确定。复位时 SAU 处于禁用状态。

只有在处理器包含 ARMv8-M Security Extension 时才实现 SAU。SAU 所包含的区域数量可配置为 **0、4 或 8**。

如果未定义任何 SAU 区域，或 SAU 被禁用，且系统中未包含 IDAU，则**整个内存地址空间均为 Secure**，处理器**无法切换到 Non-secure 状态**。任何试图切换到 Non-secure 状态的行为都会导致 **fault**。

SAU **只能在 Secure 状态下**编程。区域通过 **SAU_RNR**（SAU 区域号寄存器）、**SAU_RBAR**（SAU 区域基地址寄存器）和 **SAU_RLAR**（SAU 区域上限地址寄存器）进行配置。可通过 **SAU_CTRL**（SAU 控制寄存器）使能 SAU。

> 在对 SAU 中的 Non-secure 区域进行编程时，必须确保不会将 Secure 数据和代码暴露给 Non-secure 应用。

处理器中的安全归属与内存保护由可选的 **SAU** 与可选的 **MPU**（Memory Protection Unit）提供。

对于**指令**与**数据**访问，SAU 会返回与该地址关联的**安全属性**。  
对于**指令**，该属性决定指令执行时处理器允许的安全状态，并可指示位于 Secure 地址的代码是否可被 Non-secure 状态调用（通过应用 **NSC** 属性进行检查）。  
对于**数据**，该属性决定某个内存地址是否可从 Non-secure 世界访问，以及相应的外部存储器请求应标记为 Secure 还是 Non-secure。

如果在 **Non-secure** 世界对标记为 **Secure** 的地址进行数据访问，则处理器会触发 **Secure Fault** 异常。若在 **Secure** 世界对标记为 **Non-secure** 的地址进行数据访问，则相应的外部存储器访问会被标记为 **Non-secure**。

### 3.2.1 SAU 区域配置

当启用 SAU 时，未被启用的 SAU 区域覆盖到的内存默认为 **Secure**。

- 各区域通过 **SAU_RLAR** 单独启用。
- 当 **SAU_RLAR.ENABLE = 1** 且 **SAU_RLAR.NSC = 0** 时，该区域为 **Non-secure**。
- 当 **SAU_RLAR.ENABLE = 1** 且 **SAU_RLAR.NSC = 1** 时，该区域为 **Secure 且 Non-secure callable（NSC）**。

## 3.3 IDAU 接口、IDAU 与内存映射

IDAU 用于指示处理器某个内存地址是 Secure、Non-secure Callable（NSC）还是 Non-secure，并提供该地址所在的**区域号**。它也可以将某个内存区域标记为**免安全检查**（例如 ROM 表）。

IDAU 接口通常是**处理器相关**的；不过，不同 Cortex-M 处理器上的 IDAU 接口**高度相似**。

理论上可以把 IDAU 设计成可编程的。但 IDAU 接口上的信号往往处在**时序关键路径**，使复杂的 IDAU 不切实际且会增加门数。因此，IDAU 通常仅提供**简单的内存映射**，可配置性有限。

### 3.3.1 内存映射示例

ARMv8-M 将内存映射按 **512 MB** 边界划分。该示例通过在每个 512 MB 边界的**中点做别名**来加入安全支持：**下半部分**提供对同一 256 MB 区域的 **Non-secure 窗口**访问，**上半部分**提供对同一 256 MB 区域的 **Secure 视图**。

系统中其他控制点决定在各自的 Secure 与 Non-secure 窗口中**可访问的内容**。

设计者可以使用地址的 **bit[28]** 来区分某段内存是 Secure 还是 Non-secure，由此得到如下的内存映射示例。


> 同时用位 [28] 进行别名映射并区分 Secure 与 Non-secure **仅是示例**，**不得**由软件使用。

该 IDAU 可通过以下方式生成所需信号：

- 可使用地址位 [28] 生成 Secure/Non-secure 指示。
- Secure Non-secure Callable（NSC） 指示可复用 Secure 指示。这样会导致所有 Secure 区域与 Secure NSC 区域不可区分，因而默认可被 Non-secure 软件调用。在允许任何 Non-secure 软件运行之前，Secure 软件必须使用内部的 SAU 将大多数 Secure NSC 区域强制为 Secure 区域（非 NSC）。

必须确保只有包含有效 Secure 入口函数（使用 SG 指令）的内存区域被配置为 NSC。其他 Secure 内存（例如栈）可能包含与 SG 指令匹配的数据模式，因此不得配置为 NSC 区域。

区域号可由地址位 [31:28] 生成，并将 Region Valid 信号拉高。除非通过 IDAU 接口指示该内存区域号无效，否则各内存区域的区域号必须唯一。

若地址位于 CoreSight ROM 表地址范围内，则将 Exempted Region 控制位置 1，从而即使调试器被限制为 Non-secure 调试，也允许其访问用于设备识别的 ROM 表。

对于每个内存区域，Secure 内存在上半区还是下半区并无限制。如果所用处理器的初始启动地址被限制为 `0x00000000`，则更好将地址的下半区标记为 Secure，以便处理器在 Secure 状态下启动。

在将 ARMv8-M 处理器与 ARMv8-A 系统共同使用、且共享内存安全属性配置的应用场景中，应基于系统范围的安全安排来生成 IDAU 响应信号。此处示例所述的简单内存映射安排并不足够。

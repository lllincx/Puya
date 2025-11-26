ARM® TrustZone® 技术是一种可选的安全扩展，旨在为各种嵌入式应用提供更高系统安全性的基础。

**安全世界与非安全世界**
TrustZone 技术使系统与软件可以被划分为安全（Secure）与非安全（Non-secure）两个世界。安全世界的软件可以访问安全与非安全的存储与资源；非安全世界的软件只能访问非安全的存储与资源

**安全状态与线程模式和处理模式的关系**
该安全状态与现有的 Thread 模式和 Handler 模式是正交关系，因此在安全与非安全状态下都可以运行 Thread 与 Handler 模式。

**应放置在安全世界的系统安全组件清单**

- 安全引导加载程序（Secure boot loader）
- 密钥（Secret keys）
- Flash 编程支持（Flash programming support）
- 高价值资产（High value assets）

**安全与非安全世界切换**
安全与非安全软件可以协同工作，但非安全软件不能直接访问安全资源。必须通过由安全软件提供的 API，并由这些 API 执行身份/权限校验以决定是否允许访问。

TrustZone 在 Arm Cortex-A 处理器上已使用多年，如今扩展到 Armv8-M 处理器。
Arm Cortex-A：只能通过监视器模式完成状态切换
Arm Cortex-M：在异常处理代码中自动完成状态切换

**Cortex-M 与 Cortex-A 处理器 TrustZone 方案的关系**
相对于 Cortex-A 的 TrustZone 方案，Cortex-M 方案采用自底向上重新设计，底层运行机制不同。
Cortex-M 方案针对微控制器和低功耗 SoC 应用进行了优化。低功耗、低内存占用和低延迟是关键因素。
Cortex-M 方案的安全与非安全世界的划分主要基于内存映射
Cortex-M 方案支持多个安全函数入口点；而在 Cortex-A 的 TrustZone 中，Secure Monitor 处理程序是唯一入口。
Cortex-M 方案允许安全与非安全状态共享寄存器组
状态切换开销低，便于 Secure 与 Non-secure 软件频繁交互（当安全固件含 GUI 库或通信协议栈等软件库时尤为常见）。

**安全平台的安全性要求**
要确保平台安全，安全设计不能只停留在处理器架构层面，而必须在整个系统层级做增强以满足安全需求。要求包括：

- 总线协议需扩展以支持安全属性。
- 需要额外的系统组件来管理安全，例如外设管理访问权限。
- 调试架构必须具备安全感知能力，防止通过调试口或追踪功能接触到机密信息。
- 运行在安全世界的软件必须谨慎编写，避免引入漏洞。

**嵌入式系统的安全需求**

- 通信保护（Communication protection）  
   该保护防止数据传输被未授权方看到或拦截，通常还包括密码学等技术。
- 数据保护（Data protection）  
   该保护防止未授权方访问存储在设备内部的机密数据。
- 固件保护（Firmware protection）  
   该保护防止片上固件被逆向工程。
- 运行保护（Operation protection）  
   该保护防止关键操作被恶意地故意破坏。
- 防篡改（Tamper protection）  
   在许多对安全敏感的产品中，需要防篡改特性，以防止设备的运行或保护机制被绕过。

**存储系统及其划分**
NSC 是一种特殊的安全存储区域，处理器仅允许此区域放置 SG（Security Gate）指令，用于使软件从非安全状态切换到安全状态。NSC 通常只存放简明中转代码。
引入 NSC 是为了防止其他二进制数据（例如查找表）因为其值恰好与 SG 指令的操作码相同而被当作进入 Secure 状态的入口函数。

**归属单元（Attribution units，AU）**
- SAU（Secure Attribution Unit，安全归属单元）：内部可编程模块
- IDAU（Implementation Defined Attribution Unit，实现定义归属单元）：外部固定逻辑模块


IDAU 通常由 SoC 或 MCU 设计者在外部逻辑中实现，用来定义固定的内存安全映射
SAU 是可编程的，只能在 Secure 状态下配置，可以灵活配置NS，S，HSC。SAU 默认在复位后 禁用
例如IDAU 可能定义“500MB Secure + 500MB Non-secure”交错区间，而 SAU 再对其中的某些页做细分修改。


**状态切换指令**
SG（Secure Gateway）：从非安全切换到安全
BXNS（Branch with exchange to Non-secure state）：切换到非安全状态并跳转执行
BLXNS（Branch with link and exchange to Non-secure state）：调用非安全函数并切换到非安全状态执行

**非安全程序调用安全程序**
当且仅当入口点的第一条指令为 **SG**，且该入口位于 **NSC（Non-secure Callable）** 内存位置时，允许 Non-secure 直接调用 Secure API。
当 Non-secure 程序调用 Secure API 完成后，会通过 **BXNS** 返回到 Non-secure 状态。

**安全程序调用非安全程序**
Secure 程序使用 BLXNS 指令调用 Non-secure 程序。状态转换期间，返回地址与部分处理器状态会被压入 Secure 栈，同时链接寄存器（LR）中的返回地址被设置为特殊值 FNC_RETURN。
Non-secure 函数通过跳转到 FNC_RETURN 地址来结束调用；这会自动从 Secure 栈弹出真实返回地址并回到调用方。该状态转换机制会自动隐藏 Secure 软件的返回地址。Secure 软件可在调用前选择性把部分寄存器值作为参数传递到 Non-secure 侧，并清理寄存器组中其余的安全数据。


**通过异常与中断进行状态转换**
在执行 Secure 代码期间发生 Non-secure 中断时：此时处理器会自动将所有 Secure 信息压入 Secure 栈并清除寄存器组内容，以避免信息泄露。
为保证低中断延时，其他情况下，TrustZone架构下的异常、中断处理与非TrustZone架构一致。


Test Target 指令
查询某一内存位置的安全状态，访问权限，与区域编号（同一区域编号的地址安全状态相同）。
通过对某一内存范围（例如数据数组或数据结构）的起始地址与结束地址分别执行 TT，并确认二者属于同一区域编号，软件即可快速判断该内存范围是否完全位于 Non-secure 空间。


# 8 面向不同攻击场景的 Armv8-M TrustZone 安全性

TrustZone 技术可避免的攻击场景

**软件访问**  
通过系统级的安全组件，可将存储器划分为 Secure 与 Non-secure 区域，并禁止 Non-secure 软件访问 Secure 存储器与资源。

**跳转到任意 Secure 地址**  
`SG` 指令与 NSC 内存属性确保：从 Non-secure 代码跳转到 Secure 代码时，只有合法的入口点才能被使用。

**二进制数据中误含 SG 指令**  
NSC 属性保证只有那些被明确标识为入口点的 Secure 地址才能用于状态切换。  
若程序跳转到一个未标记为 NSC 的地址，而该地址的二进制数据恰好与 `SG` 指令编码相同，处理器会触发 Fault 异常。

**伪造返回地址调用 Secure API**  
当执行 `SG` 指令时，函数返回状态会被记录在链接寄存器（LR）返回地址的最低位（LSB）。  
在函数返回时，硬件会校验该位与实际返回状态是否一致，以防止 Secure API 被 Non-secure 侧伪造返回地址并跳回到 Secure 区域。

**利用 FNC_RETURN 伪造切换到 Secure 侧**  
当从不可返回的 Secure 代码（如 Secure Bootloader）切换到 Non-secure 代码时，必须使用 `BLXNS` 指令以确保存在有效的返回栈，从而在需要时能进入错误处理程序。  
此机制防止恶意 Non-secure 代码利用 FNC_RETURN 强行切换到 Secure 区而导致崩溃。  
此建议不适用于从 Secure API 返回到 Non-secure 的情形，此类返回应使用 `BXNS` 指令。

**伪造 EXC_RETURN 以非法返回 Secure 状态**  
当在 Secure 代码执行期间触发 Non-secure 中断时，处理器会在 Secure 栈帧中自动加入签名值。  
若 Non-secure 软件试图伪造异常返回以切入 Secure 状态，异常返回时的签名校验会失败，从而检测并阻止该攻击。

**制造 Secure 侧栈溢出**  
在 Armv8-M Mainline 与 Baseline 架构中，Secure 栈指针都具有栈上限（stack limit）机制。  
因此，一旦发生溢出，Fault 异常处理程序会立即检测并处理。

**调试访问安全管理**  
处理器实现了调试认证信号（debug authentication signals），可让系统设计者分别控制 Secure 与 Non-secure 状态下是否允许调试与追踪操作。  
AMBA 总线协议还提供旁带信号（sideband signals），以便系统在总线层过滤传输，防止调试器直接访问 Secure 存储器。

**调试与跟踪控制**  
可通过配置调试认证信号，使处理器在运行于 Secure 状态时禁用调试与跟踪功能。


使用地址位[28]作为安全非安全区分位，如果所用处理器的初始启动地址被限制为 0x00000000，则更适合将地址下半部分标记为 Secure，以便处理器能够在 Secure 状态下启动。
区域编号可由地址值的位 [31:28] 生成，并将Region_Vaild信号置位。（所有有效的区域需要有唯一的编号）
当地址位于 CoreSight ROM 表的地址范围时，将 Exempted Region 控制位置 1，使调试器即使仅限于 Non-secure 调试，也能访问 ROM 表以进行器件识别。




### 基于水印的安全区域

水印 (Watermark) 机制通过在选项字节 (Option Bytes) 中配置一个地址阈值，将 Flash 物理划分为低地址的安全区和高地址的非安全区。

### 易失与非易失

“易失/非易失”特指 “安全属性配置” (Security Attribute Configuration) 的生存周期，而非 \*\*“存储介质” 本身。

- 存储介质（Flash）：永远是 非易失 的。无论配置如何，里面的数据掉电都不丢。
- 安全属性（配置）：
  - Option Bytes 定义 = 非易失属性（掉电后，该页“是安全页”这个身份保留）。
  - Registers 定义 = 易失属性（复位后，该页“是安全页”这个身份丢失，变回默认）。

### 安全隐藏保护（Secure Hide Protection，HDP）

在一个 系统复位周期 (System Reset Cycle)内，只执行一次后，就不能被访问或执行。

### 系统启动流程

#### TrustZone 禁用

- 正常启动：Reset $\rightarrow$ 用户程序。
- 系统启动：Reset $\rightarrow$ Bootloader (位于只读系统 Flash)。

#### TrustZone 启用

1. RSS (位于只读系统 Flash，非易失配置，HDP 保护)。
2. Secure Bootloader (位于用户 Flash 的基于水印的安全区，非易失配置，HDP 保护)。
3. Runtime 阶段 (位于用户 Flash 的以下区域，易失配置，无 HDP 保护)：

   - 基于水印的安全区
   - 安全页
   - 非安全页
4. Bootloader-NS (位于只读系统 Flash）被忽略

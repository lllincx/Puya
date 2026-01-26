# SMC

SMC 是一种符合高级微控制器总线架构（AMBA）的系统级芯片（SoC）外设。该产品系列包括高性能、
面积优化的 SRAM 和 NAND 存储器控制器，其片上总线接口符合 AMBA 高级可扩展接口（AXI）协议。
SMC 支持 NAND 和 SRAM 类型的内存接口。
NAND 存储器接口类型定义为支持带复用地址/数据（A/D）总线的 NAND 闪存。
SRAM 存储器接口类型定义为支持：
 异步 SRAM
 NOR 闪存
 带 SRAM 接口的 NAND 闪存设备。
SMC 的主要特性有：
 支持 8 位和 16 位存储器数据宽度
 支持 32 位 AXI 总线宽度。
 支持突发模式。
 最多支持四个芯片选择信号。
 为每个存储器组提供独立的配置
 可选的 2 位检测、1 位纠错错误校正码 (ECC)块，适用于单级单元 (SLC) NAND 存储器。
 可编程地址周期和命令值，用于 NAND 闪存访问，支持与各种 NAND 设备配合使用。
 支持多个时钟域，并可配置为异步模式
 8 x32bit 深度的读、写、命令 FIFO。

# SE

Security Engine 作为系统安全组件，通过内部加密引擎实现高性能、低功耗的加解密操作。支持的加解密方案如下：
 对称方案： AES-ECB/CBC/CTR/CBC-MAC/CMAC/CCM/GCM (密钥尺寸：128-bit, 192-bit 和 256-bit).SM4-ECB/CBC/CTR/CBC-MAC/CMAC/CCM/GCM.（CFB/OFB/XTS）
 摘要方案：SHA1/224/256，SM3.
 非对称方案：RSA 1024/2048/3072/4096 和 ECCP 192/224/256/384/512/521 以及 SM2.
Security Engine 为了减少软件在安全方面的复杂性，增强系统安全性，提供高安全保证，还具备以下功能：
 密钥阶梯（key ladder)管理
 生命周期（LCS）管理
 一次性可编程（OTP）访问控制
 真随机数生成（TRNG）
Security Engine 支持多主机。
 加解密引擎支持 0~2 个安全主机，0~1 个非安全主机。多个主机共享同一个加速器引擎内核，支持配置仲裁算法与粒度。
 真随机数生成器支持 0~2 个安全主机，0~1 个非安全主机。多个主机共享同一个真随机数生成内核。
Security Engine 适配 ARM TrustZone。

# DMA-350

- 可编程的 APB4 配置寄存器接口
- AXI5 数据通路，可配置为 1 或 2 个
- 用于时钟和电源管理的低功耗接口 (LPI, Q-Channel/P-Channel)
- 1 到 8 个并行 DMA 通道，每个通道带有可配置的 FIFO
- 包含地址自增功能的 1D 内存拷贝
- 支持每个通道的中断以及全局事件中断
- 灵活的命令链接 (Command linking) 能力
- 用于流控 (Flow control) 的触发能力
- 扩展的内存拷贝能力：2D / 回绕 (wrap) / 模板 (template) 模式
- 扩展接口 (Expansion interface)
- 支持通道标识（ID)寄存器，位宽可配。
- 支持通道通用输出（GPO)寄存器，位宽可配。
- 支持通道的流 (Stream) 接口
- 支持安全属性（TrustZone）与特权功能。

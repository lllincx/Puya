ARM专家：

您好

图中显示。16个不具备安全感知功能的外设在发生安全违例后，中断信号会被汇集到peripheral protection controller中，仅输出一个irq信号。

请问是否有参考设计，或者其他客户的方案可以实现，输出每个外设的irq信号。图片以STM32U5为例，每个外设均有安全中断

---

Dear ARM Expert,

Hello.

As shown in the diagram, when a security violation occurs on the 16 peripherals that lack security-aware capability, their interrupt signals are aggregated into the Peripheral Protection Controller (PPC), which outputs only a single IRQ signal.

Could you advise whether there is a reference design, or an implementation from other customers, that allows the IRQ signal of each individual peripheral to be exposed separately? For reference, the attached diagram uses STM32U5 as an example, in which every peripheral has its own secure interrupt.

Best regards,
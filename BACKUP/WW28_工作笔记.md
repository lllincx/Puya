# WW28 周报

#### DBG SMC

1. 地址 msk 与 mtch 值错配问题，修改 syscfg 配置初始值。
2. 发现并解决时序违例问题，vivado 将 clk3 配置为 30。
3. syscfg16 问题，软件部门 C 程序问题。
4. D1 位始终为低，A12 位同样占用了 PG1。

#### TrustEngine TRNG

1. Trng case 优化完成，去除冗余的遍历熵源功能，重构循环读为中断访问。
![|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250710105304423.png)

2. 参考波形看 trng 代码。

#### TrustEngine OTP

支持外包同事完FPGA测试

#### 试用期进度

1. 完成考核期绩效目标设定并通过审核
2. 完成试用期自评


# 7月7日 星期一


1. 修正【修改地址 msk 与 mtch 值错配问题，并设置为 syscfg 配置】导致的问题，并上传

| 名称         | 1   | 2   | 3   |
| ---------- | --- | --- | --- |
| cs0if0msk  | ff  | 7c  | fc  |
| cs0if0mtch | 70  | 70  | 70  |
| cs1if0msh  | ff  | ff  | ff  |
| cs1if0mtch | 74  | 78  | 74  |
| cs0if1msk  | ff  | 7c  | fc  |
| cs0if1mtch | 78  | 74  | 78  |
| cs1if1msh  | ff  | ff  | ff  |
| cs1if1mtch | 7f  | 7f  | 7f  |

2. 发现并解决smc 时序违例问题：clk3->30
3. 跑SMC新网表，仍存在问题，awsize初始值为2，不符合预期，重新出网表。


# 7月8日 星期二


[[考核期的绩效目标设定]]

smc syscfg16 问题解决: 软件部门C程序问题

trng case 优化
trng 看波形代码

# 7月9日 星期三


**DBG SMC D1恒为零问题**
**DBG address msk 初始值错误**

| 名称         | 1   | 2   | 3   | 4   |
| ---------- | --- | --- | --- | --- |
| cs0if0msk  | ff  | 7c  | fc  | fc  |
| cs0if0mtch | 70  | 70  | 70  | 70  |
| cs1if0msh  | ff  | ff  | ff  | fc  |
| cs1if0mtch | 74  | 78  | 74  | 74  |
| cs0if1msk  | ff  | 7c  | fc  | ff  |
| cs0if1mtch | 78  | 74  | 78  | 78  |
| cs1if1msh  | ff  | ff  | ff  | ff  |
| cs1if1mtch | 7f  | 7f  | 7f  | 7f  |
**trng case 优化测试**

**试用期自评**

展现扎实的设计实现能力，代码结构清晰高效；验证环节自主完成环境配置与用例迭代，快速定位技术问题；准确理解综合/STA报告关键结论；文档逻辑严谨可直接应用于后续开发。

可靠完成模块级设计任务，代码功能完备并通过基础验证；独立执行标准测试用例，有效覆盖核心场景并厘清问题根源；准确理解综合/STA报告关键结论；文档完整呈现技术要点。

在TrustEngine/SMC模块实现验证案例零差错移植，主动优化4项测试场景覆盖率；独立修复代码问题并验证功能符合预期；为FPGA团队提供可直接部署的网表及协议解析指南；整理Flash接口关键参数文档；跨部门协作中提出有效流程改进建议。

# 7月10日 星期四


trng case 优化完成
![|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250710105304423.png)

fpga otp 测试支持

SMC busy位有问题，确认IO属性无误
SMC D1位问题解决，ADDR12位同样占用了PG1

# 7月11日 星期五


学习TrustEngine TRNG
![[TrustEngine Process#trng]]

DBG smc nor busy 信号无反馈，HIO47高阻


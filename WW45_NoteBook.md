
- TrustEngine->Security Engine
- 协助魏凯，fsmc pinmux确认
- 确认pinmux修改未引入smc相关case fail
- 日常提取迭代新网表的无复位值寄存器列表等
- fmc相关的违例分析

- TrustZone硬件系统设计关键点：
1. 系统总线(必需)
	1. AXI总线根据ARPORT[1]，AWPORT[1]表示安全主机与否
	2. APB，AHB总线不具备定义安全安全位，需要AXI-APB，AXI-AHB，AHB-AXI内完成安全属性管理
2. 缓存（可选）
	1. 安全与非安全的数据在换成中需要隔离
	2. 如果在安全状态下需要使用二级缓存，需要支持TrustZone 的二级缓存控制器IP
	3. 对于适配TrustZone的处理器，内部的TCM与L1有相应的隔离逻辑
3. DMA(可选)
	1. 安全主机可不使用DMA功能
4. 存储器
	1. 可以把同一片存储器分为安全区和非安全区
	2. 不使用该适配器可以为安全区单独划分存储器
5. 外设
	1. 分为安全外设非安全外设
6. 中断（必需）
	1. 阻止 Normal world 修改 Secure 中断源的配置
	2. 中断设计需要具体权衡
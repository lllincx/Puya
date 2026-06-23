#### 规格定义

- 查看是否有 IP 缺失，参考 addr map
- 参考四五款竞品做法：
  - sec attr 与 priv attr 访问权限的条件关系
		- ST
			- sec attr reg wr permission：sec & (priv attr def)
			- priv attr reg wr permission：priv & (sec attr def)
		- 瑞萨
			- sec attr reg wr permission：sec & priv
			- priv attr reg wr permission：priv & (sec attr def)
  - resp 连接的静态值（ST 为 0）
#### 设计参考

- 参考 corestone 320 ppc mpc msc 的intrClr，intr，resp，sec，ap连法
#### 设计变更

- 增加外设 sec resp ctrl reg & output，permit：sec&priv
- IFC reg 需要连到 output
- sec attr 与 priv attr 访问权限更正，参考u5
- ==待定：intr clr cdc 问题==

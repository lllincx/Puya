#rep 

TrustEngine 大多数 case 在交接前已移植完毕并支持 SelfCheck。现汇报此前遗留子模块问题：

# 多存储器类型

会议上，时擎称 smc 类型无法支持，目前 case 中已完成接口。
dmc，需要等待验证方面写好 dmc_init 函数，目前 case 中已完成接口。

|      | sram | psram | smc | dmc | tcm |
| ---- | ---- | ----- | --- | --- | --- |
| 时擎通过 | 1    | 1     | 0   | 1   | 1   |
| 完成移植 | 1    | 1     | 0   | 0   | 1   |
| 移植通过 | 1    | 1     | 0   | 0   | 1   |

# TRNG

时擎 case 已验证通过
需要在仿真阶段配置的 TRNG 内容已经更新
![Pasted image 20250617150133](https://pic.lllincx.cn/Pasted%20image%2020250617150133.png)
移植完成，仿真通过
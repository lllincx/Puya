# WW25 周报

## 时擎交接

仿真 TRNG，MultiMem 遗留 case 通过
汇报总结 TrustEngine IP 交接情况

## TrustEngine FPGA 仿真

完成大多数 case
DBG

## TrustEngine Case 移植

移植 TRNG、MultiMem case 并仿真通过
在设计代码中添加需要在仿真阶段配置的 TRNG 内容
解决因 sram 连线错误导致 bug
解决中断 bug

## TrustEngine 软件应用学习

学习安全启动等功能
参与软件会议

## 支持软件与 FPGA 同事

- otp 相关 case 讲解
- TrustEngine 密钥相关疑问解答
- eMemory 为什么没有支持
- 协调 FOTA 功能依赖用户定义空间问题

## SMC

学习 SPEC,跑 case 看波形


# 6月16日 星期一

## 时擎交接

### TRNG

在外包平台跑 TRNG 通过

### Multi-Mem

在外包平台跑多存储器种类通过，其中 SMC 不通过（与会议上介绍的一致）

### FPGA-Sim

大部分 FPGA 仿真完成，例外：
- aca_cg 卡在 run，asic 没有出现
- trng 目前还未移植

![[FPGA Sim]]

## Multi-Mem 移植

框架完成，与各类型mem接口写好，等待mem函数移植适配
TMC，SRAM，Psram验证通过

## 解决SRAM连线错误导致BUG

# 6月17日 星期二


[[TrustEngine 时擎交接情况]]

## TRNG

- 交接时擎case
- 修改.V代码，宏定义验证阶段配置
- 移植并asic仿真通过

## MultiMem

### Psram

- 交接时擎case
- 移植并asic仿真通过

# 6月18日 星期三

## Case DBG

- 解决 ACA case FPGA sim bug

## SPEC 学习

- Security Boot 文档阅读

## 会议

### 工作安排：负责 SMC

### 软件会议

> with 隔空

- otp相关case讲解
- 软件spec介绍（包含安全启动）
- TrustEngine密钥相关疑问解答
- eMemory为什么没有支持
- FOTA功能依赖用户定义空间，需要考虑是否支持

# 6月19日 星期四


## Case DBG

- fix scs intr bug (with chkpt version)
  ![image.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250619150848449.png)

## SMC支持

- SPEC学习
- 跑smc case，结合波形看

## 会议

- 撰写前一天会议的问题解答
  [[6月18日 星期三 会议问题解答]]
- 询问 ememory 问题
- 跟踪用户定义空间问题

## smc DBG(未完成)

> SMC  有个确定的问题，syscfg.bit16 未生效 SMC 波形错误。 FPGA 仿真确认一下

宇波称，fpga 问题，仿真无法体现失误
debug 优先级低，优先结合 case 看波形

## otp问题提utracker

# 6月20日 星期五


## SMC 学习

- case 中读命令与波形不对应
- cach 访问
- 需要等待 case 更新（低优先级）
- 看 smc 波形可以看 model 接口



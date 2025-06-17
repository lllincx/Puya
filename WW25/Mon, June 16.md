# 时擎交接

## TRNG

在外包平台跑 TRNG 通过

## Multi-Mem

在外包平台跑多存储器种类通过，其中 SMC 不通过（与会议上介绍的一致）

![[Multi-Mem]]

# FPGA-Sim

大部分 FPGA 仿真完成，例外：
aca_cg 卡在 run，asic 没有出现
trng 目前还未移植

![[FPGA Sim]]

# Multi-Mem 移植

框架完成，与各类型mem接口写好，等待mem函数移植适配
TMC，SRAM验证通过
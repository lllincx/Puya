# 10.13 Mon

- DBG TrustEngine Gsim fail, ask for help, suspending.
- lint rpt for te/smc
- dev sdc for te/smc

# 10.14 Tue

- opt sdc for te/smc
- cdc chk for te/smc
- make review slide fot te/smc
- review te/smc
- TrustEngine Gsim fail: maybe unreset reg cause

# 10.15 Wed

review meeting to-do. [[WW42_TrustEngine&SMC_review RPT]]
SMC top tie-off. [[WW42_SMC_TOP tie-off RPT]]
TrustEngine testcase desp.

# 10.16 Thu

## TrustEngine

Testcase desp. [[WW42_TrustEngine_case desp.]]
DBG gsim fail: get unreset reg

## SMC

Review SMC top tie-off.

`pt_shell:restore_session asic_top`

Support CAI: rd ecc value while ecc mode = 01.

# 10.17 Fri

Opt get unrest reg

### `nand_csl`

No impact on compat across NAND types.  
`nand_csl=1` better perf for single-die excl.  
`nand_csl=0` supports multi-die interlv.

# Weekly Report

## IP 评审

开发 sdc，撰写 Lint、CDC 报告，编写评审 PPT，并在会上通过 review。
编写会议记录，并根据会上意见完善任务。

## TrustEngine

DBG 后仿 fail 问题，有寄存器无复位值导致。开发脚本从 pt 抓取全部无复位值寄存器提交验证。迭代脚本抓取全部无复位值寄存器 QN[x]，Q[x]引脚便于验证同事使用
编写全部 testcase 描述并列入验证表格

## SMC

编写顶层 Tie-off 情况报告并 review
支持蔡紫阳 ecc mode 为 01 时 ecc 使用方式

# To-do

DEFMA
add sram.db to filelist

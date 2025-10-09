# 9.22 Mon

- update SPEC REG Chapter by script
- Try to make case for ttr & tpc

# 9.23 Tue

- Run burst hex sim for Dev nor burst case
- Add useful  case to table.

# 9.24 Wed

- Join meeting about GSIM 
- Run burst hex sim to confirm timing para effect. [[WW39_Hex Sim Rpt for diff tpc]]
- Dev nor burst case: nor model don't support burst operation
- Opt SPEC. [[WW39_SMC_Mem Blk]]
# 9.25 Thu

- Join SPEC review, note revision comments.

# 9.26 Fri

- [[WW39_SMC_Nor MUX]]
- Opt TrustEngine SPEC
# Weekly Report

### 主要工作总结

- 将此前开发的有效case，补充进验证回归列表
- 参与验证GSIM会议
- 完善SPEC，参与SPEC核对会议，按照会议要求完善SPEC

#### SMC

- 解答蔡紫阳关于nor、nand时序参数的疑问
	- nor：tr，tpc 的含义
	- nand：tclr，tar，trea中SMC和器件SPEC描述不符合
- 构建case证实tpc的实际作用
- 构建突发读写case：终止，现有nor不支持突发读写
- 编写文档，讲解nor mux的意义并提交

### 项目状态

TrustEngine SPEC：除寄存器需重新生成，其他已完成。
SMC SPEC：待完善。
Verify: Add case Desp. into table
Verify: Check coverage for integration (e.g., DMA, interrupts); note cases not tested in sim/FPGA.

### 补充说明材料

[[WW39_SMC_Mem timing para confusion]]
[[WW39_SMC_Nor MUX]]
# To-do

- Verify: Add case Desp. into table
- Verify: Check coverage for integration (e.g., DMA, interrupts); note cases not tested in sim/FPGA.
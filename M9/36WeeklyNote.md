## Work Conclusion

### DMAX

- support AE理解传输速度与burst长度关系
  - 在fpga中加debug信号出bitfile：测试复杂度高于HEX仿真放弃
  - 改写IOMUX的IP debug 信号出bitfile：测试复杂度高于HEX仿真放弃
  - hex仿真：并非最大burst长度传输速度最快，这一现象具有普遍性

### TZC

- 沟通debug信号高位被截断问题

### PVTC

- debug DPD混仿问题
  - 对比前后仿波形，发现原因是后仿无视大小写，要求后端重新出PR网表
  - 混仿通过
- debug DTS混仿问题
	- case写法debug
	- DTS_EN取反
		- 分别独立修改RTL，综合网表，后仿网表并进行fm检查
	- 混仿通过
- 验证ANA输出SDO正确性
  - 验证通过
  - 发布脚本
- 出具遍历各种条件的vcd
  - 咨询VV批量出case跑波形的方式并调试

### Other

- 各IP的spyglass检查
- 准备IP评审文档

---

# Project Progess

### Highlight

- pvtc混仿跑通，开始批量出各种条件的vcd

### Lowlight

- dmax出debug信号流程没跑好，最终通过hex仿真解决

### Help Needed


- 

### Next Plan


- pvtc user manual

- pvtc spyglass检查

- 准备IP评审文档

	

	

	


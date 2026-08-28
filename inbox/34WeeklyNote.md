## Work Conclusion

### TE

- 参与armchina软件培训会议

### DMAX

- debug AE反馈问题
	- 跑hex仿真
	- 速度不随burst配置变化问题：AE理解有误，可配的是maxburst，未跑到maxburst成为瓶颈的情形
	- 速度不随位宽配置变化问题：推断合理，只是与PT105情况不一致。位宽并非传输瓶颈，可能由其他原因决定（如FIFO深度），待hex仿真确认

### PVTC

#### feature

- 根据模拟要求，更新model
- 修正电压define问题
- 解决ip_faultn bug
- 添加dpd_ipcfga

#### syn

- 迭代网表与sdc

#### jtag

- 学习测试特性
	- 在IP环境跑通测试相关tc
- support AE 开发测试tc

#### other

- 根据ANA要求，编写tc，提供vcd，有效性待反馈
- 填写数模接口表格
- 参与会议

### Other

- 填写风险评估表

---

# Project Progess

### Highlight

- dmax速度不随burst配置变化问题：AE理解有误，可配的是maxburst，未跑到maxburst成为瓶颈的情形
- pvtc综合迭代
- pvtc根据ANA要求，编写tc，提供vcd，有效性待反馈

### Lowlight

- 

### Help Needed


- 

### Next Plan


- 跑hex确认，dmax速度不随位宽配置变化问题

	

	

	



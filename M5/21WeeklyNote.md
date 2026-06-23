# **工作总结**

### TrustEngine

- conncet to fmc
- clk en default 1
- update intergration manul: add cfg table

### DMAX

- TCM modify, axi map change, regen
- cofirm fifo depth
- update intergration manul: add cfg table
- support VV team
- present at Vplan meeting
- 查看halt用法：CTI，查看cs320 halt接口接法，咨询ARM cs320 DMAX接口问题
- 与思雨沟通CTI问题，在mcu dbg那边处理后接入dmax

###   TZC

- 根据规格变更移除npu主机配置
- fix priv issue

### 其他

- support mcu debug
- support AE：reg table

### SMC

- debug pcd100：awlen应为 0x0，已反馈VV提交郭老师处理
- debug pt105: AE 反馈nand ecc在通过写命令方式读取rydy状态时出现问题，轮询和中断方式都没问题

---

# **项目状态**

### Highlight

- debug pcd100：awlen应为 0x0，已反馈VV提交郭老师处理

### Lowlight


- 推送的dmax更新commit存在bug，随后解决

### Help Needed


- debug pcd100：awlen应为 0x0，已反馈VV提交郭老师处理
- debug pt105: AE 反馈nand ecc在通过写命令方式读取rydy状态时出现问题，轮询和中断方式都没问题

### Next Plan


- FPGA: stub
- debug PT105 SMC



# 补充说明材料



- 

1. 

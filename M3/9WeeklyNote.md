### 工作总结

#### PCD100

- dma mux

- **dma mux**

  - 收集同事提供信息，更新 dma mux 表格

- **fsmc**

  - debug 端口位宽声明错误
  - 连接 iomux

- **intr**

  - dmax，te，smc 完成
  - 修正 te 中断向量表

- **工具**

  - 安装配置自动连线工具

- **DMA350**
	- 目前卡在验证安全功能的部分，发起`ch_stop`命令，波形上未显示。
	- 看case：`config_check_sec_ext`
	    - 安全违例寄存器配置，安全违例中断
	    - command link，命令提示符+待更新寄存器
	    - done pause 开关
	    - DMA 运行过程中，写 stop，写 pause 并恢复

#### PT105

- 支持软件同事理解 nand 中断信号

### 项目状态

#### DMA MUX

- [x] v0.1
- [x] 脚本
- [x] 收集同事 dma req 信息
- [x] v0.2
- [ ] 更新代码

#### DMA350

- [ ] `config_check_ext_feat`
- [ ] `config_check_sec_ext`
  - [x] 安全违例寄存器配置，安全违例中断
  - [x] command link，命令提示符+待更新寄存器
  - [x] donepause 开关
  - [x] DMA 运行过程中，写 stop，写 pause 并恢复

#### 中断向量表

- [x] 修正 TE 中断向量表
- [x] 连接负责 IP 的中断
  - [x] TE
  - [x] DMAX
  - [x] SMC

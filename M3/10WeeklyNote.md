### 工作总结

**DMA-350**

- PCD100 项目中可能涉及的 DMA-350 case 完成
  - `config_check_sec_ext`:**发起`ch_stop`命令，波形上未显示原因**：msc 报 irq 会拉低`ch_enable`在此之后写`ch_cmd`不会生效。
  - `config_check_ext_feat`:araddr 未增加问题：符合涉及意图，`xincr=0`
- 总结 case 问题笔记：dma350 testcase tips
- 查看cs330代码

**TrustEngine**

- 更换mem

**dmaMux**

- 根据 req 表格生成新 req，ack 代码上传
- 解决变更带来的问题
- 上传新 single，last

### 项目状态

#### DMA350

- [x] `config_check_ext_feat`
  - [x] 2D传输
- [x] `config_check_sec_ext`
  - [x] 安全违例寄存器配置，安全违例中断
  - [x] command link，命令提示符+待更新寄存器
  - [x] donepause 开关
  - [x] DMA 运行过程中，写 stop，写 pause 并恢复

#### dmaMux

- [x] req，ack
- [x] single，last
- [ ] eot

#### 更换mem

- [x] TrustEngine

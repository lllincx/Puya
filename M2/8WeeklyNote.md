## 工作总结

### PCD100

- dma mux
	- 出一版dma mux表格
	- 开发脚本，dma mux表格更新后可以输出代码。[[dma mux 表格脚本]]
- SMC（GMC )
	- 对比芯来GMC和SMC的功能
	- GMC无nand mem接口。feature 讲的支持one nand是接口类似nor的nand。
- 跑dma350 case
	- ext_feat case中包含不符合预期的波形行为，暂缓查看
	- sec_ext case查看进行中


## 项目状态

TrustZone

- [ ] ~~学习恩智浦安全手册~~
- [ ] corstone 320 新增资料学习
- [x] 参与系统安全会议
- [ ] 参与具体 IP TrustZone 集成
- [x] 调研N6加密IP发生错误时的处理措施

DMA350

- [x] 召开跨部门会议介绍 DMA
- [x] 编制表格，对比竞品 dma 性能
- [x] 对比不同 fifo 深度配置面积
- [x] 列举 ST，PT105 发起 req 外设列表
- [x] 配置对标 PT105 的 cfg，集成到 pcd100
- [x] 收集PT105 DMA req外设同步与否
- [ ] 跑 dma350 case，并研究波形
	- [x] `initial_checktest`
	- [x] `config_check_trigger_in`
	- [x] `config_check_trigger_out`
	- [ ] ~~`config_check_stream`~~
	- [ ] `config_check_ext_feat`
	- [ ] ~~`config_check_gpo`~~
	- [ ] `config_check_sec_ext`
	- [ ] ~~`max_power_test`~~
	- [ ] ~~`typ_power_test`~~
	- [ ] ~~`min_power_test



## 工作总结

### PCD100

- 完成集成DMA-350
	- 将原dmax上接口连线到dma350上
	- 原配置ahb接口替换为dma350 apb接口并与运卿对接
- 调研N6加密IP发生错误时的处理措施：[[SysSec N6安全IP错误管理]]
- dma mux：收集PT105 DMA req外设同步与否
- 跑 dma350 case
  - 包含 trigger case 的搬运，查看波形并研究状态机跳转
  - ext_case 其他复杂功能测试case，进行中

## PT105


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



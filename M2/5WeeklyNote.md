## 工作总结

### PCD100

- fsmc 集成：生成 fsmc filelist
- 参与系统安全会议
- dma350：生成不同 fifo 深度配置文件，综合对比面积大小
- 跑 dma350 case
  - 基础搬运，并查看波形
  - 包含 trigger case 的搬运，查看波形并研究状态机跳转

## PT105

支持 AE nand 16 位操作：

- 目前 fpga 无验证 nand 16 位操作能力，对 ST 的代码写法有疑问
- 查看 nand model 代码，nand 技术手册讲解行为解答技术问题
- 开发读 nand id case

## 项目状态

TrustZone

- [ ] ~~学习恩智浦安全手册~~
- [ ] corstone 320 新增资料学习
- [x] 参与系统安全会议
- [ ] 参与具体 IP TrustZone 集成

DMA350

- [x] 召开跨部门会议介绍 DMA
- [x] 编制表格，对比竞品 dma 性能
- [ ] 对比不同 fifo 深度配置面积
- [ ] 列举 ST，PT105 发起 req 外设列表
- [ ] 配置对标 PT105 的 cfg，集成到 pcd100
- [ ] 跑 dma350 case
	- [x]`initial_checktest`
	- [x] `config_check_trigger_in`
	- [ ] `config_check_trigger_out`
	- [ ] `config_check_stream`
	- [ ] `config_check_ext_feat`
	- [ ] `config_check_gpo`
	- [ ] `config_check_sec_ext`
	- [ ] ~~`max_power_test`~~
	- [ ] ~~`typ_power_test`~~
	- [ ] ~~`min_power_test
- [ ] 研究 dma350 case 波形
	- [x]`initial_checktest`x
	- [ ] `config_check_trigger_in`
	- [ ] `config_check_trigger_out`
	- [ ] `config_check_stream`
	- [ ] `config_check_ext_feat`
	- [ ] `config_check_gpo`
	- [ ] `config_check_sec_ext`
	- [ ] ~~`max_power_test`~~
	- [ ] ~~`typ_power_test`~~
	- [ ] ~~`min_power_test

fsmc

- [x] 完成集成 fsmc
- [x] 提交 fsmc filelist
- [ ] ~~集成 mpc~~


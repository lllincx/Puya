## 工作总结

### PT105

SMC访问nand flash时数据丢失
- hex仿真环境问题解决
- 软件问题复现
- 参与会议讨论
- 问题已解决

### PC100

- 对比竞品DMAfeature，列举表格[[WW56_DMA feature对比]]
- 检索AHB接口支持TrustZone的DMA
- 集成fsmc，完成度80%


## 项目状态
### PC100系统安全

TrustZone

- [ ] 学习恩智浦安全手册
- [x] ST N6 U5，英飞凌，瑞萨安全手册学习
- [x] corstone 320现有资料学习
- [ ] corstone 320新增资料学习

DMA350

- [x] 总结DMA-350为TrustZone架构的设计
- [x] 搭建环境实现仿真，可在verdi查看代码
- [x] 搭建综合环境，综合DMA-350，取得面积报告
- [x] 625mhz时钟综合，取得报告
- [x] 对比dma350，自研dma，ST瑞萨dma feature表格
- [ ] 再次学习dma350手册，全面了解功能
- [ ] 制作ppt介绍dma350

fsmc
- [x] 集成105已有的smc，dmc，mem_mux
- [ ] 集成fsmc_mux
- [ ] 集成mpc
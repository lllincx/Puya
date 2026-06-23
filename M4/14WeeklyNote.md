### 工作总结

**TrustEngine**

- 寄存器读写 case 运行成功
- 修复 rst 命名不匹配问题

**TZC**

- 根据 review 意见，完成定义的规格，上传 v1.9
- 检查 tzc 规格问题，纠正 dubhe 为安全感知
- 在 tzc 其他规格确定之前，codeing 任务完成
- 查看 SSE 320 中 tzc 的设计与连接
- 交流安全感知从设备实现方法

**DMA 350**

- 寄存器读写 case 运行成功
- 解决 qchannel port 问题
- 修复时钟复位问题
- 发现寄存器地址空间不足问题，更换 apb 位置

**fsmc**

- 修复遗留问题
- 修复 smc nwait rnb 问题
- 修复 syscfg 问题
- smc 寄存器读写 case 运行成功

**dmaMux**

- 新增 esmc dma req

---

### 项目状态

**Highlight**

- 清 lint

**Lowlight**

- tzc 参与 review 会议，对 spec 理解存在较大偏差，正在进行修正
- 清 lint gpio 问题存在一定反复

**Help Needed**

- TrustEngine OTP 方案待确定
- TZC 方案待定

**Next Plan**

- TZC 代码完成，后续 review，寄存器表格，文档
- OTP 方案文档提交并讨论
- DMAX，TrustEngine 集成文档

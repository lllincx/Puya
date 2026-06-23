### 工作总结

**fsmc**

- 与魏凯交流 fsmc hierarchy 定位问题
- fix `fsmc_da` `oe`连接问题（连`~nadv`)

**SMC**
- debug 集成时代码被修改导致的apb关键信号悬空问题

**Lint**
- SMC，fsmc，TZC

**Reg Tab**

- 生成 DMA-350 寄存器表格
- 从 PT105 迁移 TrustEngine, SMC 寄存器表格
- 根据新 TrustEngine 修改寄存器表格（主机数量相关的未修改）

**TrustZone**
- 参与arm工程师会议
- 参与OTP讨论会议
- 编写OTP方案说明，准备提交与arm讨论

**TrustZone Ctrl**

- 完成代码并上传
- 完成lint检查

### 项目状态

**Highlight**

- TZC完成代码并上传，并检查lint
- debug 集成时代码被修改导致的apb关键信号悬空问题
- 完成负责所有模块的寄存器表格文档

**Lowlight**

- fix smc aid位宽问题反复多次

**Help Needed**

- TrustEngine OTP方案待确定

**Next Plan**

- TZC报告，寄存器表格，Review
- OTP方案文档提交并讨论
- TrustEngine换mem，换完查lint

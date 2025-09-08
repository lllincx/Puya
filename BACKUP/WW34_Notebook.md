# WW34 周报

### SMC

支持 FPGA 同事了解 SMC ECC 相关情况
DBG SMC Byte 访问问题：与 Direcet Commend REG cmd_type 位有关，待 FPGA 同事进一步测试。
DBG SMC Byte 访问问题：与 Direcet Commend REG cmd_type 位有关。
进一步了解 Direcet Commend REG。
修改 smc input float 并 signoff
dbg fpga smc 时序违例问题：smc aclk 和 mclk 的关系

### TrustEngine

同事编写 TrustEngine 相关 OTP 空间访问表格
完成 OTP SPEC 提交严冯杰审阅，提交软件同事浏览，并负责后续答疑和完善。
参与软件部门会议，讨论秘钥梯事项。
TrustEngine 仿真 fail check：sram4 变更，case 需要与之匹配

完成 smc TrustEngine 模块 reg check
检查 lint: SMC & TrustEngine


# 8月18日 星期一


- 支持fpga同事了解SMC ecc相关情况
- DBG smc 8bit 访问问题
- 编写OTP WR、RD表格

# 8月19日 星期二


- 参与软件部门会议，讨论秘钥梯事项
- 构建通过秘钥梯加密case，对加密数据再次解密开是否匹配
- 本周前完成otp spec
- 完成smc TrustEngine模块reg check
- 修改smc input float 并signoff


# 8月20日 星期三

- dbg fpga smc 时序违例问题：smc aclk 和 mclk 的关系
- 检查 lint: SMC & TrustEngine
- 完成OTP SPEC v0.1，提交严冯杰审阅

# 8月22日 星期四

OTP SPEC 完善
### SMC
- DBG SWD：direst cmd ModeReg 问题
- DBG FPGA hex sim 问题
- DBG 8Bit：direst cmd ModeReg 问题


# 8月23日 星期五

- [[TrustEngine 模块软件同事诉求汇报]]
- TrustEngine 仿真fail check
- OTP SPEC完善
- 进一步了解direct cmd reg
- DBG SWD：direst cmd ModeReg 问题：UpdateRegs and AXI 断开，其他不断开：仅nor flash 支持「UpdateRegs and AXI」。
> 郭老师：pready 挂住


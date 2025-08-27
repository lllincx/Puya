#### TrustEngine case DBG

上周可能因为环境问题导致的 case bug 情况目前已经解决

#### 支持 FPGA 进行 OTP 调试

参与讨论会议
提出完善 case 意见，请示张老师，对 FPGA 没有进一步验证要求
强调 otp space init 参数问题
DBG hex 仿真问题，发现 fpga 版本代码 IRQ 悬空问题提交处理。该问题解决后取得一定进展：IP接口上有动作，但仅为开关DMA时钟，未进行数据操作，等待代码更新进一步DBG。反馈问题到群里，目前没有回复。

![89ab85a7d8b2bc6aeb21a1089a3de43c](https://raw.githubusercontent.com/lllincx/IMG/master/89ab85a7d8b2bc6aeb21a1089a3de43c.png)

#### TrustEngine Introduction Meeting Issue Solution

SCA 非整数倍输入补零问题解决
ACA 三个操作数用途问题，查看代码处理中

#### 编写HEX Sim笔记

![[HEX Sim]]
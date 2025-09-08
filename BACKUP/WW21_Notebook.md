# Mon, May 19

### TrustEngine TRNG DBG

与李老师沟通，因为存在组合逻辑环，RTL没有delay，仿真时间不再往前推进
与张老师沟通，不再验证该模块
#### TrustEngine introduction

主要进行ACA内容填充


# Tues, May 20

#### 参加FPGA验证日会

#### TrustEngine introduction

完成PPT，讲稿初稿


# Wed, May 21

#### TrustEngine introduction

完善PPT，完成讲稿
召开会议介绍

[[TrustEngine Introdution Meeting Minutes]]


#### 支持OTP 调试

1. 测试那边的`DUBHE OTP INIT VALUE=0`
2. 测试那边的OTP空间可以写入
要来他们的hex文件在我的环境下执行

```
1.SOC_PT105_VERIFY/bin/ihex2mem32.pl
2./pt1-5_soc_v1/asic/dv/tests/rtl_typ0/example/fc_fpga_example_sram/c_dst/arm_c_dst/mem32 //生成文件放置位置

```

# Thur, May 22

参与员工培训
参与ECO工具介绍会议

# Fri, May 23

#### 支持 FPGA 进行 OTP 调试

**解决多种问题，成功跑起 HEX 文件**
IP 接口上没有动作
OTP 的初始化正常
返回给 FPGA 重新提供 HEX

#### TrustEngine DBG

原本 case 出现跑不通的情况，尝试各种方法无果后，删除全部验证文档重新 clone
其他 case 没问题，sca 存在一些问题

#### TrustEngine SPEC

校对完成并汇报

#### 检索密钥梯的用法

检索国家行业标准一篇，国际技术标准一篇



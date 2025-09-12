# 9.8 Mon

### SMC Byte Issue

Confirm word access work after the fix above.
Complete SPEC with two solution comparison.[[WW37_SMC_Nor Flash Byte Access]]

### TrustEngine OTP SPEC

Update for otp change 2
Update otp table

# 9.9 Tue

- Optimize TrustEngine OTP SPEC
- Participated in meeting on FPGA secure boot testing.
- Study OTP567 case
- Develop new LCS case

# 9.10 Wed

- Optimize TrustEngine OTP Table: mainly permisson
- Develop new LCS case: running, take long time
- Find OTP BUG: init OTP value, todo
- Optimize TrustEngine SPEC

# 9.11 Thu

- Cai Ziyang: SMC Nor A16 issue
- Run fpga sim,no A16 issue found.
- Optimize SMC SPEC
- Run new LCS case blocked

# 9.12 Fri

### TrustEngine

- Confirm DTCM availability: YES
- Ask for OTP SPEC confirm: to be done on the weekend
- DBG OTP user spec addr.

#### DTCM Issue

- DTCM Access fail
- Run HEX sim

### SMC

#### A16 Issue

Ask Cai Ziyang test more addr to locate the problem.
HEX sim don't have the problem.
Test env hardware cause the problem, A16 issue solved.

# Weekly Report

## SMC

编写文档，记录DBG ByteAccess过程
蔡紫阳提出A16问题，协助完整FPGA，HEX仿真，定位问题并最终解决。
优化SMC SPEC，进度约50%
### TrustEngine

根据OTP空间第二次变更，修改OTP SPEC与表格
参与FPGA安全启动测试会议
学习OTP567 case并开发新OTP对应的lcs case
DBG OTP：变更OTP初始值
优化TrustEngine SPEC 完成
协助解决DTCM访问问题，进行HEX仿真。
DBG OTP 用户安全区地址设定。

# To-do

Complete TrustEngine OTP SPEC update
Optimeze SMC SPEC
Ask TrustEngine DTCM progress

==pointer==

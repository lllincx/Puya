# 9.15 Mon

### TrustEngine

- confirm OTP SPEC done and submit
- finish OTP variable (page 5.6.7) case and push
- add OTP fixed (page 2.3.4) case and push
- join meeting on ACA SRAM clear under TAMP hacking

### SMC

- Update SPEC

# 9.16 Tue

### TrustEngine

- Support Liu Xiande for understanding OTP SPEC
- Support Shawn for verifying OTP page 2.3.4 prg and chk
- DBG wr lcs = 7, but rd lcs = f

### SMC

- update SPEC

# 9.17 Wed

### TrustEngine

- **explain why "wr lcs = 7, but rd lcs = f"**: lcs[3] reserved for hardware use, software shoud not read it.
- **Found issue**: **user sec/no-sec area** too small (8B). Data meant for user secure area wrongly placed in test area, but no impact on most accesses. TrustEngine read perms differ but ignorable since always readable in flash. Reason flash is always readable: to verify successful writes.

### SMC

- update SPEC, mainly ECC.

# 9.18 Thu

### SMC

- Update SPEC. [[WW38_SMC_ECC SPEC]]
- Run and chk ECC case for wr SPEC.

### TrustEngine

- opt case for page 2.3.4
  - add selfcheck func during LCS=DD/DR for preset LCS
  - add selfcheck func during LCS=DD/DR for inc LCS
  - cfm key access perm duing invaild LCS

# 9.19 Fri

### SMC

- Update SPEC.
- Run and chk ECC case for wr SPEC.

### TrustEngine

- update usr reigon to match design intent
- run case to verify OTP work well after update
- test page 2.3.4 rd perm during invalid LCS such as 101.

# Weekly Report

## SMC

- 更新 SPEC
- 为完成 ECC 章节 SPEC，进一步查看并测试 ECC case
- 支持蔡紫阳理解存储器时序参数

## TrustEngine

- OTP 文档：与严冯杰确认文档修改并提交刘贤德，支持刘贤德理解文档问题
- 支持刘贤德了解 LCS 写 7 会读回 f 的问题：LCS[3]为保留位，供硬件内部使用，读 f 符合设计意图
- 验证 Case 开发：完成 OTP_variable (page 5.6.7), OTP_fixed (page 2.3.4)
- 测试异常 LCS（如 101）下 OTP 空间的读写权限。
- 优化验证 Case：将发生 Hardfault 纳入预期。
- 参与会议了解 TAMP 侵入下 ACA SRAM 问题
- 发现问题：用户安全、非安全区定义过小，导致 RTL v2.0 预期放入用户安全区的数据被放入测试区域。但对访问无影响，已经受到软件部门认可。
- 在 fmc 模块不做修改下，调整 OTP cofig 宏定义使用户安全区符合设计意图。并测试读写权限。

**OTP Case**
![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250924115047225.png)

**调整 OTP cofig 宏定义使用户安全区符合设计意图**
![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250924115108724.png)

# To-do

- 支持蔡紫阳理解存储器时序参数

  - 构建 case，得出变化时序参数后的波形
  - 分析由于 SMC 和存储器时序参数不同的原因和后果

- 完善 SMC，TrustEngine SPEC，补充寄存器章节

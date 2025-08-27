# Tues, June 3

#### SCA_cg code review

计算模块没有看
扩展不同配置的case，如外部key，非整数源地址，目标地址

- mgr
  - dmain_intf
  - dmaout_intf
  - ~~calc_core~~

#### hash_cg code review

- host_0
  - regfiledvbu


# Wed, June 4

#### hash_cg code review

改external key

- host_0
  - regfile

#### 支持软件同事

- lock_ctrl 读写方式
- usr_region 读写方式
- flash 写入 otp 流程，OBL 复位影响情况

#### 支持验证

优化otp access

#### 支持FPGA

读dubhe_conf1_addr 32位数据
了解vivado

#### OTP Review

读user reigon看什么值 期望是default


# Thur, June 5

#### hash_cg code review

改 external key

- host_0
  - regfile

#### 学习 vivado

![[头文件DBG情况]]

#### OTP Review

读 user reigon 看什么值 期望是 default

![[OTP usr region DBG]]


# Fri, June 6

#### 1


头文件

synth 8-9263
cannot open include file **.vh

头文件已经被包含在工程中但仍显示：
解决方法：将准备add的.v,.vh文件放置在同意目录中。

#### 2

usr region 问题验证通过


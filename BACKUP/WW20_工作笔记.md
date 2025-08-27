# Mon, May 12

### TrustEngine

#### 移植 tc_c_sca

![[SCA 问题及排查过程]]

# Tues, May 13

### TrustEngine

再次尝试解决TRNG问题，咨询验证同事未果
进行[[Trust Engine 任务汇报]]
下一步任务：结合case跑出来的波形进一步学习一下代码

查看代码：
- apb
- reg access
- mem access

# Wed, May 14

### TrustEngine

处理 OTP 加载，LCS 相关问题
优先查看 OTP 相关代码

`DUBHE_OTP_INIT_VALUE`保持为0会导致LCS的配置与检测需要多个映射表：

| LCS          | CM  | DM  | DD  | DR  |
| ------------ | --- | --- | --- | --- |
| 3'b          | 000 | 001 | 011 | 111 |
| flash write  | 7   | 6   | 4   | 0   |
| read otp spc | 8   | 9   | b   | f   |


掌握更改 OTP flash 数据方式


# Thur, May 15

### TrustEngine

#### Mem_access DBG

##### bug情况

只能进行一次读写，第二次读写会fail

##### 前期忽略原因

case读写数据较多，以为是需要仿真时间过长，于是手动中断

##### 排查与解决

rdata为X态，由raddr指向高位导致（高位未写数据）
原因未raddr一次读写后未归零
在VIM中复制错误导致，未仔细检查

#### OTP access Code Review

40%

# Fri, May 16

### TrustEngine

#### 周会

#### TrustEngine introduction

##### 任务安排：

**向 FPGA 介绍 IP 情况**
着重 OTP 方面
编写 PPT 30 页左右
下周三提交

##### 工作情况：

**参与跨部门会议**
外包比较熟悉IP，目前进行了SCA和ACA的验证
内部对IP不太熟悉，需要介绍

**编写PPT：17页**



# WW32 周报

### SMC

试图出基于 Newbus 的 bitfile，解决 FPGA 仿真环境 bug，解决 verdi 目录结构混乱问题。
DBG fpga case：fpga_pinmux 设置有疏漏，D12 重复设置。
DBG 全部外包 case：目前 fpga sim 外包的 case pass，fail 函数失效，会一直 run，需要替换为内部函数。
解决软件同事关于 SMC 的深度技术问题。
深入学习 ECC 操作。

### TrustEngine

#### OTP

参与 OTP 存储空间变更会议，并制作报告向软件同事汇报讨论并解决相关疑问
制作报告，汇报 OTP 不同配置的写入需求优先级。
根据对 LCS 和用户定义安全区的理解要求改变存储配置。

#### SCA

软件同事要求配合研究秘钥梯生成算法

### 待完成事项

#### SMC FPGA SWD DBG

解决方法：开发 SMC SWD case，执行仿真查看结果

#### TrustEngine SCA

研究秘钥梯生成算法

# 8月4日 星期一


支持fpga dbg SMC：
出基于newbus的smc bitfile

支持软件同事关于SMC相关问题

深入学习 smc ECC 操作

# 8月5日 星期二


- 支持软件同事关于SMC相关问题
- 深入学习 smc ECC 操作
- DBG SMC FPGA sim


# 8月6日 星期三


### TrustEngine OTP

[[TrustEngine OTP WR Req]]
参与OTP会议，讨论存储空间变更

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250807094157796.png)



### SMC

解决fpga sim问题
verdi目录结构混乱：删除novas文件

研究ECC jump暂停

# 8月7日 星期四


### smc

#### debug fpga sim

nor_basic case可以跑通，但nor_buffer_pgm跑不同：fpga_pinmux设置有疏漏，D12重复设置，读0时会产生X态，导致仿真错误，basic case由于没有读0的情况所以错误通过。

目前fpga sim 外包的case pass，fail函数失效，会一直run，需要替换为内部函数。

### TrustEngine

#### OTP

向软件同事介绍OTP空间变更，并解决一些疑问：
1. page的高位空间无效
2. OTP是否可以重复写？
3. 任务计划：OTP SPEC

#### SCA

软件同事要求配合研究秘钥梯生成算法


# 8月8日 星期五


0x100 usr_sec_blk0 FOTAH
0x104 usr_sec_blk1 FOTAL
0x108 usr_sec_blk2 Recovery manifest version
0x10c usr_sec_blk3 Primary manifest version


我今天下午和张老师讨论了一下，为了更适配Shaihai软件调用的场景，【FOTA，manifest version】应该作为OTP的用户安全区域设置。

与其他只写一次的page保持一致，复位时将【LCS，FOTA，manifest version】载入Shaihai内部寄存器。在此处添加：
```
13'h100:flash_otp_data = usr_sec_blk0； //FOTA1
13'h104:flash_otp_data = usr_sec_blk1； //FOTA2
13'h108:flash_otp_data = usr_sec_blk2； //Recovery M.V.
13'h10c:flash_otp_data = usr_sec_blk3； //Primary M.V.
```

撤销【FOTA，manifest version】lcs[2]置位后不可读的需求。
变为LCS，FOTA，manifest version三个page均设为始终不可读，与其他只写一次的page保持一致。


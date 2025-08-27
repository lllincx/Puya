# WW 33 周报

### 协助完成寄存器表格变更

### SMC

#### swd 访问问题

开发 swd 仿真 case，并解决环境问题，仿真通过，与 Ccase 现象一致
开发 Ccase，连续以不同方式读 smc reg 地址无误
完成代码修改并提交，新网表待 fpga 上机测试

#### 8bit 访问问题

与 fpga 同事交流问题现象
fpga hex 仿真对比 16bit 与 8bit 波形
构建 asic 仿真 case：nor sector erase

### TrustEngine

#### 秘钥梯原理分析

#### 进一步熟悉 TrustEngine 软件手册

#### OTP 空间变更查看

推进验证反馈

#### OTP SPEC

改编 OTP 强相关的 flash 表格


# 8月11日 星期一


### 寄存器表格变更
### swd case开发

# 8月12日 星期二


### swd case 开发

### TrustEngine 秘钥梯原理分析

根据波形看了一下秘钥梯使用过程中的行为，绘制了一下示意图。
sca 计算核有数据输入输出和秘钥输入输出。
通过调用计算核，输入 root key「OTP 空间中」、EK123，即可输出最终秘钥。

![](https://raw.githubusercontent.com/lllincx/IMG/master/Snipaste_2025-08-12_16-38-52.png)


# 8月13日 星期三


### 开发 swd case

「 asic & FPGA 」读 smc 的 RO，WO，RW 寄存器，与 Ccase 现象一致

### TrustEngine 软件集成手册阅读

[[WW34_TrustEngine Software 集成手册]]


# 8月14日 星期四


### 协助解决 swd bug

- 连续读 smc reg 4kb 地址，双字读，比特读无误
- 代码修改

### DBG 8bit 问题

进行 hex 仿真
仿真前由于近期变动点多，其他 case 出现跑不通情况，花费时间 DBG


# 8月15日 星期五


### DBG smc 8bit

与fpga同事交流问题现象
fpga hex仿真对比16bit与8bit波形
构建asic仿真case：nor sector erase

> byte，word访问device要求命令不同
> 需要在asic环境修改device的byte位

### OTP 空间变更查看

推进验证反馈

### OTP SPEC

改编OTP强相关的flash表格


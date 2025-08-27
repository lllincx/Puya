# WW29周报

### 周二到周五参加公司培训

### SMC

- DBG busy 信号无反馈问题
  - 开启 norflash_en，进行 hex 仿真无误，提交 fpga 共同 dbg
- 看更新的 case
  - nor buffer pgm
  - nand_block_rease
  - tc_c_smc_nand_readcheck
  - tc_c_smc_nand_ecc（进行中）
- 解决读 nand status 会返回错误的加长数据问题
- 发现 nand_ecc 时钟更改问题，提交宇波处理
- 学习 nand 器件手册

### TrustEngine OTP

- 支持外包解决密钥无法读取问题
- 根据外包提供 hex 执行仿真，并要求其解释波形现象
- 导出 ccase 给内部软件部门并提供描述
- 检查软件部门返回的 keil 工程
- 实机测试通过，otp_access，lcs case 符合预期
- 了解 flash 内数据预置方法，准备出 bitfile 验证 otp_rdck case

### 支持 dmc sdram 连接问题


# 7月14日 星期一

## SMC DBG

DBG smc nor busy 信号无反馈问题。
NorFlash_en没有开：fpga不需要开该选项，hex仿真需要手动配置开启该选项才可以与对方匹配。
hex仿真结果显示没有问题，提交fpga共同dbg。

## TrustEngine DBG

密钥始终无法读问题。
IP总线上没有变化，要求软件提供在flash启动的hex。
run较长时间，波形上显示IP仅进行了时钟和复位操作，且相隔很久，要求软件解释相隔很久的原因，要求提供反汇编文件。

## 其他

支持dmc sdram连接问题。
参与商业保险会议。


# 7月15日 星期二


### 应届生培训

### TrustEngine OTP DBG

TrustEngine OTP Ccase 导出给内部软件部门


# 7月16日 星期三


### 应届生培训

### SMC case review

- nor buffer pgm
- nand_block_rease

### TrustEngine OTP

TrustEngine OTP Ccase 导出给内部软件部门
[[OTP Ccase intro]]
浏览返回的 Keil 工程


# 7月17日 星期四


### 应届生培训

### SMC case review

- nand_block_rease
读nand status会返回错误的加长数据，实际状态为8'he0，返回数据为32'he000e0。添加nand_rsta函数调用read_mem16解决此问题。

### TrustEngine OTP

目前otp_access，lcs case fpga测试符合预期
[[预置flash内内容方法]]
出bitfile受阻



# 7月18日 星期五


### 应届生培训

### SMC case review

### TrustEngine OTP

提供预置 flash 内容的 bitfile

tc_c_smc_nand_readcheck 不写数据，只从 0 地址读数据并与 4\*addr 对比，case 不通过，这个 case 是需要在运行之前预置器件内的数据吗。

tc_c_smc_nand_ecc(\_inj)报错：

```
$stop at time 960508500000 Scope: top.u_dut_top.DUT_TOP_FSMC.u_nand_flash_0 File: /PRODUCT_MCU/PT105/V1/_gitview/lincx/pt105_init/SOC_PT105_VERIFY/env/..//tb/top/dut_top/subs/fsmc/nand_flash/w29n02gwxxba.v Line:2909
```



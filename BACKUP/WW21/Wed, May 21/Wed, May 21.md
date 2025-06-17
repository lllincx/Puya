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
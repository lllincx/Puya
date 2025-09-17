# Sun, April 27

### TrustEngine

- otp_access case 浏览
- lcs_func_test case 浏览
- trng_func_test case 浏览
- 包含文件查看：
	- sh_common.c 浏览
	- mem_rw.c 浏览

完成除 puf_basic 外所有硬件集成手册中提及的 testcase
完成 10/10 所有 case 浏览

参与培训

解决内部仿真环境问题，可以执行了
	解决方法：datebase应该由脚本生成

# Mon, April 28

解决至安盾客户端截图问题

### TrustEngine

完成 10/10 所有 case 浏览

解决仿真环境问题
+ 新case模板创建
+ 头文件位置



# Tues, April 29

### TrustEngine

### case lib

编写 IP 头文件：
`/PRODUCT_MCU/PT105/V1/_gitview/lincx/SOC_PT105_VERIFY/ccase/lib/pt105/Include/py32f537_func.h`

移植外包 case 函数：
`/PRODUCT_MCU/PT105/V1/_gitview/lincx/SOC_PT105_VERIFY/ccase/lib/pt105/Source/py32f537_func.c`

解决IP基地址问题：
```
.../pt105_init/SOC_PT105_VERIFY/tb/env/subs/$module
//set ma 解锁后修改
```
解决仿真环境问题

### 移植 case


tc_c_otp_access
tc_c_mem_access
tc_c_reg_access
tc_c_apb

# Wed, April 30

### TrustEngine

以tc_c_otp_access为线索，了解IP

解决：
[[otp_access 问题及排查过程]]


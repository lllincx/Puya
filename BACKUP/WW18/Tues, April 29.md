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
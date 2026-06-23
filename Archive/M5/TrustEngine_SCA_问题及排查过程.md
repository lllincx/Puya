##### 1. `wait otp init ready` 函数问题

移植该函数到内部仿真环境后，可能会错误打印出超时信息。
经查看波形，暂不存在超时现象。
故注释掉该等待函数
更改为 otp init ready 时打印信息，再实际执行时，若未打印再具体检查或修改
```C
/*################################################ 
replace wait otp init ready because it's always ready
################################################ */ 
//SIM_chkpt(0x71);
reg32_rdata=rd(OTP_MANGER_ADDR);
if(reg32_rdata==1){                 //otp init ready? 
	SIM_printf("otp init ready\n"); 
//SIM_chkpt(0x80);
//wait_otp_init_ready(); 
//SIM_chkpt(0x72); 

```
#### 2. 时钟开启有误导致输出数据不匹配
```
../shanhai/sh_sca_cg_test/sh_cmd.c/
36:write_mem(BASE_ADDR+Ox00000000,0x00000002);//open sca clock
-> write_mem(BASE_ADDR+Ox00000000,0x0000001f);
```

> 设置为`1f`可能存在功耗上的问题，具体哪些时钟可以关断还需要进一步试验


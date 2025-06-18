1. 所有 case 的 FC_c.log 都有 HardFault detected
   ![Pasted image 20250611095618](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250611095618.png)

   > 可以忽略

2. `sh_trng_func_test`卡住，手动中断后，波形显示和我们在内部环境无法运行的现象一致。
```
pt105_soc_v1/ip/soc/TrustEn200/rtl/macro/rm_inv.v
28://`elsif sc7mcpp140z_cln22ul //ARM 22
29://puya_inv 1_inv_dontouch(,ZH(2),,I(A));
```

![Pasted image 20250611105018](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250611105018.png) 

3. 多个存储器类型访问被添加到了 hash case 里面，在他们的环境和移植过来之后，其他类型的存储都是会 fail 的

> SMC 不能写，其他已经解决

| case name            | 符合预期 | 移植完毕 |
| -------------------- | ---- | ---- |
| sh abnormal_ahb_test | 1    | 1    |
| sh abnormal_apb_test | 1    | 1    |
| sh_aca_cg_test       | 1    | 1    |
| sh_hash_cg_test      | 0    | 1    |
| sh_lcs_func_test     | 1    | 1    |
| sh_mem_access_test   | 1    | 1    |
| sh_otp_access_test   | 1    | 1    |
| sh_reg_access_test   | 1    | 1    |
| sh_sca_cg_test       | 1    | 1    |
| sh_trng_func_test    | 0    | 0    |

## 失效功能

经排查，只要对 `rn_pool_fill_req (rn_pool_crtl REG)` 按照文档要求写 1，即会触发仿真停止
![](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250508100737.png)

---

![Pasted image 20250508102414](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250508102414.png)

其中，checkpoint 设置如下：

```C
SIM_printf("chain_en: 0\n")
SIM_chkpt(0x71);
wr(TRNG_ADDR+0x4, 0x1); //entropy_src
SIM_chkpt(0x72);
wr(POOL_CTRL_ADDR, 0x1); / pool ctrl
SIM_chkpt(0x73);
```

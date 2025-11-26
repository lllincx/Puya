> 李老师昨天报告了fmc相关的违例，这一条是因为nand输出的中断信号（busy）没有直接进行cdc处理，而是在ip内部作为时钟产生一个信号int_status，然后对这个信号进行同步。因为这中间一部分逻辑是yuyang写的，不是golden的，所以我又检查确认了一下。

### 背景

![image.png|400](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110107572.png)
![Snipaste_2025-11-10_11-01-33.png|1000](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/Snipaste_2025-11-10_11-01-33.png)

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110209202.png)

### fmc_int

fmc_int 信号由 nand 的 busy 输出经 pinmux 过来。

![image.png|800](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110232897.png)

fmc_int 经过时序逻辑成为 fmc_int_r，fmc_int_r 可能为亚稳态

![image.png|400](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110325481.png)

代码 blame

![image.png|600|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110134115601.png)

fmc_int_r --> pre_mux_nand_busy_o -->nand_busy_o

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110428759.png)

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110457831.png)

在 smc ip 内部 busy_1 当做时钟处理，产生 int_status

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110110523728.png)

最后对 nand_busy (int_status) 进行同步处理

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251110111032452.png)

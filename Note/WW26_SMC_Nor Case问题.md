# `SCB_CleanInvalidateDCache`函数问题

Q：包含的函数`SCB_CleanInvalidateDCache`在`.../ccase/lib/arm_cm4/Include`中声明，该函数参数为空。但在 case 中使用的方式是含参数的。

![image.png|600](https://pic.lllincx.cn/20250624094714665.png)

![image.png|600](https://pic.lllincx.cn/20250624094917465.png)

==A：M52中该函数有参数。

# 读出数据与波形不匹配问题

## 2025.6.24 描述

由于 nor model 未配置，其中数据应为全 f，但此处读出数据为 0x779988

![image.png|450](https://pic.lllincx.cn/20250624095240439.png)

![image.png|1000](https://pic.lllincx.cn/20250624095914352.png)

## 2025.6.25 描述

此前描述的对应有问题。实际情况如下:
case 读 mem 共三次，因为第二次读操作在 arvalid 与 rvalid 上没有响应，因此误认为第三次读取是第二次。
目前问题转变为：对 mem 的读操作在 smc 和 CPU 接口上无变化，可能与 cache 有关

![|1000](https://pic.lllincx.cn/20250625111817589.png)

在 chkpt=12 位置，CPU 有读取 77669988 现象。
![image.png|1000](https://pic.lllincx.cn/20250625111930789.png)

在 chkpt=13>14 位置，CPU 无预期读操作。
![image.png|1000](https://pic.lllincx.cn/20250625112028940.png)

==A：**是cache打开的原因， CPU直接从Dcache读了， 如我飞书所讲，我在这个case 把Dcache 关掉了， 现在可以了**

# NOR 等存储 model 数据预埋方法

咨询宇阳，他表示不是很清楚。
==A：在case下构造这个preload 文件， 就是常用的readmemh的方式preload的，可以通过@address , 指定位置

![image.png|1000](https://pic.lllincx.cn/20250625135017923.png)

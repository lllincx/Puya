# `SCB_CleanInvalidateDCache`函数问题

包含的函数`SCB_CleanInvalidateDCache`在`.../ccase/lib/arm_cm4/Include`中声明，该函数参数为空。

![image.png](https://raw.githubusercontent.com/lllincx/IMG/master/20250624094714665.png)
但在 case 中使用的方式是含参数的。
![image.png](https://raw.githubusercontent.com/lllincx/IMG/master/20250624094917465.png)

# 读出数据与波形不匹配问题

由于nor model未配置，其中数据应为全f，但此处读出数据为0x779988

![image.png](https://raw.githubusercontent.com/lllincx/IMG/master/20250624095240439.png)

![image.png](https://raw.githubusercontent.com/lllincx/IMG/master/20250624095914352.png)

# NOR 等存储model数据预埋方法

咨询宇阳，他表示不是很清楚。
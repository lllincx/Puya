# 一、ACA 与 SCA 测试结论相同问题

这是由于测试结论是对 shanhai 整个 IP 来讲的测试结论吗？看起来不是的。
似乎是一个子模块的报告是另外一个作为模板，最终测试结论部分没有修改。
![image.png](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250626095204961.png)

![image.png](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250626095344293.png)

# 二、测试数据对应问题

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250626095815760.png)

# 三、SCA 未测试 SM4 算法

# 四、TRNG 测试

我今天仔细查看发现，TRNG 测试作为两个大项目包含在了 ACA 的表格里。
我认为测试覆盖不足，TRNG 作为与 ACA 并列的子模块应该需要单独列一个表格，并且其中有很多功能配置项需要比对 SPEC 逐个测试。比如：
遍历内部各个熵源，选用外部熵源查看输出结果
测试随机数后处理对随机性提升幅度
生成低质量随机数(通过选用低质量外部熵源方式等),测试 TRNG 内部随机度测试与评价功能

# 五、Hash，OTP 未测试

# 六、TRNG 与加密算法联动测试

trng 生成随机数作为密钥进行 hash，sca 加解密测试

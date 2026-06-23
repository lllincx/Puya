# Mon, April 21

### PT106-CRC

结合波形了解 IP

### TrustEngine

获取文档资料@朱高林

阅读技术参考手册
+ Technical overview
	+ SCA
	+ ACA
	+ HASH
	+ OTP strage contraller
	+ TRNG
+ Register descriptions


# Tues, April 22

### TrustEngine

#### 文档阅读

+ 技术参考手册
	+ Register descriptions
	+ Signal descriptions
+ 硬件集成手册
+ 其他手册

#### 仿真执行

+ flow了解
```
\\192.168.1.8\pt105\V1\A15_verification\verification env user guide v1p5
make go FSDB=1
make verdi
```


# Wed, April 23

### TrustEngine

#### 解决仿真环境问题

- 代码更新问题
- 服务器问题

结论：解决环境问题之后发现外包 testcase 存在问题，CPU 没有正常运行，跑不通

#### 工作计划

阅读并标注现有 testcase 访问寄存器及读写数据的情况
了解其流程与意图
向内部 flow 移植 testcase

#### TestCase 标注

aca_cg_test


# Thur, April 24

### TrustEngine

- aca_cg_test 寄存器标注
- aca_cg_test 关键命令分析与技术参考手册的针对性学习
- hash_cg_test 寄存器标注
- hash_cg_test 关键命令分析与技术参考手册的针对性学习


# Fri, April 25

### TrustEngine

- hash_cg_test 寄存器标注
- hash_cg_test 关键命令分析与技术参考手册的针对性学习
- sca_cg_test 寄存器标注
- mem_access case 浏览
- reg_access case 浏览
- abnormal_apb case 浏览

完成除 puf_basic 外所有硬件集成手册中提及的 testcase
完成 6/10 所有 case 浏览



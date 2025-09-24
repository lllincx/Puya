#rep 
### 一、密钥梯

Key Ladder（密钥阶梯）是一种在加密系统中用于安全管理和派生密钥的分层机制。其核心思想是通过多级密钥的逐层派生，保护根密钥（通常是最顶层的密钥）不被直接暴露，从而提升系统的整体安全性。
需要使用 EK1，EK2，EK3 三个参数的原因是为了兼容通用标准：

国家行业标准：[可下载条件接收系统技术规范](https://www.nrta.gov.cn/module/download/downfile.jsp?spm=chekydwncf.0.0.1.HYsXqs&classid=0&showname=GYT%20255-2024%E3%80%8A%E5%8F%AF%E4%B8%8B%E8%BD%BD%E6%9D%A1%E4%BB%B6%E6%8E%A5%E6%94%B6%E7%B3%BB%E7%BB%9F%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83%E3%80%8B.pdf&filename=114fb5fe3d2b4c748e86b5e4630056cc.pdf)，见附件一。

![Pasted image 20250527172800](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/Pasted%20image%2020250527172800.png)

国际技术标准：[ETSI TS 103 162 V1.1.1](https://www.etsi.org/deliver/etsi_ts/103100_103199/103162/01.01.01_60/ts_103162v010101p.pdf)

![Pasted image 20250527172101](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/Pasted%20image%2020250527172101.png)

#### 二、SCA 输入数据非整数问题

```
SCA_Process(src, size, dest);
\\Data size:The byte size of the original data. This size must be aligned to the 16-byte block size except for CMAC mode.
```

SCA Process 命令的数据尺寸参数要求：除 CMAC 模式外，必须 16 位对齐。IP 不支持自动补充操作，可要求用户手动补 0。

#### 三、ACA 操作码与操作数

##### 待写入入口寄存器的数据内容

operand_a: GRID O
operand_b: GRID P
operand_c: GRID Q
operand_r: GRID R
len_type_id: len_type_S

##### 通用寄存器或长度类型寄存器的数据内容

GR O: addr w，待计算的数据 A 所在的 sram 首地址
GR P: addr x ，待计算的数据 B 所在的 sram 首地址
GR C: addr y ，待计算的数据 C 所在的 sram 首地址
GR R: addr z ，计算的结果数据 R 所在的 sram 首地址
len_type_S: 数据 L，待计算的数据 A、B、C 的长度

##### Operand a, b, c, r 的关系

对一般运算操作，数据 R 为数据 A，数据 B 运算的结果，不使用数据 C
仅对模乘加（Modular Multiplication and Accumulation，modMULACC），免约减模乘加（Modular Multiplication and Accumulation without reduction，modMULACCNR）来说，数据 R 为数据 A，数据 B，数据 C 运算的结果。

$$
\begin{align}
modMULACC:R  &= (A\times B+C)\ mod\ n\\
modMULACCNR:R  &= A\times B+C
\end{align}
$$

示意图详见附件三：
![[Pasted image 20250527172349.png]]

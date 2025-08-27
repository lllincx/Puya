# Mon, May 26

#### TrustEngine case DBG

上周可能因为环境问题导致的 case bug 情况目前已经解决

#### 支持 FPGA 进行 OTP 调试

参与讨论会议
提出完善 case 意见，请示张老师，对 FPGA 没有进一步验证要求
强调 otp space init 参数问题
DBG hex 仿真问题，发现 fpga 版本代码 IRQ 悬空问题提交处理。该问题解决后取得一定进展：IP接口上有动作，但仅为开关DMA时钟，未进行数据操作，等待代码更新进一步DBG。反馈问题到群里，目前没有回复。

#### TrustEngine Introduction Meeting Issue Solution

SCA 非整数倍输入补零问题解决
ACA 三个操作数用途问题，查看代码处理中

#### 编写HEX Sim笔记

![[HEX Sim]]

# Tues, May 27

#### 支持 FPGA 进行 OTP 调试

IP 接口上有动作，但仅为开关 DMA 时钟，未进行数据操作问题仍然存在。
考虑可能是仿真时间不够导致。

[[ASIC & FPGA parameter unmatch issue]]
#### TrustEngine Introduction Meeting Issue Solution

学习蒙哥马利算法

[[TrustEngine 中 SPEC未提及的若干问题解释]]

# Wed, May 28

#rep 
### 一、密钥梯

Key Ladder（密钥阶梯）是一种在加密系统中用于安全管理和派生密钥的分层机制。其核心思想是通过多级密钥的逐层派生，保护根密钥（通常是最顶层的密钥）不被直接暴露，从而提升系统的整体安全性。
需要使用 EK1，EK2，EK3 三个参数的原因是为了兼容通用标准：

国家行业标准：[可下载条件接收系统技术规范](https://www.nrta.gov.cn/module/download/downfile.jsp?spm=chekydwncf.0.0.1.HYsXqs&classid=0&showname=GYT%20255-2024%E3%80%8A%E5%8F%AF%E4%B8%8B%E8%BD%BD%E6%9D%A1%E4%BB%B6%E6%8E%A5%E6%94%B6%E7%B3%BB%E7%BB%9F%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83%E3%80%8B.pdf&filename=114fb5fe3d2b4c748e86b5e4630056cc.pdf)，见附件一。

![Pasted image 20250527172800](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250527172800.png)

国际技术标准：[ETSI TS 103 162 V1.1.1](https://www.etsi.org/deliver/etsi_ts/103100_103199/103162/01.01.01_60/ts_103162v010101p.pdf)

![Pasted image 20250527172101](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250527172101.png)

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
![Pasted image 20250527172349](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250527172349.png)


# Thur, May 29

#### SCA_cg code review

##### debug

> 发现存在 bug，目前仿真无法跑完

针对发现的 bug，查看波形发现：
载入 EK1 的时候显示 key_valid 拉低，是由 LCS 处于 dr 导致
因此在 case 目录内部附加 flash_otp.txt 设置 LCS 未 CM
仅设置 LSC 后发现 rd_equ 对比不通过
在 flash_otp.txt 中设置 key 为 8‘hffffffff，对比通过。
在 case 中添加备注：

```
SCA BUG
LCS must be set as CM(data in flash set as 3'b111),otherwise EK will not be loaded.
Internal KEY should be set as 0(data in flash set as 8'hffffffff),otherwise rd_equ check will fail.
```

##### 完成进度

- host_0
  - cmd_fifo
    - sca_regfile
- mgr


# Fri, May 30

#### 周会

#### 支持 FPGA 进行 OTP 调试

支持 flash 写入相关问题
支持 ACA，SCA 理解方面问题

#### SCA_cg code review

- host_0
  - cmd_fifo
    - sca_regfile
- mgr
  - dmain_intf




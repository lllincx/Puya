#### 待写入入口寄存器的数据内容

operand_a: GRID O
operand_b: GRID P
operand_c: GRID Q
operand_r: GRID R
len_type_id: len_type_S

#### 通用寄存器或长度类型寄存器的数据内容

GR O: addr w，待计算的数据 A 所在的 sram 首地址
GR P: addr x ，待计算的数据 B 所在的 sram 首地址
GR C: addr y ，待计算的数据 C 所在的 sram 首地址
GR R: addr z ，计算的结果数据 R 所在的 sram 首地址
len_type_S: 数据 L，待计算的数据 A、B、C 的长度

#### Operand a, b, c, r 的关系

对一般运算操作，数据 R 为数据 A，数据 B 运算的结果，不使用数据 C
仅对模乘加（Modular Multiplication and Accumulation，modMULACC），免约减模乘加（Modular Multiplication and Accumulation without reduction，modMULACCNR）来说，数据 R 为数据 A，数据 B，数据 C 运算的结果。

$$
\begin{align}
modMULACC:R  &= (A\times B+C)\ mod\ n\\
modMULACCNR:R  &= A\times B+C
\end{align}
$$

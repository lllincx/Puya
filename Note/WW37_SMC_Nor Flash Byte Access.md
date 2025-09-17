**SMC Nor Flash Byte访问总结**
### 摘要

**问题**：FPGA 反馈 Nor Flash 在 **byte 模式读写异常**；ASIC 仿真验证，**写正常、读异常**。
**原因**：Q[15] 被当作地址 A[-1]，但高 8 位输出高阻。
**方案**：
	**最小修改**：固定Q[15]为 0，舍弃一半空间，改动小。
	**最终方案**：A0 接数据高位，其他地址右移，更符合 spec，但 FPGA 需大量跳线。
**结果**：两种方案仿真都通过；FPGA 已用最小修改方案解决。
**待确认**：是否接受 **最小修改方案**作为最终结果，还是要求 FPGA 重新布线测试。

### 1. FPGA 反馈情况

蔡紫阳反馈 nor flash 以 byte 为单位的读写存在问题。

### 2. ASIC 仿真结果

nor flash byte 写正常。byte 读时，数据线异常。

### 3. 异常定位

nor flash 以 byte 模式读写时，数据位的最高位 Q[15]作为地址的 -1 位，寻址字地址的高 byte 或低 byte，即：
NorAddr[26:0]={A[25:0], Q[15]}
数据位的高 8 位被输出为高阻，因此读取数据异常。

### 4. 解决方案

#### 4.1 理论解决方案及其限制

增加地址引脚分配 FMC_A-1，与 FMC_A0~25 共同构成 27 位字节地址。
由于目前新增输入引脚变动较大，因此需采用 byte 模式下，放弃一半存储空间的方式。

---

#### 4.2 最小修改解决方案

> 本着最小修改的原则，我首先采用以下解决方式：

**解决方式**：在 byte 模式下，将数据线最高位固定接 0，即：NorAddr[26:0]={FMC_A[25:0],1'b0}
**地址取舍**：舍弃所有字地址的高 Byte。
**flash端口含义:**
A 端口数据为字地址，A 端口数据左移一位为字节地址。
Q 端口数据为输出数据。
![image.png|700](https://raw.githubusercontent.com/lllincx/IMG/master/20250908144707717.png)

**修改内容**
![image.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250908150859932.png)

**实现代价**
![Snipaste_2025-09-08_15-27-09.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/Snipaste_2025-09-08_15-27-09.png)

---

#### 4.3 最终解决方案

> 本着更接近 nor flash spec 描述的意图，郭老师建议我应用以下修改：

**解决方式**：在 byte 模式下，将 FMC_A0 线接入 nor flash 数据位高位，其他地址线依次右移接入 nor flash 地址线，高位补 0，即：NorAddr[26:0]={1'b0,FMC_A[25:0]}
**地址取舍**：舍弃最高位地址为 1 的所有地址。
**flash端口含义:**
A 端口数据为字地址，【A 端口数据+Q 端口高位】为字节地址。
Q 端口数据忽略高位为输出数据

![image.png|700](https://raw.githubusercontent.com/lllincx/IMG/master/20250908145328588.png)

**修改内容**
![image.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250908150117736.png)

**实现代价**
![Snipaste_2025-09-08_15-27-37.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/Snipaste_2025-09-08_15-27-37.png)

### 5. 结果

两种解决方案实施后，仿真均通过，同时 word 访问未受影响。两种方案均上传 git。

![Snipaste_2025-09-08_15-30-51.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/Snipaste_2025-09-08_15-30-51.png)

### 6. 对 FPGA 的指示

蔡紫阳称，最终修改方案需要跳接的引线过多，比较难以实施。并且在两种访问方式切换后均需要全部更换，实现代价较高。

蔡紫阳自行临时采用了【最小修改解决方案】，成功实现Byte模式读写，是否可以视为该问题已经解决。或者还是需要求他们按照最终方案重新接线测试？




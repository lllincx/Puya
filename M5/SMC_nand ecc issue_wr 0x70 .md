### err condition

- mem: nand
- ecc: on
- ecc_mode: 0x10
- mem busy status get method: wr 0x70 to mem to get status

### mem busy status get method:

 1. polling
 2. intr
 3. wr 0x70 to mem to get status

![image-20260528102514831](https://pic.lllincx.cn/image-20260528102514831.png)

### 写0x70读存储器状态原因

AE之所以采用写0x70模式，原因是ST的库普遍采取这种方式，但==ST并不支持我们出问题的这种ecc_mode==。

### 写0x70读存储器状态的返回

读取存储器状态后，为了返回读数据状态需要写0x00返回。但存储器文档中写的是（为了返回普通读模式），有可能==含ecc功能的读模式不属于文档中讲到的读模式，所以不应写0x00命令。==

### ecc_mode介绍

ecc_mode: 0x10的特点：在存储器接口上，读block n后，==硬件自动写读取ecc值的命令==，硬件自动读取ecc值。

ecc_mode: 0x01的特点：在存储器接口上不存在写读取ecc值的命令。

### Coding

- 编写case，在普通读模式下，写0x70读存储器状态成功
- 编写case，复现err

![image-20260528105559926](https://pic.lllincx.cn/image-20260528105559926.png)

### 波形现象

有reg表示smc发出数据的周期长度，如果是发送命令，周期长度应为5。在发送0x00后，reg数值变更为2，导致写读取ecc值的命令无法发送成功。

### 结论

写「0x70读存储器状态」，并「写0x00返回普通读模式」打断了ecc_mode: 0x10条件下，ecc读模式下在读取block数据中穿插「硬件写读取ecc值的命令」的完整流程。ecc_mode: 0x01条件下，不存在「硬件写读取ecc值的命令」情况，因此不受影响。
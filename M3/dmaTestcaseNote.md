结构体成员信号的 trace：目前发现只有通过 string 查找可以。
结构体类型声明位置：
`/testbench/shared/common_lib/Include/ada_dma_command_lib.h`
函数声明位置：
`/testbench/shared/common_lib/ada_dma_command_lib.c`

### config_check_ext_feat case

![image.png|800](https://pic.lllincx.cn/20260210094055695.png)

- 读写地址每 80h 增加，分析原因为一整行读写完毕，增加`ystride`大小。
- **问题**：在一行数据的读写范围内，`araddr`理应增加，但是实际未增加。
- 可能导致问题的原因是`xsize`的大小为 200h，但`ystride`对应的行间距仅为 80h。

  ![image.png|600](https://pic.lllincx.cn/20260210095835799.png)

- 一次`araddr`突发传输对应 16 次`rdata`无误。只是 16 次`rdata`数据一样。
- 配置突发长度为 3，读写地址依旧是 80h 增加。

---

读`CH_STATUS`寄存器的`STAT_RESUMEWAIT`位，直到为 1。
写`CH_STATUS`寄存器的所有`W1C`位
写`CH_CMD`寄存器的`RESUMECMD`位

---

msc 报 irq 会拉低`ch_enable`在此之后写`ch_cmd`不会生效。

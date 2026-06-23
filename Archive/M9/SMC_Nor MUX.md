根据目前 case 的输出波形，对 nor flash 来说，在数据传输阶段 syscfg16 开启与否不会影响传输结果。

> **AWSIZE**：定义单次传输（beat）的数据宽度，以字节为单位的对数（即 `AWSIZE=2` 表示一次传输 2^2 = **4 字节**）。
> **WSTRB**：写选通信号（Write Strobe），每个比特对应写数据总线 `WDATA` 上的一个字节。值为 `1` 表示该字节有效，需要写入；值为 `0` 表示该字节无效，不会写入。

### 理想情况

从 AXI 总线发出的命令：
`AWSIZE = 2` → 每次传输宽度是 **4 字节 (32bit)**；
`WSTRB = 4` → 即 `WSTRB = 4'b0100`。
理想情况下，应当：

- 传输的单位仍然是 **4 字节宽**；
- 但是 WSTRB 只使能第三高字节，其余 3 个字节被屏蔽掉；
- 结果就是：总线发出一个 32bit 的写数据，但 **只有[23:16]bit 会真正写入存储器，其余 24bit 不会更新**。

### SMC 情况

SMC 内部不按字节利用 axi 总线提供的 wstrb 信号，而是或在一起使用，进而无法实现只编程 1 字节的目的。

![image.png](https://pic.lllincx.cn/20250926112611530.png)

![image.png](https://pic.lllincx.cn/20250926144033510.png)

为此需要在 axi 指令输入 SMC 前将 awsize MUX 为 0，即每次传输宽度为 1 字节（8bit）

### 实测波形
`syscfg16=1`

![image.png](https://pic.lllincx.cn/20250926155317272.png)

![image.png|600](https://pic.lllincx.cn/20250926155321198.png)

![image.png|600](https://pic.lllincx.cn/20250926155328349.png)

`syscfg16=0`

![image.png](https://pic.lllincx.cn/20250926155821601.png)

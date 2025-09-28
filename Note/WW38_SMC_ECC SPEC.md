## ST

FMC NAND 卡控制器包括两个纠错码计算硬件模块，每个存储区域有一个。这些模块可在软件处理 ECC 时减少主机 CPU 工作负载。  
这两个 ECC 模块相同，分别与存储区域 2 和存储区域 3 相关联。因此，与存储区域 4 连接的内存没有可用的硬件 ECC 计算。  
对 NAND Flash 执行读取或写入操作时，相应每 256、512、1024、2048、4096 或 8192 个字节，FMC 中使用的 ECC 算法可修正 1 位错误并且检测出 2 位错误。该操作基于 Hamming 编码算法，并且包括计算行和列奇偶校验。  
每当 NAND Flash 存储区域处于激活状态时，ECC 模块均会监视 NAND Flash 数据总线和读/写信号（NCE 和 NWE）。

ECC 的操作如下：  
• 当访问 NAND Flash 存储区域 2 或存储区域 3 时，将锁存 D[15:0] 总线上出现的数据并将其用于 ECC 计算。  
• 当访问 NAND Flash 中的任何其他地址时，ECC 逻辑会进入空闲状态，不执行任何操作。因此，进行 ECC 计算时，用于定义 NAND Flash 命令或地址的写操作无效。

主机 CPU 对 NAND Flash 完成所需字节数的读取/写入操作后，必须读取 FMC_ECCR 寄存器，才能检索计算出的值。读取后，应通过将 ECCEN 位复位为 0 来将这些寄存器清零。要计算新的数据块，必须将 FMC_PCR 寄存器中的 ECCEN 位置 1。

要进行 ECC 计算：
1. 使能 FMC_PCR 寄存器中的 ECCEN 位。
2. 将数据写入 NAND Flash 页。在写入 NAND 页期间，ECC 模块将计算 ECC 值。
3. 读取 FMC_ECCR 寄存器中所提供的 ECC 值，并将其存储到变量。
4. 将 FMC_PCR 寄存器中的 ECCEN 位清零后使能，然后从 NAND 页回读写入的数据。在读取 NAND 页期间，ECC 模块将计算 ECC 值。
5. 读取 FMC_ECCR 寄存器中所提供的新 ECC 值。
6. 如果两次读取的 ECC 值相同，则无需校正，否则说明存在 ECC 错误，并且软件校正例程将返回有关该错误是否能够得到校正的信息。

## SMC ECC

- 配置ecc_memcfg, ecc_commend 寄存器
	- 根据使用的nand flash的ecc指令，配置ecc_memcommand1, ecc_memcommand2寄存器，对通用nand flash，保持默认值即可。
	- 配置ecc_memcfg寄存器中的ecc_mode。
	- 根据nand flash的大小配置ecc_memcfg寄存器中的page_size位。
	- 根据nand flash每个page extra block的大小配置ecc_memcfg寄存器中的ecc_extra_block, ecc_extra_block_size 位。
将数据写入 NAND Flash 页。在写入 NAND 页期间，ECC 模块将计算 ECC 值，并将ecc值存入extra block。ecc值也可以通过对应block的ecc_value[n]寄存器读出。

从nand flash回读写入的数据时，读取期间ECC模块将计算ECC值，并与存储在extra block的已经存入的ecc值比较。比较结果可通过ecc_status寄存器查看。
1. pt105增加端口：`fmc_data_en`，N6未提及。
2. pt105端口冗余：
	1. `fmc_ba0/1`，已经包含在`fmc_a`中。
	2. `fmc_lb, fmc_ub`，已经包含在`fmc_nbl`中。
3. 数据总线差异：
	1. PT105为16位，N6为32位。增加32位sram，sdram支持。
	2. PT105分读写数据总线，N6不分。
4. 通用控制差异：
	1. PT105`NE,NBL`为一位，N6为四位。
	2. PT105 nand的`nand_busy_o`信号合在`NWAIT`信号中，N6 nand 的`NAND_RNB`与`NWAIT`独立。
	3. PT105 sram的`sram_clk_out_o`与sdram的`dmc_hclk`合并于`fmc_clk`。N6则分别对应`FMC_CLK,FMC_SDCLK`。
5. N6增加器件支持：16bit-multiplesed sram，配置了`AD`总线。
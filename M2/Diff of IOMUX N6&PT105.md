|           | **PT105**       |                 |                        |                     | **N6**             |                  |                    |                      |
| --------- | --------------- | --------------- | ---------------------- | ------------------- | ------------------ | ---------------- | ------------------ | -------------------- |
|           | **FMC**         | **SRAM**        | **NAND**               | **SDRAM**           | **FMC**            | **SRAM**         | **NAND**           | **SDRAM**            |
| **a**     | **fmc_a**       | sram_add_i      | nand_ale_i, nand_cle_i | s_bank_addr, s_addr | **FMC_A[25:0]**    | SRAM_A[25:0]{2}  | NAND_ALE, NAND_CLE | S_BA[1:0], S_A[13:0] |
|           | ~~**fmc_ba0**~~ |                 |                        | s_bank_addr[0]      |                    |                  |                    |                      |
|           | ~~**fmc_ba1**~~ |                 |                        | s_bank_addr[1]      |                    |                  |                    |                      |
| **d**     | **fmc_wdata**   | sram_data_out_i | nand_data_out_i        | s_wr_data           | **FMC_D[31:0]**    | SRAM_D[31:0]{3}  | NAND_D[15:0]{4}    | S_D[31:0]            |
|           | **fmc_rdata**   | sram_data_in_o  | nand_data_in_o         | s_rd_data           |                    |                  |                    |                      |
| **nce**   | **fmc_nce**     |                 | nand_cs_n_i            |                     | **FMC_NCE**        |                  | NAND_NCE           |                      |
| **ne**    | **fmc_ne**      | sram_cs_n_i     |                        |                     | **FMC_NE[4:1]**    | SRAM_NE[x], 1~4  |                    |                      |
| **noe**   | **fmc_noe**     | sram_oe_n_i     | nand_re_n_i            |                     | **FMC_NOE**        | SRAM_NOE         | NAND_NOE           |                      |
| **nwe**   | **fmc_nwe**     | sram_we_n_i     | nand_we_n_i            |                     | **FMC_NWE**        | SRAM_NWE         | NAND_NWE           |                      |
| **nwait** | **fmc_nwait**   | sram_wait_o     | nand_busy_o            |                     | **FMC_NWAIT**      | SRAM_NWAIT       |                    |                      |
|           |                 |                 |                        |                     | **FMC_RNB**        |                  | NAND_RNB           |                      |
| **nbl**   | **fmc_nbl**     | sram_bls_n_i    |                        | s_dqm               | **FMC_NBL[3:0]**   | SRAM_NBL[3:0]{1} |                    | S_NBL[3:0]           |
| **nadv**  | **fmc_nadv**    | sram_adv_n_i    |                        |                     | **FMC_NADV**       | SRAM_NADV        |                    |                      |
| **clk**   | **fmc_clk**     | sram_clk_out_o  |                        | dmc_hclk            | **FMC_CLK**        | SRAM_CLK         |                    |                      |
|           |                 |                 |                        |                     | **FMC_SDCLK**      |                  |                    | S_SDCLK              |
| **sdnwe** | **fmc_sdnwe**   |                 |                        | s_we_n              | **FMC_SDNWE**      |                  |                    | S_SDNWE              |
| **cke**   | **fmc_cke**     |                 |                        | s_cke               | **FMC_SDCKE[1:0]** |                  |                    | S_SDCKE[1:0]         |
| **sdne**  | **fmc_sdne**    |                 |                        | s_sel_n             | **FMC_SDNE[1:0]**  |                  |                    | S_SDNE[1:0]          |
| **nras**  | **fmc_nras**    |                 |                        | s_ras_n             | **FMC_NRAS**       |                  |                    | S_NRAS               |
| **ncas**  | **fmc_ncas**    |                 |                        | s_cas_n             | **FMC_NCAS**       |                  |                    | S_NCAS               |
| **en**    | ==fmc_data_en== | sram_data_en_i  | nand_data_en_i         | s_dout_valid        |                    |                  |                    |                      |
| **lb**    | ~~**fmc_lb**~~  | sram_bls_n_i[0] |                        |                     |                    |                  |                    |                      |
| **ub**    | ~~**fmc_ub**~~  | sram_bls_n_i[1] |                        |                     |                    |                  |                    |                      |
1. 限PSRAM/SRAM/FRAM，nor无NBL
2. 限non-multiplexed，16bit-multiplexed接SRAM_A[25:16]，SRAM_AD[15:0]
3. 限non-multiplexed，16bit-multiplexed接SRAM_AD[15:0]
4. 限16bit，8bit接NAND_D[7:0]

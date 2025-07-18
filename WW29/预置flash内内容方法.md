![image.png|1000](https://raw.githubusercontent.com/lllincx/IMG/master/20250717101739613.png)

1. 在 ASIC SIM 下跑使用 flash_otp.txt 预置 flash 内容的 case，将`PRODUCT_MCU/PT105/V1/_digital/thzhou/ws1/fpga/rtl/flash_info.mem`文件复制到本地`PRODUCT_MCU/PT105/V1/_gitview/lincx/pt105_soc_v1/`。
2. 修改`PRODUCT_MCU/PT105/V1/_gitview/lincx/pt105_init/pt105_soc_v1/fpga/rtl/FPGA_MEM.v`中 28 行，替换为`PRODUCT_MCU/PT105/V1/_gitview/lincx/pt105_soc_v1/`。
3. 在 config.vh 中注释 DUBHE 和 SRAM。

> 有疑问可咨询伟彬

1. host0仅可访问 SRAM 低 8KByte空间，host1仅可访问 SRAM 高 8KByte空间，请按照以下要求充分验证。

1. 第1步，先写地址0到sram_waddr 寄存器，只写1次；
2. 第2步，写数据到sram_wdata寄存器，由于地址会自增，连续写2048次；
3. 第3步，先写地址0到sram_raddr 寄存器，只写1次；
4. 第4步，读sram_wdata寄存器，由于地址会自增，连续读2048次进行数据比对；
5. 为了实现对所有host 的ACA SRAM的验证，那么需要按照以上四点操作每个host的 sram_waddr 和 sram_wdata, sram_raddr和sram_rdata的寄存器。

Table B1-104-107
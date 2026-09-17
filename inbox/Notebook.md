## Note

**testcase temp gen**

```shell
gen_temp tb --name=$module
gen_temp tc --name=$module/$case
```

## TODO

### pvtc



测试发现存在其他条件一致。AXI总线上实际burst length更小，实际传输速度更快的现象



因此我有两个问题：

以下三者对DMA的实际传输效率的影响

FIFO深度

AXI总线上实际burst length

寄存器中maxburst配置。



在实际使用过程中为实现更高的传输效率，maxburst应如何配置，是否需要配合fifo深度配置

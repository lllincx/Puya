# SWD读取问题

28日讨论希望更改Direct_CMD REG 中CMD_type位复位值，但该寄存器为只写，复位值难以修改。详情见图片。

# Byte读取问题

目前asic仿真，fpga仿真结果与上机测试同样，nor flash在接收到指定序列之后，不产生中断。我认为该结果说明smc功能上没有问题，而是mem存在问题。

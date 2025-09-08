# WW31周报

出具TrustEngine，SMC模块的Notiming List
基于newbus的TrustEngine和SMC测试均通过
学习项目安全启动方案

开发SMC nand 跨Page边界读写case
单个page具有0x420个字的地址范围，从0x400地址连续写0x40个数，并回读。前0x20个字与写入数据符合，后0x20个字与写入数据不符合。下一个page的数据内容也没有改变。

支持FPGA同事：
了解address match 与address mask，等SMC相关问题
在TrustEngine方面各子模块问题包括SCA的Process命令中：last proc仅在cmac 模式下起效，需要计算CMAC长度，不包括结束回话的指令。
与陈老师讨论：LCS可写功能比较有必要，LCS功能可以和OTA一起做。

深入学习smc SPEC，充分了解以下配置：
- Cycle寄存器
- Opmode寄存器
- SRAM接口时序
- NAND接口时序
- ECC 操作


# 7月28日 星期一


出具TrustEngine，SMC模块的Notiming List
继续dbg SMC nand 跨边界存储问题

# 7月29日 星期二


支持软件同事对nand 片选配置理解

开发cross broundary case

![image.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250729151109159.png)

单个page具有0x420个字的地址范围，从0x400地址连续写0x40个数，并回读。前0x20个字与写入数据符合，后0x20个字与写入数据不符合。下一个page的数据内容也没有改变。

尝试newbus跑case
学习安全启动

# 7月30日 星期三


学习安全启动
Newbus 测试均通过
学习SMC
支持软件同事关于SMC相关问题

# 7月31日 星期四


深入学习smc SPEC，充分了解以下配置：
- Cycle寄存器
- Opmode寄存器
- SRAM接口时序

支持软件部门在TrustEngine方面各子模块问题，包括：
last proc在cmac 模式下起效，需要计算CMAC长度
dubhe_sca_mgr.v
![image.png|600](https://raw.githubusercontent.com/lllincx/IMG/master/20250731162759458.png)
LCS可写功能比较有必要，LCS功能可以和OTA一起做。




# 8月1日 星期五

深入学习 smc SPEC，充分了解以下配置：

- NAND 接口时序
- ECC 操作



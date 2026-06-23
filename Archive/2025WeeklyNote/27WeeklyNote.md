# WW27周报

nor flash fpga model 连接
- nor flash fpga model 连接 debug
- 与之匹配修改case，
- 协助同事完成DMC model 连接

与fpga同事交流otp uart问题。
与fpga同事交流smc fpga 头文件不包含 syscfg 问题。

修改地址msk与mtch值错配问题，并设置为syscfg配置。验证通过并上传。
支持DFT，为SMC添加scan clk、mode mux。验证通过并上传。

用新生成的bitfile进行测试并抓取信号。
> - 读取成功，但写失败，仍存在一次片选有效对应两次写使能有效的现象。
> - 确认在fpga仿真阶段。syscfg有效时，一次片选有效对应两次读使能有效，一次片选有效对应一次写使能有效，仿真结果正确。syscfg无效时，一次片选有效对应两次读使能有效，一次片选有效对应两次写使能有效，仿真结果错误。

与宇波讨论smc syscfg16不起作用导致写失败问题，并汇报张老师。

> 纠正fpga同事介绍的“一次片选有效对应多次读使能有效会导致错误问题”。
> 实际情况是写操作需要向nor flash写入多个8位的数据，对应axi总线上的awsize应为0。但m52只支持进行32位数据的发送，对应axi总线上的asize会为2。这将导致nor flash无法识别。
> 例如，nor flash期待向0x55地址写入0xaa数据。CPU发出的命令被nor flash介绍到的将为：向0x54写入0x00，向0x55写入0xaa。与命令格式不匹配，写入失败。
> 为解决此问题，添加syscfg16，对CPU发来的信号将进行mux，将awsize转变为0。
> 
> debug建议：
> 1. 探针测试awsize位，看是否被msk掉。
> 2. 仿真结果无误，网表测试存在问题。考虑单独综合smc。

# 6月30日 星期一


## fpga 进度同步会议

- smc 先进行fpga仿真，fpga验证优先级放低
- TrustEngine SM4 软件包不包含，因此没有验证

## nor flash fpga model 连接

- nor flash fpga model 连接
- nor flash fpga case 修改
- nor flash fpga dbg


# 7月1日 星期二


[[Nor Flash FPGA DBG]]
1~4.5

# 7月2日 星期三


## 支持 FPGA

- TrustEngine fpga otp uart 问题
- smc fpga 头文件不包含 syscfg 问题

## SMC

**FPGA Sim**

- [[Nor Flash FPGA DBG]] 4.5~6

修改地址msk与mtch值错配问题，并设置为syscfg配置

支持DFT，为SMC添加scan clk、mode mux


# 7月3日 星期四



支持DFT，为SMC添加scan clk、mode mux。验证通过并上传。
修改地址msk与mtch值错配问题，并设置为syscfg配置工作完成，验证通过并上传
用新生成的bitfile进行测试并抓取信号。
- 读取成功，但写失败，仍存在一次片选有效对应两次写使能有效的现象。
- 确认在fpga仿真阶段。syscfg有效时，一次片选有效对应两次读使能有效，一次片选有效对应一次写使能有效，仿真结果正确。syscfg无效时，一次片选有效对应两次读使能有效，一次片选有效对应两次写使能有效，仿真结果错误。

# 7月4日 星期五


与宇波讨论smc syscfg16不起作用导致写失败问题，并汇报张老师。

纠正fpga同事介绍的“一次片选有效对应多次读使能有效会导致错误问题”。
实际情况是写操作需要向nor flash写入多个8位的数据，对应axi总线上的awsize应为0。但m52只支持进行32位数据的发送，对应axi总线上的asize会为2。这将导致nor flash无法识别。
例如，nor flash期待向0x55地址写入0xaa数据。CPU发出的命令被nor flash介绍到的将为：向0x54写入0x00，向0x55写入0xaa。与命令格式不匹配，写入失败。
为解决此问题，添加syscfg16，对CPU发来的信号将进行mux，将awsize转变为0。

debug建议：
1. 探针测试awsize位，看是否被msk掉。
2. 仿真结果无误，网表测试存在问题。考虑单独综合smc。


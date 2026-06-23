# Mon, June 9


完成绝大多数 TrustEngine case 更新

# Tues, June 10


#### 完成全部 TrustEngine case 更新并汇报

[[TrustEngine case update report]]

#### 移植多存储种类 case

未跑通

#### 时擎交接

检查提供的 case 是否可以跑通

| case name            | 符合预期 | 移植完毕 |
| -------------------- | -------- | -------- |
| sh abnormal_ahb_test | 1        | 1        |
| sh abnormal_apb_test | 1        | 1        |
| sh_aca_cg_test       | 1        | 1        |
| sh_hash_cg_test      | 0        | 1        |
| sh_lcs_func_test     | 1        | 1        |
| sh_mem_access_test   | 1        | 1        |
| sh_otp_access_test   | 1        | 1        |

#### 支持软件

otp_init_value 问题解决

![65b60e89e2f4717389d1990ae771ae08](https://pic.lllincx.cn/65b60e89e2f4717389d1990ae771ae08.png)
```
otp init value access begin
493d0010
otp init value=l
```
转告 otp flash 写入方法
准备新 case 供使用


# Wed, June 11

#### 时擎交接

完成全部 case 检查

[[Fri, June 13 时擎交接 会议记录]]

#### FPGA 学习

#### 支持软件

宏实现方式介绍

#### FPGA sim DBG

中断结束之后，不会返回主程序


# Thur, June 12

#### 周会

七月中旬:RTL2.0
月底之前完成 SPEC 补全，参照 ST

#### FPGA sim DBG

中断结束之后，不会返回主程序
debug fpga sim 过程中，发现之前的 case 中断程序写的有问题，花费一天时间改正
中断问题改正之后，仍然存在写源地址命令，cmd_intr 异常



# Fri, June 13

#### 工作安排

1. axi_sram 支持
2. 看系统层面使用 shanhai ，和其他 IP 合作的文档，安全启动等
#### Shanhai 交接

##### 会议内容

[[Fri, June 13 时擎交接 会议记录]]

trng 可以在 default/cfg 中添加 define

##### 后续工作

1. 跑 trng 并移植
2. 跑多存储类型并移植

#### FPGA sim

环境跑不通，等待修改

#### case intr DBG

修正中断函数 bug
添加函数

#### 支持软件

推新 case 供测试



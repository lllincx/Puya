#daily

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

![65b60e89e2f4717389d1990ae771ae08](https://raw.githubusercontent.com/lllincx/IMG/master/65b60e89e2f4717389d1990ae771ae08.png)
```
otp init value access begin
493d0010
otp init value=l
```
转告 otp flash 写入方法
准备新 case 供使用

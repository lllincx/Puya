#### SCA_cg code review

##### debug

> 发现存在 bug，目前仿真无法跑完

针对发现的 bug，查看波形发现：
载入 EK1 的时候显示 key_valid 拉低，是由 LCS 处于 dr 导致
因此在 case 目录内部附加 flash_otp.txt 设置 LCS 未 CM
仅设置 LSC 后发现 rd_equ 对比不通过
在 flash_otp.txt 中设置 key 为 8‘hffffffff，对比通过。
在 case 中添加备注：

```
SCA BUG
LCS must be set as CM(data in flash set as 3'b111),otherwise EK will not be loaded.
Internal KEY should be set as 0(data in flash set as 8'hffffffff),otherwise rd_equ check will fail.
```

##### 完成进度

- host_0
  - cmd_fifo
    - sca_regfile
- mgr

### TrustEngine

#### Mem_access DBG

##### bug情况

只能进行一次读写，第二次读写会fail

##### 前期忽略原因

case读写数据较多，以为是需要仿真时间过长，于是手动中断

##### 排查与解决

rdata为X态，由raddr指向高位导致（高位未写数据）
原因未raddr一次读写后未归零
在VIM中复制错误导致，未仔细检查

#### OTP access Code Review

40%
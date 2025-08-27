# Wed, May 8

### TrustEngine

移植 tc_c_trng，并排查问题


![[TRNG 问题及排查过程]]


# Thur, May 9

### TrustEngine

#### 移植tc_c_ahb

移植中断服务函数
实现采用dly方式等待中断发生
完成v1.0


# Fri, May 10

### 周会

### TrustEngine

#### 移植 tc_c_ahb

丰富中断服务函数，采用中断计数方式区分多次进入中断后执行的不同程序
解决需要通过实验方式确定延时时间的问题
完成 v2.1，输出结果验证匹配

#### 移植 tc_c_hash

与 ahb 完全相同

#### 移植 tc_c_sca



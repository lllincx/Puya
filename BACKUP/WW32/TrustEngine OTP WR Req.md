### 第一优先级：

#### LCS

大小：4bits
典型值：32bits
收益：在 CM、DM 阶段，授权读取秘钥信息

#### FOTA version (User secure region)

大小：IMPLEMENTATION DEFINED
典型值：32bits
收益：FOTA 功能必需

### 第二优先级：

#### Recovery mainfest version (User secure region) & Primary mainfest versinon (User secure region)

大小：IMPLEMENTATION DEFINED × 2
典型值：32bits × 2
收益：Secure boot (Shanhai) 功能必需
说明：The manifest version for the primary (recovery) boot path. Used for anti-rollback.

#### OTP Lock Ctrl

大小：32bits
收益：OTP 锁定

### 第三优先级

#### 其他 User secure region、User non-secure region、Test region
收益：在 DD 阶段，可供用户读写

### 第四优先级

#### 所有 OTP 区域内容

收益：在 CM、DM 阶段，可多次读写配置内容

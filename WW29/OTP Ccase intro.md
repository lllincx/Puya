### py32f537_te_func.h

**4：** IP 基地址
**30-36：** OTP 管理及 OTP 空间地址

### py32f537_te_func.c

**2：** dubhe_init，IP 初始化，CLK 和 RST 置位复位
**89：** pt_otp_init_val，打印 otp 空间初始值
**72：** pt_lcs，打印生命周期
**18：** chk_cnt，addr 内数据的值与 exp 不符返回 1，否则返回 0。
**32：** otp_wr_ctrl，通过 IP 写 OTP 空间
**38：** otp_reset，重置 OTP 子模块

### case 描述

lcs：通过写 lcs 控制位，单向改变 lcs
otp_access：通过 IP，读写 otp 空间
otp_rdck：在 flash 中预置数据，通过 IP 读取并与预期比较。

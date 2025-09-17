###### tc_c_otp_access case简介

配置 otp manger 寄存器并运行
otp space 的指定地址被写入指定数据
读取制定地址的数据

##### 现象

读取到的数据恒定为 0xffffffff，与预期不符
otp manger 寄存器读写正常
otp space 读正常
otp space 无法写入

##### 原因排查过程

otp_top/otp_arb/otp_update_fail 被拉高（该信息可以通过 otp_update_state REG 读出）
otp_update_fail 主要受./otp_acc_ack (otp_top/otp_sec_chk/otp_acc_ack_s)影响
otp_acc_ack_s 在 ./c_state 为 ERR 状态时被置位
在 IDLE 状态下，./sec_chk_fail 有效时跳转到 ERR 状态
sec_chk_fail 由./hit_mid (地址选中) & ./sec_chk_fail_mid 置位
./lcs_is_dr 状态下，有读写操作（./otp_acc_wr_s），均将置位 sec_chk_fail_mid
lcs_is_dr为otp_top/otp_lcs_mgr/shadow_lcs的低三位
shadow_lcs在./c_state处于LOAD_LCS状态下由./otp_acc_rdata_int写入otp_acc_rdata_int当./otp_apt_mst/c_state为P_ACCESS状态 并且 ./n_state为RESP状态时由./prdata_int写入
prdata_int收到参数DUBHE_OTP_INIT_VALUE影响，默认为1，此时OTP各种参数均被置1，LCS为DR状态，无法写入




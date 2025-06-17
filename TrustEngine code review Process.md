###### apb

###### reg access

###### mem access

###### otp

- regfile
- arb
  `r_otp_wr_trig`在`OTP WR REG`写 1 之后触发
  `otp_wr_busy` 在`r_otp_wr_trig`触发之后拉高，在`otp_acc_ack`到来之后拉低
  `otp_wr_req=r_otp_wr_trig|otp_wr_busy`
- sec_chk
- lcs_mgr
  - apb_mst

###### sca

计算模块没有看

- host_0
  - cmd_fifo
    - sca_regfile
- mgr
  - dmain_intf
  - dmaout_intf
  - ~~calc_core~~
###### hash
- host_0
	- regfile
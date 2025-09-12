## apb

## reg access

## mem access

## otp

- regfile
- arb
  `r_otp_wr_trig`在`OTP WR REG`写 1 之后触发
  `otp_wr_busy` 在`r_otp_wr_trig`触发之后拉高，在`otp_acc_ack`到来之后拉低
  `otp_wr_req=r_otp_wr_trig|otp_wr_busy`
- sec_chk
- lcs_mgr
  - apb_mst

## sca

计算模块没有看

- host_0
  - cmd_fifo
    - sca_regfile
- mgr
  - dmain_intf
  - dmaout_intf
  - ~~calc_core~~

## hash

- host_0
  - regfile

## trng

- regfile
- pool0_regfile
- arbit_ctrl
  主要用于多主机，略看
- ctrl
- entropy_src
  - group_chain_0
    f_ro_en, loop_mux_sel, rr_cnt 等 reg 与环形振荡器配置强相关，没有具体理解
    - ~~g_1~~
- sampling
- pp
	- ~~vn_collector
	- lfsr
	- s2p
	- ~~crng_test
- rn_pool
- ~~eval
- ~~autocorr
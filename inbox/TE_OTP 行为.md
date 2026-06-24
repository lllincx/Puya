数据： model_id、model_key、device_id、device_root_key、LCS、lock_ctrl

敏感数据：model_key,device_root_key,user_sec_region

1. TE-200自定义的OTP region 需要保留，其中reserved空间也需要保留。
2. 写入后回读更新寄存器：若通过 TE-200 写入数据，写入完成后 TE-200 会回读并更新内部寄存器。
3. OTP上电初始化：上电后TE-200硬件主动发起对数据的读操作并保存到内部寄存器。
4. 当LCS一旦进入到DR阶段，TE-200 硬件会主动发起对敏感数据写全1擦除，擦除完成后将LCS bit3 写1作为擦除完成的flag。
5. TE-200 上电之后若读取到的LCS 的状态为DR且 LCS [3] = 1’b0（写擦除是否完成的flag），代表TE-200在上一个power cycle 敏感数据写擦除未完成，因此又会重新发起写擦除。
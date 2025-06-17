## 关于 5 月 26 日会议中强调的 ASIC 与 FPGA 参数不匹配的问题

### 问题背景：

软件同事测试结果显示，fpga 仿真环境的 `DUBHE_OTP_INIT_VALUE` 参数定义与 ASIC 不一致。

### 解决方案：

`DUBHE_OTP_INIT_VALUE`参数定义在文件 `……/pt105_soc_v1/ip/soc/TrustEn200/rtl/inc/dubhe_top_cfg.vh` 中

因此需将 `fpga_flist.f` 中 68+6 行中引用的文件同步至`fpga_sim_flist.f` 中

我现在暂无该文件的编辑权限，如需解决该问题，请安排有权限的同事按以上方案修改。

完成以上修改之后，我们再看【**otp 本该无法写入，fpga 仿真结果显示可以写入**】的问题是否仍旧存在。

![[Pasted image 20250527142158.png]]

---

#### ASIC 参数定义位置

```
pt105_soc_v1/asic/rtl/top_list
68:-f $IP/soc/TrustEn200/dubhe_top.f
1:+incdir+$SOC_IP/TrustEn200/rtl/inc
dubhe_top_cfg.vh
42:parameter DUBHE_OTP_INIT_VALUE

```

#### FPGA 引用文件位置

```
pt105_soc_v1/fpga/fpga_flist.f & fpga_sim_flist.f
```

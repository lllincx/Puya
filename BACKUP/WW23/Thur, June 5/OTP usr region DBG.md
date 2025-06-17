#### case 介绍

![[Pasted image 20250605151651.png]]
路径：`/SOC_PT105_VERIFY/tc/tc/tc_c_otp_usrrg
#### 打印结果

![[Pasted image 20250605151717.png]]

#### 导致后果

usr reigon 的数据访问限制比 Key 宽松，将导致 key 可以通过访问 usr reigon 区域的方式被泄露。

![[Pasted image 20250605152801.png]]

#### 问题原因与解决方案

由于 case 条件 flash_otp_addr[6:0]仅七位，因此在访问 usr_reigon 时地址将溢出，并访问到 id 与 key 部分。可以考虑增加 case 条件位数或 addr[7]=1'b1 时 data 清零。

![[Pasted image 20250605153808.png]]
![[Pasted image 20250605152216.png]]

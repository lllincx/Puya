#rep 

张老师，李老师：

1. 由于 shiqing 提供的 case 格式是对 IP 提供 case 的最小修改，我在移植到内部环境时也保留了这种特点。经李老师指导，我对 TrustEngine 的所有 case 修改完毕，增强了可移植性并支持 selfcheck。
2. 因修改命令导致 fail 的 case 已经全部还原。
3. 例外：
   - TRNG 未移植完毕。
   - tc_c_lcs, tc_c_otp_access fail 可以忽略。

wr 命令序列->for 循环+数组
![Pasted image 20250610141304](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250610141304.png)

check 不通过 rc++

![Pasted image 20250610141304](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250610141353.png)
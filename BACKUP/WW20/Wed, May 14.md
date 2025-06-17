### TrustEngine

处理 OTP 加载，LCS 相关问题
优先查看 OTP 相关代码

`DUBHE_OTP_INIT_VALUE`保持为0会导致LCS的配置与检测需要多个映射表：

| LCS          | CM  | DM  | DD  | DR  |
| ------------ | --- | --- | --- | --- |
| 3'b          | 000 | 001 | 011 | 111 |
| flash write  | 7   | 6   | 4   | 0   |
| read otp spc | 8   | 9   | b   | f   |


掌握更改 OTP flash 数据方式

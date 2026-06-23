1. efuse对工艺的要求
2. 咨询刘贤德，软件写OTP时进行哪些操作
3. 询问ARM AE对E20提供授权信号的意见。

待定方案：
1. 使用efuse
2. E20的APB总线转AHB总线控制FMC操作flash读写。
![image.png|600](https://pic.lllincx.cn/20260323164211456.png)

3. E20的APB总线发出授权信号给FMC，期望写入OTP的数据经授权后写入。
![image.png|600](https://pic.lllincx.cn/20260323164216609.png)



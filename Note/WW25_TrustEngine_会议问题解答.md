# 密钥读写权限

主机仅有安全模式的前提下。
常规应用下，SPEC 说明的 OTP 空间读写权限如下表：

| OTP Region                | CM/DM | DD  | DR  |
| ------------------------- | ----- | --- | --- |
| Model ID                  | RW    | RO  | RO  |
| Model Key                 | RW    | NA  | NA  |
| Device ID                 | RW    | RO  | RO  |
| Device Root Key           | RW    | NA  | NA  |
| Secure Boot Pub-Key Hash  | RW    | RO  | RO  |
| Secure Debug Pub-Key Hash | RW    | RO  | RO  |
| LCS                       | RW    | RW  | RW  |
| Reserved                  | RW    | RW  | RW  |
| OTP Lock Ctrl             | RW    | RW  | RW  |
| User secure region        | RW    | RW  | NA  |
| User non-secure region    | RW    | RW  | RW  |
| Test region               | RW    | RW  | RW  |

由于我们的 OTP 空间对软件均不可写，因此表格应简化为：

| OTP Region                | CM/DM | DD  | DR  |
| ------------------------- | ----- | --- | --- |
| Model ID                  | RO    | RO  | RO  |
| Model Key                 | RO    | NA  | NA  |
| Device ID                 | RO    | RO  | RO  |
| Device Root Key           | RO    | NA  | NA  |
| Secure Boot Pub-Key Hash  | RO    | RO  | RO  |
| Secure Debug Pub-Key Hash | RO    | RO  | RO  |
| LCS                       | RO    | RO  | RO  |
| Reserved                  | RO    | RO  | RO  |
| OTP Lock Ctrl             | RO    | RO  | RO  |
| User secure region        | RO    | RO  | NA  |
| User non-secure region    | RO    | RO  | RO  |
| Test region               | RO    | RO  | RO  |

**即在 LCS 状态为 CM、DM 下密钥可读，DD、DR 下密钥不可读。**

> 这种读写性质我在 5 月 26 日 case 说明中强调过。
>
> ![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250619094003157.png)

# 密钥可读的安全问题

1. CM、DM 均为制造阶段，并未送达用户使用
2. 在 SCA 加密的过程中，内部密钥不会单独使用，而是会结合密钥梯（Key ladder）中 EK1、EK2、EK3.加强安全性。

# 密钥的使用

密钥在非DR生命周期可以在 SCA 模块中被调用，DR生命周期密钥被清除。

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20250619095301618.png)

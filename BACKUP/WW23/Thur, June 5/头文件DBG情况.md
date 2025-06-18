#### 摘要

我之前框选的疑似没有吃进去的头文件分两种情况：明确导致 fpga 与我仿真结果不一致的文件：dubhe_top_cfg.vh 。其中定义的全部宏无法在 reg 中被追踪。
其他头文件应该是被吃到的，以 dubhe_regbase_define.vh 为例，如果这些文件没被吃到，会导致 RTL 无法正常运行。

#### 1

明确导致 fpga 与我仿真结果不一致的文件：dubhe_top_cfg.vh 。其中定义的宏无法在 reg 中被追踪。
该文件中包含的宏定义分两种：

##### 1.1 没有被使用的宏定义

![Pasted image 20250605110352](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605110352.png)

![Pasted image 20250605110000](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605110000.png)

##### 1.2 没有被存储到 reg 的宏定义

![Pasted image 20250605110440](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605110440.png)

![Pasted image 20250605110440](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605110647.png)


#### 2

其他头文件应该是被吃到的，以 dubhe_regbase_define.vh 为例，如果这些文件没被吃到，会导致 RTL 无法正常运行。
![Pasted image 20250605112838](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605112838.png)
![Pasted image 20250605112654](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605112654.png)
![Pasted image 20250605112639](https://raw.githubusercontent.com/lllincx/IMG/master/Pasted%20image%2020250605112639.png)

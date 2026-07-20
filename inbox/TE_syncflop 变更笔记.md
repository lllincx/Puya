### 摘要

为满足后端需求，使用stdcell替换TrustEngine macro中的rm_syncflop。搭建简单验证环境测试通过；arm china人员检查通过；形式验证通过；执行trng case发现输出随机数随机性受影响，经arm china人员确认忽略

![image-20260717151504977](https://pic.lllincx.cn/image-20260717151504977.png)

### 背景

为满足后端需求，使用stdcell替换TrustEngine macro中的rm_syncflop

### 设计

##### 功能介绍

复位低有效，打三拍

##### 驱动能力选择

与其他替换macro的stdcell一致，选择X4

##### V1

![image-20260717142722600](https://pic.lllincx.cn/image-20260717142722600.png)

V1优点：实现相同逻辑基础上，节省三个反相器

##### V2

郭老师建议不要在数据路径中反复取反，应采用V2

![image-20260717142738572](https://pic.lllincx.cn/image-20260717142738572.png)

### 验证方法

1. 使用tcl脚本，force D引脚跳变。
2. 搭建简单验证环境，向dut中输入激励查看波形
3. 请arm china人员检查
4. 形式验证
5. 执行trng case



### 测试结果

##### **一**

经反复尝试，请求VV同事协助，始终无法生效

##### **二**

V1问题：复位后d_sync_inv[1]=0,复位释放后的第一个上升沿，该0值会被末尾一级dff捕捉，拉高q一个时钟周期。

V2问题：局限于在测试中，在0时刻配置rstn为0，由于inv模块时延，导致dff复位端的rst初值为X态，导致各级dff输出均为X态。需要在编译过程中添加+delay_mode_zero选项，wavie掉此问题。

##### **三**

请arm china人员检查通过，建议进一步进行形式验证

##### **四**

形式验证通过

##### **五**

case可以执行完毕，但输出随机数的随机性存在问题。跟arm 中国人员确认，仅影响仿真，可忽略。

![talk_log_with_arm_china](https://pic.lllincx.cn/talk_log_with_arm_china.png)



### 附录

1. SDFFSQN datasheet

![image-20260717150751734](https://pic.lllincx.cn/image-20260717150751734.png)

2. SDFFRPQ datasheet

![image-20260717150833555](https://pic.lllincx.cn/image-20260717150833555.png)
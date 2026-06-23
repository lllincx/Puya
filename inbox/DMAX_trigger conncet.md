

1. 确认触发链接不能通过链表实现

查看dma350手册，查看ST用户手册，咨询伟彬，确认链表只能操作同一通道内的事务，因此跨通道只能通过触发链接实现

2. 竞品的触发连接

- 有
	-  恩智浦
	- N6
	- U5
- 无
	- 瑞萨 
	- 恩智浦：疑似使用的就是DMA350，具有触发输入输出，只是没有加触发连接的feature
	- 乐鑫
	- 全志
	- 兆易

3. arm邮件

> As described in Section 5.4.4 of the technical reference manual, the DMA-350 provides an internal trigger connection feature. To implement this feature, how should the trigger ports be connected during integration?
>
> Based on my understanding, taking three channels as an example, each channel's trigger input is connected to the output of a mux, and the inputs to that mux are the external trigger input and the trigger outputs of all the other channels.

When you are using the "internal trigger" mechanism the connection between the channel triggers is implemented inside the DMA-350 when you configure this operation, so you don't need to do anything with the external trigger ports involved.

> 既然不需要外部连接，那么需要如何配置实现内部触发功能，具体需要配置哪些寄存器，如何指定通道间的触发关系。请以通道1的触发输出作为通道2的触发输入为例，详细说明。
>
> 触发连接功能无需在配置中使能触发接口吗
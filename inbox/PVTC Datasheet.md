### PTSC（process temperature sensor controler）

数字工艺检测器（ DPD，Process Detector）用于检测器件由于制造波动和长期漂移所引起的工艺变化。数字温度传感器（DTS，Temperature Sensor）是一种高精度、低功耗的结温传感器。PTSC提供一个通用接口，使得可以通过 APB 总线以读写方式访问 DTS和DPD。

- 一个数字温度传感器，一个数字温度传感器
- 对于每个传感器：
	- 两个可编程硬件告警，可配置为上升触发或下降触发，并支持迟滞功能；
	- 状态寄存器可记录接收到的最小值和最大值；
- 一个带 IRQ 的上电定时器，用于支持手动操作。
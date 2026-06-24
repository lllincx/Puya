时间：2026年6月22日

主持人：林晨希

参会人员：张延雄，朱大方，林晨希，卞鼐

| 序号 | 分类      | 介绍                                                         | 人员                   |
| ---- | --------- | ------------------------------------------------------------ | ---------------------- |
| 1    | OTP       | 咨询OTP用户定义空间是否够用                                  | @林晨希，赵鹏（ARMCH） |
| 2    | OTP       | OTP TEST空间有什么用途,是否需要配置                          | @林晨希，赵鹏（ARMCH） |
| 3    | sec debug | 注意验证TE变更:dubug ctrl仅在rss boot阶段可以使用            | @卞鼐， @魏凯          |
| 4    | sec debug | TE变更:dubug ctrl仅在rss boot阶段可以使用,在集成手册中补充   | @林晨希                |
| 5    | RTC       | 会议中,时钟无法trace                                         | @林晨希， @庞卜滈      |
| 6    | bus       | 系统框图关于TE不够完善,dubhe_cfg前需要添加AHB2APB同步桥,dubhe前需要添加AHB2AXI同步桥。 | @郭凯乐                |
| 7    | FMC       | FMC与TE间的同步问题,交互内容为静态数据                       | @林晨希， @朱大方      |
| 8    | core_ss   | core memory cfg需要注意是否正确                              | @郭凯乐                |
| 9    | sec debug | 注意按照安全调试真值表验证TE TOP功能                         | @李顺林                |
| 10   | bus       | TE专属的AHB2AXI同步桥中hprot为7位,与常规不同,需确认上游bus与其兼容。注意验证priv功能有效性。 | @郭凯乐， @卞鼐        |
| 11   | power     | 注意TE 存储器低功耗问题                                      | @徐健                  |
| 12   | macro     | TE stdcell替换中,例化语句代码规范问题。                      | @林晨希                |
| 13   | TRNG      | 咨询ARM对inv stdcell要求(vt,驱动能力)                        | @林晨希，赵鹏（ARMCH） |
| 14   | Proj      | 补充Lint,CDC报告                                             | @林晨希                |
| 15   | RTC       | TE的clkgate,reset需要仅限安全控制                            | @庞卜滈                |
| 16   | RTC       | clk_dubhe_2nd_trng需要补充源时钟图                           | @庞卜滈                |
| 17   | ACA       | 咨询SRAM尺寸会影响什么                                       | @林晨希，赵鹏（ARMCH） |
| 18   | SYN       | trng子模块的stdcell需配置为don't touch                       | @郭凯乐                |
| 19   | DFT       | 注意OTP相关DFT问题                                           | @张延雄， @林晨希      |
| 20   | Proj      | 补充tzc Lint CDC报告                                         |                        |


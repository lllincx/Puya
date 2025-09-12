#归档

| 简介      | 日期         | 人员   | 状态  | 详情                                                                                                              |
| ------- | ---------- | ---- | --- | --------------------------------------------------------------------------------------------------------------- |
| 问题上报    | 2025/09/12 | @蔡紫阳 | 完成  | nor flash program 0x00000(A16=0),0x10000(A16=1) will be changed                                                 |
| case开发  | 2025/09/12 | @林晨希 | 完成  | dev case wr 0x00000, rd 0x00000 and 0x10000.FPGA Sim didn't reproduced A16 issue.                               |
| 张老师指示   | 2025/09/13 | @张延雄 | 完成  | Suspect crosstalk; export a bitfile with additional debug signals to verify the digital IC outputs are correct. |
| 验证问题复现性 | 2025/09/13 | @蔡紫阳 | 完成  | Test more addr, all have A16 issue.                                                                             |
| HEX Sim | 2025/09/13 | @林晨希 | 完成  | HEX Sim didn't reproduced A16 issue.                                                                            |
| 反馈测试结果  | 2025/09/13 | @蔡紫阳 | 完成  | Report oscilloscope test results.                                                                               |
| 问题解决    | 2025/09/13 | @蔡紫阳 | 完成  | Test env hardware problem. Issue solved.                                                                        |

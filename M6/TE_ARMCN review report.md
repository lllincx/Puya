1. 软件代码版本需匹配r2p2
2. TE-200 外部的时钟门控、软件复位等寄存器建议放置在secure region。
3. config 中 `aca sram size`含义是每个主机的存储空间，所以应保持8192
4. config 中 `aca sram size`配置为8192有普适性，16384有更高性能，但没有必要。
5. `aca sram size`验证注意事项：检测边界，每个主机访问专属自己的8K空间。对sram的访问为递增访问，超出8K时会访问0，避免误当做16K（专属空间）。
6. otp user空间配置为32 bytes是否足够：如果采用TE的软件方案，FOTA功能和清单版本将占用9bytes空间。
7. otp test区域用途：一般用于真实OTP，测试访问OTP有效性。
8. TRNG相关stdcell选用要求：
  1. 禁止使用jitter小的，换言之禁止使用带ck的
  2. 需要较大驱动能力，选用X4，或X3，禁止选用X1
  3. VT不关注
9. 参考设计采用40nm制程，时钟频率可达200MHz。因此PCD100采用22nm，时钟频率250MHz没问题
10. TE APB 从接口丢弃Pstrb
11. LCS进入DR阶段，在清除密钥与用户安全区后会置位LCS[3]。fmc必须添加此feature。
12. 使用flash替代OTP应注意可重复烧写问题。
13. 其他旁路读写OTP，需保证敏感数据安全性
14. 当使用lcs_is_cm/lcs_is_dm/lcs_is_dd/lcs_is_dr 信号，需要使用lcs_is_valid 作为有效判断
15. APB主接口暂时未发现风险，但不排除潜在风险， 建议使用Psel，Penable并在FMC进行简单逻辑处理。
16. LCS的FOTA必须放在用户非安全区，FMC写OTP需follow变更，FMC lock ctrl需follow变更
17. 注意对lock ctrl功能的充分验证。对照Table A2-13 lock_ctrl region definition
18. 注意FMC写OTP的权限不要过于严格，可能影响功能
19. TRNG后端
	1. 有培训，与ARMCN约定时间
	2. 布线需要与其他逻辑保持举例
	3. STA singoff不准确，不可以依赖
	4. DFTTM会用于TRNG组合逻辑环
20. 安全启动方案需要找ARMCN review
21. conifg中TRHG CH LENGTH与制程相关：保持当前配置不变
22. 应当在FPGA中跑TE性能测试
23. 访问TE_cfg，不会通过地址限制，而是通过安全属性
24. DFT可能导致OTP中安全信息泄露
	1. 在DFT中 bypassOTP
	2. 在DFT中屏蔽密钥访问
	3. DFT测试完成后，量产之后关闭DFT通道
	4. 进入DFT前通过复位，清空所有OTP相关寄存器

25. DFTTM、DFTSE、DFTCGEN 的处理方案待确认
26. 需要对TE-200 所有寄存器的地址进行通路测试以及secure 属性验证。
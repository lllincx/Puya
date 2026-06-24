1. config 中 `aca sram size`含义是每个主机的存储空间，所以应保持8192
2. config 中 `aca sram size`配置为8192有普适性，16384有更高性能，但没有必要。
3. `aca sram size`验证注意事项：检测边界，每个主机访问专属自己的8K空间。对sram的访问为递增访问，超出8K时会访问0，避免误当做16K（专属空间）。

4. otp user空间配置为32 bytes是否足够：如果采用TE的软件方案，FOTA功能和清单版本将占用约10bytes空间，待ARM中国进一步确认。
5. otp test区域用途：一般用于真实OTP，测试访问OTP有效性。
6. TRNG相关stdcell选用要求：
	1. 禁止使用jitter小的，换言之禁止使用带ck的
	2. 需要较大驱动能力，选用D4，或D3，禁止选用D1
	3. VT不关注

7. 时钟频率
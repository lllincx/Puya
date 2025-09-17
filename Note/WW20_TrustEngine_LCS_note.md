## 芯片、器件制造 (Chip/Decvice Manufacturing，CM、DM)

芯片处于生产过程中，可使用芯片接口和外部测试功能。
完成所有 OEM 信息配置工作（包括设备 ID、型号 ID、型号密钥、设备根密钥、设备根密钥、设备根密钥）。

> CM，DM 区别在于 CM 启用了芯片内部测试功能（扫描链，mbist），但在读 OTP 数据过程中无区别，因此放在一起。

### 设备部署 (DD，Device Deployment)

设备处于正常状态。启用安全功能。禁止写入 IP 定义的 OTP 区域。

### 设备撤销 (DR，Device Revocation)

芯片被送回制造商进行故障分析。用户定义的安全数据必须清除。

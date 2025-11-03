### 抓取2p3版本的无复位值寄存器
### TrustEngine：解决TRNG后仿fail问题

无复位寄存器的Q端口抓取有bug，有名字为Q_reg的cell，这个cell的所有pin的完整路径包含Q，因此都被抓取。
手动移除Q_reg的不正确的pin，并且抓取所有的CK pin以供验证使用。

### SMC：解决ecc mode=1，ecc blockx valid异常的问题。

1. 需配置ecc_memcfg寄存器中ecc_read_end位为0；
2. 每次读取一个block之后，需要要把对应的raw_int_status（ecc_status寄存器中）写1

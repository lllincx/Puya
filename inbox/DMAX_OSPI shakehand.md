### 问题描述

OSPI与DMAH握手存在问题

OSPI给出REQ后，DMAH回长ACK。

OSPI看到ACK后拉低REQ后，DMAH的ACK暂未拉低。

OSPI重新起REQ，看到DMAH暂未拉低的ACK，立即拉低REQ。

### 问题原因

- OSPI的REQ条件未包含ACK不能为高
- OSPI与DMAH时钟异步，需要同步逻辑。

### 解决方案

- OSPI与DMAX时钟同步，不需要同步逻辑。
- OSPI的DMA请求送给DMAX
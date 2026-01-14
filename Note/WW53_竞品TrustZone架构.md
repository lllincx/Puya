> **总线需求**
> 为传播安全属性，特权属性，CID 信息，AXI 版本需要在 AXI3 以上。
> 为传播安全属性，特权属性，CID 信息，需要 AHB5。
> 为传播安全属性，特权属性，需要 APB4。

## N6

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251225161503759.png)

### 主机

**CPU**
安全属性定义：IDAU+SAU
安全属性过滤：SAU
特权属性定义、过滤：MPU
CID：固定

**非 CPU**
安全属性、特权属性、CID 定义： RIMU

### 从机

对于 RIF 感知外设，直接与总线连接，外设的 IP 内部将检查安全属性，特权属性，CID 信息。
对于非感知外设，通过 RISUP 与总线连接，在 RISUP 中检查安全属性，特权属性，CID 信息。
存储器通过 RIFSC 与总线连接，在 RIFSC 中检查安全属性，特权属性，CID 信息。

## 瑞萨

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251225161517670.png)

### 主机

**CPU**
安全属性定义：IDAU+SAU
安全属性过滤：SAU
特权属性定义、过滤：MPU

**非 CPU**
安全属性定义：MSAU+bm-MPU
安全属性过滤：bm-MPU
特权属性定义、过滤：bm-MPU

### 从机

Type1：TrustZone 不兼容，整个外设统一安全属性。
Type2：TrustZone 兼容，安全属性不统一。包含存储器，系统控制等
对于 Type2 外设，直接与总线连接，外设的 IP 内部将检查安全属性，特权属性。
对于Type1外设，通过 TrustZone Filter 与总线连接，在 Filter 中检查安全属性，特权属性。

## Arm

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251225161544166.png)

**CPU**
安全属性定义：IDAU+SAU
安全属性过滤：SAU
特权属性定义、过滤：MPU

**其他安全主机**
安全属性定义：MSC+IDAU
特权属性未提及

**从机**
存储器通过 MPC 连接到总线，通过 MPC 检查安全属性
外设通过 PPC 连接到总线，通过 PPC 检查安全属性
APB 接口外设，APB PPC 有 mux 功能，在 PPC 中检查所有下属外设的安全属性

# ifineon

![image.png|600|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251226154933925.png)
## 主机

M33视为CPU，M55无TrustZone功能，视为非CPU，但具备特权功能。
其他基本与arm推荐一致
## U5

![image.png|600](https://lincx-img.oss-cn-shanghai.aliyuncs.com/img/20251225161436684.png)

### 主机

**CPU**
安全属性定义：IDAU+SAU
安全属性过滤：SAU
特权属性定义、过滤：MPU

**DMA**
安全属性，特权属性定义，过滤：DMA

**其他安全主机**
安全属性，特权属性定义：TZSC

### 从机

**Flash**
在 IP 内部进行安全属性，特权属性过滤

**SRAM**
通过 MPCBB 连接到总线，在 MPCBB 内部进行安全属性，特权属性过滤

**其他存储器**
通过 MPCMW 连接到总线，在 MPCMW 内部进行安全属性，特权属性过滤

**安全感知外设**
在 IP 内部进行安全属性，特权属性过滤

**AHB 接口一般外设**
通过 PPC 连接到总线，在 PPC 内部进行安全属性，特权属性过滤

**APB 接口一般外设**
多个外设通过同一 bridge 连接到总线，在 bridge 内进行安全属性，特权属性过滤

|     |       |       | N6                  | 瑞萨               | Arm参考          | U5                                 | ifineon    |
| --- | ----- | ----- | ------------------- | ---------------- | -------------- | ---------------------------------- | ---------- |
| 主机  | cpu   | 安全定义  | IDAU+SAU            | IDAU+SAU         | IDAU+SAU       | IDAU+SAU                           | IDAU+SAU   |
|     |       | 安全过滤  | SAU                 | SAU              | SAU            | SAU                                | SAU        |
|     |       | 特权定义  | MPU                 | MPU              | MPU            | MPU                                | MPU        |
|     |       | 特权过滤  | MPU                 | MPU              | MPU            | MPU                                | MPU        |
|     |       | CID定义 | 固定                  | 不定义              | 不定义            | 不定义                                | 不定义        |
|     | 非 CPU | 安全定义  | RIMU                | MSAU + bm-MPU    | MSC + IDAU     | TZSC                               | MSC + IDAU |
|     |       | 安全过滤  | 不过滤                 | bm-MPU           | 不过滤            | 不过滤                                | 不过滤        |
|     |       | 特权定义  | RIMU                | bm-MPU           | 不定义            | TZSC                               | 不定义        |
|     |       | 特权过滤  | 不过滤                 | bm-MPU           | 不过滤            | 不过滤                                | 不过滤        |
|     |       | CID定义 | RIMU                | 不定义              | 不定义            | 不定义                                | 不定义        |
|     | 特殊主机  | 名称    |                     |                  |                | DMA                                | M55        |
|     |       | 安全定义  |                     |                  |                | IP内部                               | IDAU       |
|     |       | 安全过滤  |                     |                  |                | 不过滤                                | 不过滤        |
|     |       | 特权定义  |                     |                  |                | IP内部                               | MPU        |
|     |       | 特权过滤  |                     |                  |                | IP内部                               | MPU        |
| 从机  | 存储器   | 从机过滤  | RIFSC               | IP 内部            | MPC            | IP 内部（flash），MPCBB（SRAM)，MPCWM（其他） |            |
|     | 感知外设  | 从机过滤  | IP 内部               | IP 内部            | IP 内部          | IP 内部                              |            |
|     | 非感知外设 | 从机过滤  | RISUP               | TrustZone Filter | PPC            | Bridge                             |            |
|     | 过滤属性  |       | 安全，特权，CID           | 安全，特权            | 安全             | 安全，特权                              |            |
| 备注  |       |       | 感知外设为RIF感知，其他均为TZ感知 |                  | APB PPC具有mux功能 |                                    |            |

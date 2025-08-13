# 第一章 简介

## 1.1 关于 IoT平台安全套件（B 类）
- **全称**：IoT Platform Security Suite（IoT平台安全套件）  
- **定位**：面向物联网的整体安全解决方案，为各类 IoT 设备提供绝密执行环境  
- **架构涵盖三部分**：  
  1. 设备端安全功能软件（如安全启动 Secure Boot）  
  2. 可综合 Verilog 的加密引擎  
  3. 云端设备管理服务（如 SaaS（云端软件服务））  
- **部署环境**：资源受限的 SoC，至少含一颗 Arm Cortex-M 系列 MCU，可配合其他处理器实现通信功能（如 NB-IoT/LoRa）  
- **支持架构**：基于 Armv8-M 的 CPU（如 Cortex-M33）  
- **设计目标**：在有限硬件资源和最小性能损耗的情况下满足安全需求  

---

## 1.2 特性
- 安全启动（Secure Boot）  
- 安全调试（Secure Debug）  
- 固件空中升级（Firmware Over-The-Air，FOTA）  
- 配置与密钥注入（Provisioning）  
- 可信执行环境（Trusted Execution Environment，TEE）  
- 安全连接（Secure Connection）  

---

## 1.3 架构基础模块

### 总览
- **硬件（Hardware）**  
  - ARMv8-M 架构 CPU  
  - TrustEngine-200  
  - Fuse/OTP  
  - Flash/NVM 等存储  

- **设备软件（Device software）**  
  - **制造阶段（Manufacturing Stage）**：Provisioning Agent  
  - **启动阶段（Boot Stage）**：Secure Boot Core、Secure Debug Agent、TRNG Agent、FOTA Update Agent、BootROM/Bootloader  
  - **运行阶段（Runtime）**：  
    - **NSPE**：Wakaama、FOTA Download Agent、Socket、libclient 等  
    - **SPE**：MbedTLS、Flash、SST、SPM 等  

- **主机工具（Host tools）**  
  - Provisioning Tool  
  - Secure Debug Tool  
  - TRNG Tool  
  - Secure Boot Tool  

- **云服务（Cloud service）**  
  - DM SaaS（设备管理服务）  
  - FOTA SaaS（固件空中升级服务）  

### 1.3.1 硬件（TrustEngine-200）
- 高安全保障：支持密钥梯、生命周期管理、真随机数发生器（TRNG）  
- 高性能与低功耗加解密：依靠内部密码学引擎  
- 降低软件复杂度：部分安全功能在硬件中实现，如 LCS 管理和 OTP 访问控制  

### 1.3.2 制造阶段安全
- 提供安全配置机制（Provisioning）以建立初始信任数据  
- 建立云服务与设备的安全通信通道  
- 初始化凭证（如运行时安全通道的预共享密钥）  
- 制造阶段烧录部分 Fuse/OTP 位，防止后续被篡改  

### 1.3.3 启动阶段安全
- 安全启动：仅允许运行原始设备制造商发布的官方镜像  
- 安全调试：带权限的调试功能启用机制  
- FOTA 更新：验证和安装 FOTA 升级包  

### 1.3.4 运行阶段安全
- 基于 Arm TrustZone，符合 Arm PSA Firmware Framework 的 TEE 解决方案  
- 运行阶段使用 FreeRTOS，包括：  
  - 安全连接：利用 TEE 与 mbed TLS 建立与 SaaS（云端软件服务）的加密连接  
  - Wakaama：LWM2M（CoAP）实现  
  - FOTA 下载代理：基于 Wakaama 接收 FOTA 升级包  

### 1.3.5 云服务
- 安全调试 SaaS（云端软件服务）  
- 配置 SaaS（云端软件服务）  
- 固件空中升级 SaaS（云端软件服务）  
- 基于微服务架构，以 Java 应用程序包形式发布，并提供 Docker 文件构建镜像  

---

## 1.4 硬件要求
- CPU 必须基于 Armv8-M 架构  
- SoC 必须包含集成安全启动功能的 BootROM  
- 至少 1024 位 Fuse/OTP  
- NVM 中需预留存储空间保存 FOTA 包和启动标志（大小取决于 FOTA 配置）  
- 硬件加密引擎（TrustEngine-200）  

> - 1024 位 Fuse/OTP 要求针对功能完整场景，实际生产可调整  
> - 各安全功能还有额外的硬件需求  

---

## 1.5 软件要求
- 硬件适配层（HAL）：提供与硬件相关的操作，如读写 NVM  
- 平台适配层（PAL）：提供与平台相关的操作，如堆内存分配和释放  
- 主机端开发环境：用于构建整体解决方案  

---

## 1.6 符合的标准
- **AES**：高级加密标准  
- **RSA**：公钥密码系统  
- **ECDSA**：椭圆曲线数字签名算法  
- **HASH**：哈希函数  
- **CoAP**：物联网专用传输协议  
- **HTTPS**：安全的超文本传输协议  
- **微服务**：高可维护、松耦合、可独立部署的服务架构  
- **UDP**：用户数据报协议  
- **DTLS**：基于 UDP 的安全通信协议  
- **JSON**：轻量级数据交换格式  
- **TRNG**：真随机数发生器  
- **NIST**：美国国家标准与技术研究院  

---

## 1.7 产品版本
- **r0p0**：首次发布  
- **r1p0**：新增 PUF 功能支持  
- **r1p1**：修复工程勘误；支持 CMAC/CCM/GCM  
- **r1p2**：修复工程勘误；支持精简加密驱动；支持安全启动细粒度配置  

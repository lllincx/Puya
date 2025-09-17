# 9 月 1 日 星期一

### SMC Byte 访问问题

根据 nor model 状态机跳转调整发送命令，仿真+上机测试通过
构建 Byte 读写测试 case，16 位读写有问题，暂停。

### SMC SWD 访问问题

对 swd case 进行 hex 仿真

# 9 月 2 日 星期二

fpga 提供 hex 转 mem hex 方式：[[WW36_Hex2Mem]]
仿真复现 fpga 用 swd 访问寄存器断开的问题
cmd_type 设置为 updateregs and axi 会拉高 dircet cmd hold ,导致 pready disable

# 9 月 3 日 星期三

## TrustEngine

### DBG TrustEngine RSA.

Make ACA sram wr & rd case.

## SMC

DBG SWD problem done, commit.

### SMC Byte access

16 bit single word wr & rd pass.
Convert to byte access, ongoing.

# 9.4 Thur

### DBG TrustEngine RSA.

Make ACA sram wr & rd case.
Confirm Case passes when booting from SRAM but fails when booting from flash.

### DBG SMC Byte access

Byte wr success.
Byte Rd High-Z, and identified the cause in model.

# 9.5 Fri

Byte access pass in two ways. Method compare spec to be done.

# Weekly Report

## TrustEngine

协助刘贤德解决 RSA case fail 问题。开发 ACA Sram 读写遍历 case，排除 ACA_REG_SRAM_BASE_ADDR 宏定义错误导致 fail 的可能。将从 flash 启动更换为 sram 启动即可 pass，后续刘贤德调整堆大小也解决了此问题。

## SMC

### ByteAccess Issue

根据 nor model 状态机跳转调整发送命令，nor sector erase仿真+上机测试通过。
蔡紫阳反馈，Byte读写不生效，构建ByteAccess读写case。nor 在Byte模式下用数据最高位用作地址的-1位，需要在Byte模式下变更存储器连接。通过两种方法解决此问题，Byte读写仿真通过，正在仿真此修改下word读写的有效性。

### SWD Access Issue

通过swd仿真复现 fpga 用 swd 访问寄存器断开的问题：cmd_type 设置为 updateregs and axi 会拉高 dircet cmd hold ,导致 pready disable。
仿真解决SWD问题，待上机测试。

# Todo

## SMC ByteAccess Issue

- [x] Byte sector erase case sim & practial test pass.
- [x] Identified the cause for byte access rd & wr fail.
- [x] Fix the problem in two ways.
- [ ] Confirm word access work after the fix above.
- [ ] Complete SPEC with two solution comparison.

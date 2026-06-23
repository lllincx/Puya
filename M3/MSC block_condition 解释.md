MSC`block condition`解释

```verilog
assign block_condition = (~idau_arunchk & ~idau_arns & (~armmusecsid_i | arprot_i[1])) |
                         (~idau_arunchk &  idau_arns &  armmusecsid_i & ~arprot_i[1] & arprot_i[2]) |
                         ( idau_arunchk &  arprot_i[2]);
```

#### 分支 A：保护安全区域 (Secure Region Protection)

`(~idau_arunchk & ~idau_arns & (~armmusecsid_i | arprot_i[1]))`

- **条件**：地址处于已知的 **Secure 区域**（`~arns`）。
- **拦截场景**：
  1. **非安全访问**：当 `arprot_i[1] == 1` (NS 访问) 时，直接拦截。这是 TrustZone 最基本的原则：NS Master 不允许访问 S 区域。
  2. **强制锁定**：如果配置位 `armmusecsid_i` 为 `0`，则该 Secure 区域会被完全封锁（任何访问都会触发 block）。

#### 分支 B：禁止从非安全区取指 (Secure Instruction Fetch from NS)

`(~idau_arunchk & idau_arns & armmusecsid_i & ~arprot_i[1] & arprot_i[2])`

- **条件**：地址处于 **Non-Secure 区域**（`idau_arns`）。
- **拦截场景**：
  - **安全取指违规**：当一个 **Secure 状态** 的 Master（`~arprot_i[1]`）尝试从 **NS 区域** 进行 **取指**（`arprot_i[2]`）操作时。
  - **原因**：在 ARMv8-M 等架构中，为了防止安全代码执行来自不可信区域的指令，默认禁止从 NS 存储空间执行 Secure 指令（除非通过特定的 NSC 机制）。

#### 分支 C：禁止在未检查区取指 (Execution Prevention in Unchecked Region)

`(idau_arunchk & arprot_i[2])`

- **条件**：地址处于 **Unchecked 区域**（`idau_arunchk`）。
- **拦截场景**：
  - **任意取指操作**：只要是取指访问（`arprot_i[2] == 1`），且地址不在预定义的 IDAU 范围内，一律拦截。
  - **原因**：这是一种安全防御机制（类似 XN, Execute Never），防止处理器跑飞到未定义的地址空间执行代码。



### 1. 脚本输入

- 接收一个参数：包含 Markdown 表格的源文件路径（如 `table.md`）。

- 表格格式示例：

| 名称 | 编号 |
| ---- | ---- |
| TIM1_COM | 240 | 
| DAC2 | 230 | 
| DAC1 | 228 |

### 2. 数据处理与命名规则

- **排序**：提取纯数字编号，按照编号**从大到小**排列（如第一行是 240）。
- **命名转换**：统一转换为小写。在源名称的第一个下划线前面加 `_dma`；如果没有下划线，则直接在末尾加 `_dma`。
  - 命名规则格式：`[ip name][ip num(optional)]_dma_[req name(optional)]_req/ack`
  - 例如：`TIM1_COM` 转换为 `tim1_dma_com`；`DAC2` 转换为 `dac2_dma`。
- **信号生成**：同时需要 `_req` 结尾和 `_ack` 结尾的信号（不再需要 `-r` 或 `-a` 参数）。

### 3. 代码结构与格式要求

- **分块输出**：生成的代码必须分为四个独立的块：

  1. `input` 声明（对应 `_req` 信号）
  2. `output` 声明（对应 `_ack` 信号）
  3. `_req` 信号拼接
  4. `_ack` 信号拼接

- **补零逻辑**：在两个信号拼接块中，如果相邻两个编号跳过（不连续），需要用 Verilog 语法补 0。例如编号 240 下一个是 230，中间插入 `9'b0,`。

- **严格对齐**（关键）：

  - `input` 和 `output` 关键字对齐，其后的端口名左对齐。

  - **注释对齐**：每一行（除补零行外）末尾带上 `//编号` 注释。无论是 input/output 声明块还是拼接块，变量名后面**限定使用两次 Tab（`\t\t`）**来实现注释的精确对齐。

  - 期望格式示例：

    Verilog

    ```
    input   tim1_dma_com_req,		//240
    input   dac2_dma_req,    		//230
    
    output  tim1_dma_com_ack,		//240
    output  dac2_dma_ack,    		//230
    
    tim1_dma_com_req,		//240
    9'b0,
    dac2_dma_req,    		//230
    ```

### 4. 输出方式

- 将生成的代码写入同名的 `.v` 文件中（例如源文件是 `table.md`，则生成 `table_dma.v`）。

---



命名规则：

```
[ip name][ip num(optional)]_dma_[req name(optional)]_req/ack

tim1_dma_com_req,
tim1_dma_trig_req,
dac2_dma_req,
```


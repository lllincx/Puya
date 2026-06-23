![image.png|600](https://pic.lllincx.cn/20260408135523245.png)
- **Secure 事务**（`axprot[1]==1`）：地址高位为 0 → 走 M1；高位为 1 → 走 M0
- **Non-secure 事务**（`axprot[1]==0`）：地址高位为 1 → 走 M1；高位为 0 → 走 M0

```systemverilog
function automatic bit address_map_m1 (
    input [32-1:0] axaddr,
    input     [2:0] axprot
);
bit res;
begin
    res = '0;
    if (axprot[1]) begin
        if (axaddr[32-1] == '0) res = '1;
    end else begin
        if (axaddr[32-1] == '1) res = '1;
    end
    return res;
end
endfunction
```
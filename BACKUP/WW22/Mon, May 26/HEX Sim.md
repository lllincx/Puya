1. Source 环境变量

```
source setenv
```

2. 首次使用 bin 文件仿真需要先编译

```
make c_comp
```

3. 用 bin 文件替换这里的 ROM 和 RAM 文件

```
/asic/dv/tests/rtl_typ0/example/fc_fpga_example_sram/c_dst/arm_c_dst/mem32
```

4. 更改`makefile`里的配置

```
24:EXTRA SIM OPT +=+fpga load en=1
25:export EXTRA SIM OPT
```

5. 运行仿真

```
make comp sim FSDB=1
```

6. 查看波形

```
verdi -dbdir ../../config/simv.daidir/ -ssf novas.fsdb &
```

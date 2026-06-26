## Note

**run testcase cmd**

```bash
run -t system/tc_c_sanity_tarmac -c 1
run -w -t $module/$case --no-quiet
```

**sse 320**

```bash
source /home/xuesy/scripts_local/cs320_verdi_v7
```

**testcase temp gen**

```shell
gen_temp tb --name=$module
gen_temp tc --name=$module/$case
```

**Checkin Checklists**

```
1. run spyglass lint
- filelist: vlog.tcl
- define top: Makefile

2. run sim
run -t system/tc_c_sanity_tarmac -c 1
```

## TODO

1. DMAX UM

1. linux config备份

1. te r2p2 SW pkg withdr

1. 注意关注pclken相关case波形是否符合需求

1. 补充lint cdc报告

	




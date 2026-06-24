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

**Checkin Checklist**

```
1. run spyglass lint
- filelist: vlog.tcl
- define top: Makefile

2. run sim
run -t system/tc_c_sanity_tarmac -c 1
```

## TODO

1. DMAX UM
1. te review report
1. tzc review report
1. dmax review report
1. week report






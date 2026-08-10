## Note

**run testcase cmd**

```bash
run -w -t $module/$case --no-quiet
```

**testcase temp gen**

```shell
gen_temp tb --name=$module
gen_temp tc --name=$module/$case
```

## TODO



- trng bitfile
- 时序约束生效性

```
foreach cell [get_cells -hierarchical *dubhe_trng_inv_chain*] {

    foreach sub_cell [get_cells $cell/*] {

        set_property DONT_TOUCH true $sub_cell

        set nets [get_nets $sub_cell/*]

        set net_element [split $nets "/"]

        if {[llength $net_element] != 0} {

            set_property DONT_TOUCH true $nets

            set_property ALLOW_COMBINATORIAL_LOOPS TRUE $nets

            puts $nets

        }

}

}
```


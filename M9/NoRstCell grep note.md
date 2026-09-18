
### restore PT session，或进入PT工程

### 抓工程实际使用的所有 DFF 类型

```tcl
set all_refs {}

foreach_in_collection c [get_cells -quiet -hier -filter {ref_name =~ *DFF*}] {
    lappend all_refs [get_attribute $c ref_name]
}

foreach r [lsort -unique $all_refs] {
    puts $r
}
```

将得到

```
DFFQ...
DFFN...
DFFRQ...
SDFFQ...
SDFFN...
SDFFRQ...
SDFFNR...
...
```

### 筛选no rst cell列表

阅读库文档，总结no rst cell命名规则，确认：

```tcl
set ref_list {
    SDFFN*
    SDFFQ*
    DFFQ*
    DFFN*
}
```

### 抓取符合ref_list的instance的完整路径

```
foreach ref $ref_list {
    set cells [get_cells -quiet -hier -filter "ref_name =~ $ref"]

    puts "$ref -> [sizeof_collection $cells]"

    if {[sizeof_collection $cells] == 0} {
        continue
    }

    ...
}
```

### 输出no rst cell Q pin

Qpin为cell的仅存的output port，因此使用`direction = out`可包含QN，Q1，Q2等

```tcl
set all_pins [get_pins -of_objects $c]

set out_pins [filter_collection $all_pins {direction == out}]

foreach_in_collection p $out_pins {
    puts $fq "${prefix}[get_object_name $p]"
}
```

### 输出no rst cell CK pin

在PT105基础上，PCD100存在CKN pin，因此需要判断并分别附加

```tcl
foreach_in_collection p $all_pins {

    set pin_name [file tail [get_object_name $p]]

    if {$pin_name eq "CK" || $pin_name eq "CKN"} {
        puts $fck "${prefix}[get_object_name $p]"
    }
}
```

### 添加VV环境下cell路径前缀
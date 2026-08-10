```tcl
set target_cells [get_cells -quiet -hierarchical *dubhe_trng_inv_chain*]

if {[llength $target_cells] == 0} {
    error "ERROR: Cannot find *dubhe_trng_inv_chain*"
}

set total_nets 0
set allow_loop_nets 0
set dont_touch_nets 0

foreach cell $target_cells {
    puts "ROOT CELL: $cell"

    set sub_cells [get_cells -quiet "${cell}/*"]

    foreach sub_cell $sub_cells {
        set cell_dt [get_property DONT_TOUCH $sub_cell]
        puts "  CELL $sub_cell: DONT_TOUCH=$cell_dt"

        set nets [get_nets -quiet "${sub_cell}/*"]

        foreach net $nets {
            incr total_nets

            set net_dt [get_property DONT_TOUCH $net]
            set net_cl [get_property ALLOW_COMBINATORIAL_LOOPS $net]

            if {$net_dt} {
                incr dont_touch_nets
            }

            if {$net_cl} {
                incr allow_loop_nets
            }

            puts "    NET $net"
            puts "      DONT_TOUCH=$net_dt"
            puts "      ALLOW_COMBINATORIAL_LOOPS=$net_cl"
        }
    }
}

puts "----------------------------------------"
puts "Total matched nets              : $total_nets"
puts "DONT_TOUCH nets                 : $dont_touch_nets"
puts "ALLOW_COMBINATORIAL_LOOPS nets  : $allow_loop_nets"
```


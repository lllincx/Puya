# gen_temp

gen_temp tc --name=$module/tc_c*\*
gen_temp tb --name=$module

# FPGA Sim cmd

run -t case_name -w --fpga --comp_id=fpga --sim-id=fpga，其中 case_name 为仿真 case 名字，如 system/tc_c_sanity

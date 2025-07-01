# 看代码（无波形）

/pt105_soc_v1/asic/rtl/top_list
verdi -sv -f pt105_sim.f -top asic_top &

# fsdbDumpflush

仿真执行到一半，暂停之后输入命令可输出当前状态的波形，之后可以继续执行
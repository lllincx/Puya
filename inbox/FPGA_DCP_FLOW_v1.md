```tcl
set $WORKSPACE/fpga/s2c_vu19p/script SCRIPT
set $WORKSPACE/fpga/s2c_vu19p/user_src USER_SRC
set $WORKSPACE/fpga/s2c_vu19p/ip_dcp_prj PRJ
set $WORKSPACE/fpga/s2c_vu19p/output_file OUTPUT
```



1. set subsystem top

```bash
$SCRIPT/create_prj_script_s2c_vu19_ip_dcp.tcl
10:set OCC_TOP "<your subsystem top>"
```

2. set file list

```bash
$WORKSPACE/flist/rtl_fpga_ip_dcp.f
1:-f $WORKSPACE/soc pcd100/flist/pcd100 vhdl.f 
2:-f $WORKSPACE/soc pcd100/flist/pcd100_vlog_fpga.f
```

3. set time constrain (xdc)

```bash
$USER_SRC/ip_dcp_timing.xdc
```

4. set stub

```bash
$USER_SRC/config.vh
```

>  define useless IP as stub
>
> subsystem STUB CANNOT be enable if its IP is useful

5. run vivado config script

```bash
cd $PRJ
./run_fpga_vivado_prj_vu19p_ip_dcp.sh
```

6. expected output:

```bash
-----------------------------------------------------
Vivado build started in background (PID=53143) 
Output Log: ./vivado. log
Monitor progress using: 
	tail -f vivado.log 
	ps -p 53143
-----------------------------------------------------
```

7. read vivado.log

```bash
tail -f vivado.log 
```

expected output:

```bash
#########################
# VIVADO set up finish ...
#########################
```

8. interrupt the process （Ctrl C）
9. launch vivado GUI

```
vivado vivado.xpr &
```

10. wait for sources update
10. manually set occ top, until it is bolded

<img src="C:\Users\linchenxi\AppData\Roaming\Typora\typora-user-images\image-20260723151848396.png" alt="image-20260723151848396" style="zoom:50%;" />

<img src="C:\Users\linchenxi\AppData\Roaming\Typora\typora-user-images\image-20260722135214789.png" alt="image-20260722135214789" style="zoom: 67%;" />

11. click run synthesis

<img src="C:\Users\linchenxi\AppData\Roaming\Typora\typora-user-images\image-20260722135300759.png" alt="image-20260722135300759" style="zoom:67%;" />

12. check synthesis status in project summary is running synth_design

<img src="C:\Users\linchenxi\AppData\Roaming\Typora\typora-user-images\image-20260722140327819.png" alt="image-20260722140327819" style="zoom: 50%;" />

13. output file location:

```
$OUTPUT/ip_dcp/<your subsystem top>_ooc_synth.dcp <your subsystem top>_stub.v
```


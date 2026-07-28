1. go to workdir

```bash
cd $WORKSPACE/fpga/s2c_vu19p/ip_dcp_prj
```

2. set subsystem top

```bash
make top
```

3. check filelist

```bash
make flist
1:-f $WORKSPACE/soc pcd100/flist/pcd100 vhdl.f 
2:-f $WORKSPACE/soc pcd100/flist/pcd100_vlog_fpga.f
```

4. set time constrain (xdc)

```bash
make xdc
```

5. set stub

```bash
make stub
```

>  define useless IP as stub
>
> subsystem STUB CANNOT be enable if its IP is useful

6. run vivado config script

```bash
make run
```

7. expected output:

```bash
-----------------------------------------------------
Vivado build started in background (PID=53143) 
Output Log: ./vivado. log
Monitor progress using: 
	tail -f vivado.log 
	ps -p 53143
-----------------------------------------------------
```

8. read vivado.log

```bash
make log
```

expected output:

```bash
#########################
# VIVADO set up finish ...
#########################
```

9. interrupt the process （Ctrl C）
10. launch vivado GUI

```
make gui
```

11. manually set occ top in sources window, until it is bolded

<img src="https://pic.lllincx.cn/image-20260723151848396.png" alt="image-20260723151848396" style="zoom:50%;" />

<img src="https://pic.lllincx.cn/image-20260722135214789.png" alt="image-20260722135214789" style="zoom: 67%;" />

12. click run synthesis in Flow Navigator

<img src="https://pic.lllincx.cn/image-20260722135300759.png" alt="image-20260722135300759" style="zoom:67%;" />

13. check synthesis status in project summary window is "running synth_design"

<img src="https://pic.lllincx.cn/image-20260722140327819.png" alt="image-20260722140327819" style="zoom: 50%;" />

14. check output file

```
make output
```

15. clr file in `PRJ`

```
make clean
```

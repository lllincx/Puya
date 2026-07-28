1. go to workdir

```bash
cd $WORKSPACE/fpga/s2c_vu19p/ip_dcp_prj
```

2. set subsystem top

```bash
make top
10: set OOC_TOP "<your_top>"
```

3. set time constrain (xdc)

```bash
make xdc
```

4. run vivado config script

```bash
make run
```

expected output:

```bash
-----------------------------------------------------
Vivado build started in background (PID=53143) 
Output Log: ./vivado. log
Monitor progress using: 
	tail -f vivado.log 
	ps -p 53143
-----------------------------------------------------
```

5. read vivado.log

```bash
make log
```

expected output:

```bash
#########################
# VIVADO set up finish ...
#########################
```

6. interrupt the process (Ctrl C) and launch vivado GUI

```
make gui
```

7. edit and save config.vh to set stub in sources window, wait for updating.

<img src="https://pic.lllincx.cn/image-20260728100003068.png" alt="image-20260728100003068" style="zoom:33%;" />

>  define useless IP as stub
>
> subsystem STUB CANNOT be enable if its IP is useful

8. manually set occ top in sources window, until it is bolded, wait for updating.

<img src="https://pic.lllincx.cn/image-20260723151848396.png" alt="image-20260723151848396" style="zoom:50%;" />

<img src="https://pic.lllincx.cn/image-20260722135214789.png" alt="image-20260722135214789" style="zoom: 67%;" />

9. click run synthesis in Flow Navigator

<img src="https://pic.lllincx.cn/image-20260722135300759.png" alt="image-20260722135300759" style="zoom:67%;" />

check synthesis status in project summary window is "running synth_design"

<img src="https://pic.lllincx.cn/image-20260722140327819.png" alt="image-20260722140327819" style="zoom: 33%;" />

10. check output file

```bash
make output
```

11. clr file in `PRJ`

```bash
make clean
```

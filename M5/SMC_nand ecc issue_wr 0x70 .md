### err condition

- mem: nand
- ecc: on
- ecc_mode: 0x10
- mem busy status get method: wr 0x70 to mem to get status

### mem busy status get method:

 1. polling
 2. intr
 3. wr 0x70 to mem to get status

> 9.1.6 READ STATUS (70h)
> The W29N02GW/Z has an 8-bit Status Register which can be read during device operation. Refer to Table 9.3 for specific Status Register definitions. After writing 70h command to the Command Register, read cycles will only read from the Status Register. The status can be read from I/O[7: 0] outputs, as long as #CE and #RE are LOW. Note; #RE does not need to be toggled for Status Register read. The Command Register remains in status read mode until another command is issued. To change to normal read mode, issue the PAGE READ (00h) command. After the PAGE READ command is issued, data output starts from the initial column address.

<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200" viewBox="0 0 1130 325" style="display:block;margin:0 auto;"><g style="stroke:#000!important;stroke-width:2.5!important;fill:none!important;stroke-linecap:round!important;stroke-linejoin:round!important;"><path d="M95 28 H148 L162 50 H1115"/><path d="M95 112 H352 L365 90 H430 L438 112 H1115"/><path d="M95 153 H373 L385 175 H405 L418 153 H1115"/><path d="M95 215 H650 L662 237 H815 L828 215 H1115"/><line x1="95" y1="282" x2="374" y2="282"/><polygon points="374,282 386,270 414,270 426,282 414,294 386,294"/><line x1="426" y1="282" x2="689" y2="282"/><polygon points="689,282 701,270 837,270 849,282 837,294 701,294"/><line x1="849" y1="282" x2="1115" y2="282"/><line x1="435" y1="73" x2="652" y2="73"/><polyline points="443,67 435,73 443,79"/><polyline points="644,67 652,73 644,79"/><line x1="435" y1="78" x2="435" y2="118"/><line x1="652" y1="78" x2="652" y2="244"/><line x1="652" y1="188" x2="689" y2="188"/><polyline points="660,182 652,188 660,194"/><polyline points="681,182 689,188 681,194"/><line x1="689" y1="180" x2="689" y2="314"/></g><g style="font-family:'Maple Mono','Maple Mono NF','Maple Mono CN',monospace;fill:#000!important;stroke:none!important;"><text x="20" y="48" style="font-size:19px;">#CE</text><text x="20" y="111" style="font-size:19px;">CLE</text><text x="20" y="174" style="font-size:19px;">#WE</text><text x="20" y="236" style="font-size:19px;">#RE</text><text x="20" y="291" style="font-size:19px;">I/Ox</text><text x="532" y="66" style="font-size:17px;">tCLR</text><text x="654" y="174" style="font-size:17px;">tREA</text><text x="400" y="282" text-anchor="middle" dominant-baseline="middle" style="font-size:15px;">70h</text><text x="769" y="282" text-anchor="middle" dominant-baseline="middle" style="font-size:14px;">Status Output</text></g></svg>

### 写0x70读存储器状态原因

AE之所以采用写0x70模式，原因是ST的库普遍采取这种方式，但==ST并不支持我们出问题的这种ecc_mode==。

### 写0x70读存储器状态的返回

读取存储器状态后，为了返回读数据状态需要写0x00返回。但存储器文档中写的是（为了返回普通读模式），有可能==含ecc功能的读模式不属于文档中讲到的读模式，所以不应写0x00命令。==

### ecc_mode介绍

ecc_mode: 0x10的特点：在存储器接口上，读block n后，==硬件自动写读取ecc值的命令==，硬件自动读取ecc值。

ecc_mode: 0x01的特点：在存储器接口上不存在写读取ecc值的命令。

### Coding

- 编写case，在普通读模式下，写0x70读存储器状态成功
- 编写case，复现err

![image-20260528105559926](https://pic.lllincx.cn/image-20260528105559926.png)

### 波形现象

有reg表示smc发出数据的周期长度，如果是发送命令，周期长度应为5。在发送0x00后，reg数值变更为2，导致写读取ecc值的命令无法发送成功。

### 结论

写「0x70读存储器状态」，并「写0x00返回普通读模式」打断了ecc_mode: 0x10条件下，ecc读模式下在读取block数据中穿插「硬件写读取ecc值的命令」的完整流程。ecc_mode: 0x01条件下，不存在「硬件写读取ecc值的命令」情况，因此不受影响。
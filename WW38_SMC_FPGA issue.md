## nand

why clr/ar count from rise edge
depending on value of nand _csel_
clr/ar/rr rea diff from device and ctrl name and

## Nor

**tpc** (page cycle time)
**ttr** (turnaround time): Mainly for sync mem; effect on async TBD 

### 关于Tpc case构建的情况

nor tpc的用法，似乎应用场景是突发读写。目前我们现有的case没有用突发，是在C代码里递增的。所以要测试这个需要开发case：要求smc突发读写存储器


### 关于Ttr case构建的情况

ttr的case也比较困难，因为现在的case不论是单个word写，还是连续写，在写之后都是要等中断的。这之后才开始读。这中间的时间肯定超过ttr了，所以这个改了之后波形也不会有区别
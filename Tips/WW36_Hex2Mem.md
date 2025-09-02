```
cd SOC_PT105_VERIFY/bin
ihex2mem32.pl ***.hex  //gen ***.mem
addecc_for_pt105.pl ***.mem ***.hex //convert ***.mem to wanted hex
cp ***.hex sim/$MODULE/$CASE
```
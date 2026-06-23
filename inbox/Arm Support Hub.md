### DMA allch_ctrl

> Why are the req and ack signals of the DMA's allch_stop/pause_nonsec/sec tied together? In our design, how do you recommend these ports be connected?

The example subsystem does not utilize the stop and pause control of the DMA.

These might be useful in certain scenarios: the stop clears the DMAC tasks, the pause function allows checking the current values of registers, or to pausing the DMA unit for a while to free up bus infrastructure resources. 

For implementation details, see section 3.1.7, Stop and pause integration, in the DMA-350 Controller Configuration and Integration Manual.

"The stop interface is built up from a simple 4-phase handshake. The allch_stop_req_nonsec is a stop request for all Non-secure channels. When asserted, all Non-secure channels that are not in IDLE are stopped. When all Non-secure channels are stopped or inactive the DMA-350 answers with asserting allch_stop_ack_nonsec. The integrator must ensure that the 4-phase handshake is followed by the stop_req signals.

The pause interface is also built up from a simple 4-phase handshake. The allch_pause_req_nonsec is a pause request for all Non-secure channels. When asserted, all Non-secure channels that are not in IDLE are paused. When all Non-secure channels are paused or inactive the DMA-350 answers with asserting allch_pause_ack_nonsec. The integrator must ensure that the 4-phase handshake is followed by the pause_req signals"



You can also generate and example of the DMA (CG096) that has a dedicated OOB testbench.

Please let us know if you have any further questions.

---

### MPC clk issue

> The MPC connects to both the AXI and APB buses, but the MPC has only a single clock. When the MPC is integrated into a system, attention should be paid to what conditions this clock must satisfy.

I think the most common choice is running MPC on AXI clock and then ensuring APB-to-MPC path is synchronized.

> How to handle APB and AXI running at different clock frequencies?

You could use an async bridge between MPC and APB master.

> 我重新描述一下我的问题。
>
> 我的axi总线与apb同步，但频率更高。当apb对mpc进行寄存器读写时，传输的信号将被axi的高频时钟多次采集，实际上会存在重复读写的情况。
>
> 一般的设计为了避免这种问题，如果不同时具有aclk和pclk，那么会有pclken。但是mpc不具有
>
> 为了避免以上我提到的问题，在集成时应该做怎样的处理

Usually the path of APB is like "interconnect -> ppc -> mpc". I'm not sure how you integrate the mpc and where protocol switches from AHB(or AXI?) to APB. But I think that is where you could add an AHB to AHB sync up bridge(because I couldn't find an APB to APB sync up bridge). As to the clk_en, I think you could generate it manually.
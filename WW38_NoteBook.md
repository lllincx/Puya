# 9.15 Mon

### TrustEngine

- confirm OTP SPEC done and submit
- finish OTP variable (page 5.6.7) case and push
- add OTP fixed (page 2.3.4) case and push
- join meeting on ACA SRAM clear under TAMP hacking

### SMC

- Update SPEC

# 9.16 Tue

### TrustEngine

- Support Liu Xiande for understanding OTP SPEC
- Support Shawn for verifying OTP page 2.3.4 prg and chk
- DBG wr lcs = 7, but rd lcs = f

### SMC

- update SPEC

# 9.17 Wed

### TrustEngine

- **explain why "wr lcs = 7, but rd lcs = f"**: lcs[3] reserved for hardware use, software shoud not read it.
- **Found issue**: **user sec/no-sec area** too small (8B). Data meant for user secure area wrongly placed in test area, but no impact on most accesses. TrustEngine read perms differ but ignorable since always readable in flash. Reason flash is always readable: to verify successful writes.

### SMC

- update SPEC, mainly ECC.

# 9.18 Thu

### SMC

- Update SPEC. [[WW38_SMC_ECC SPEC]]
- Run and chk ECC case for wr SPEC.

### TrustEngine

- opt case for page 2.3.4
  - add selfcheck func during LCS=DD/DR for preset LCS
  - add selfcheck func during LCS=DD/DR for inc LCS
  - cfm key access perm duing invaild LCS

# 9.19 Fri

# Weekly Report

# To-do

ecc spec : simply as ST SPEC
add OTP case: page 2.3.4 rd perm during invalid LCS such as 101.

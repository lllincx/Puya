1. 注意关注pclken相关case波形是否符合需求
2. 变更pready为1
3. OSPI到dmax的req type包括single，last和req，需要被验证完全
4. dmax trigger wrapper多驱
5. 补充lint cdc report
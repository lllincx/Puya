tag存放位置:
```
/PRODUCT_MCU/PT106/V1/_gitview/common/tag/pt106_soc_dv.tag
```
脚本存放位置:
```
/PRODUCT_MCU/PT106/V1/_gitview/common/script/get_db.py
```

```
get_db.py [-h] -w WORKSPACE -t TAG [-u] (-p PROJECT | -d DIRECTORY)

-h, --help, show this help message and exit
-w, WORKSPACE, --workspace, WORKSPACE workspace name to be created
-t, TAG, --tag, TAG Local file to store the module list to be processed; or Git linkage for modules list
-u,--update, Update existed workspace with specified tag
-p, PROJECT, --project PROJECT specify project name
-d, DIRECTORY, --directory DIRECTORY specify workspace path
```

Workspace 缺省创建目录根据本地工作目录(/PRODUCT_MCU/\$project/V1/\_gitview/\$user)规定推导而来,\$project 是-p 参数传入，$user 子目录 如果不存在，脚本会自动创建。脚本也支持用-d 将 workspace 创建到强制指定的可写路径，-d 和-p 是互 option，两者只能跟一个.

-u 表示只在已有的\$workspace 上根据指定 tag list 更新 database,如果指定的$workspace 不存在，脚本提醒你是否新建。

```
get db. py -w pt088 init -t ../tag/pt088_soc_init_release_20240410.tag -p PT088
```

![[Pasted image 20250418105857.png]]
![[Pasted image 20250418110035.png]]

==切记：如果是按照TAG（不是latest）创建的本地仓库，脚本会自动用指定tag在本地创建一个同名的branch 并切换到这个branch下，所以在这个本地仓库的任何改动都会在这个branch上进行，所以有仓库owner 想在用脚本创建的 database 更改仓库内容，一定要先切换到master分支再进行更改操作==
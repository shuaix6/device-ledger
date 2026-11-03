# 报错病历卡 · errors.md

> 每踩一个报错，在这里存一张"病历卡"。下次再见同一个报错 → 直接翻这里，不用重新查、重新猜。
>
> **五栏格式**（新卡照这个写）：
> ① 最小复现　② 报错原文　③ 中文意思　④ 修法　⑤ 我为什么会犯
>
> **最关键的是"最小复现"** —— 把问题缩到最小能复现的几行代码。这是工程师的核心习惯：将来调 RAG 效果，唯一有效的手段就是"把出问题的那一小段单独拎出来跑"。
>
> 已建档 **21 张**（截至 2026/11/03）｜遇到**新类型**的报错就往下加一张；同类报错再次出现不新建，合并到老卡当"变种"。

## 索引

| 报错 | 一句话 | 卡号 |
|---|---|---|
| NameError | 名字不认识（拼错） | 01 |
| TypeError | 类型对不上 | 02 · 03 · 04 · 10 · 19 |
| SyntaxError | 句子读不通 | 05 · 11 · 12 |
| IndentationError | 缩进层级对不上 | 06 |
| IndexError | 索引越界 | 07 |
| ValueError | 类型对、值不对 | 08 |
| KeyError | 字典里没有这把钥匙 | 09 |
| FileNotFoundError | 文件没找到（不在这个文件夹） | 18 |
| LookupError | 编码名不存在（密码本名字写错） | 20 |
| AttributeError | 对象身上没这个属性（逗号写成了点号） | 21 |
| （附）KeyboardInterrupt | 不是错误——按 Ctrl+C 叫停的痕迹 | — |

---

## 【病历卡 01】NameError · 名字拼写错误

· 最小复现：`pritn("hello")`
· 报错原文：`NameError: name 'pritn' is not defined. Did you mean: 'print'?`
· 中文意思：用了一个 Python 不认识的名字——拼错了
· 修法：对照拼写改正（`pritn` → `print`）；Python 通常直接提示正确拼写
· 我为什么会犯：手打太快，字母顺序打反

## 【病历卡 02】TypeError · 字符串和数字不能拼接

· 最小复现：`print("25" + 1)`
· 报错原文：`TypeError: can only concatenate str (not "int") to str`
· 中文意思：字符串只能跟字符串拼接，不能拼一个整数
· 修法：`int("25") + 1`（文字→数字）或 `"25" + str(1)`（数字→文字）
· 我为什么会犯：忘了"引号决定命运"——带引号的 "25" 是文字，不能直接参与数学运算

## 【病历卡 03】TypeError · 字符串和数字不能比较

· 最小复现：`print("5" < 3)`
· 报错原文：`TypeError: '<' not supported between instances of 'str' and 'int'`
· 中文意思：字符串和整数之间不支持比大小
· 修法：把 "5" 转成数字再比较：`int("5") < 3`
· 我为什么会犯：数据从 input() 进来时是字符串，忘了先转换就直接比较

## 【病历卡 04】TypeError · 变量名打错成内置类型

· 最小复现：`total = tuple + i`（想累加，却把变量名 `total` 打成了 `tuple`）
· 报错原文：`TypeError: unsupported operand type(s) for +: 'tuple' and 'int'`
· 中文意思：tuple（元组）和 int（整数）不能相加
· 修法：把 `tuple` 改回 `total`
· 我为什么会犯：拼写打错，而 `tuple` 恰好是 Python 内置类型名——拼错成"真实存在的词"时，报的是 TypeError 而不是 NameError，更隐蔽

## 【病历卡 05】SyntaxError · 一个等号当比较

· 最小复现：`if fault_code = "E01":`
· 报错原文：`SyntaxError: invalid syntax. Maybe you meant '==' or ':' instead of '='?`
· 中文意思：语法错误——这里该用比较运算符
· 修法：比较用 `==`。口诀：一个等号干活（赋值），两个等号提问（比较）
· 我为什么会犯：赋值和比较记混了

## 【病历卡 06】IndentationError · 缩进层级对不上

· 最小复现：同一个块里，第一行缩进 4 格、第二行缩进 2 格
· 报错原文：`IndentationError: unindent does not match any outer indentation level`
· 中文意思：往回收缩进时，退到的位置不属于任何一个已有层级
· 修法：同一块内缩进保持一致；退出块时精确退回外层原位（不能停在"半层"）
· 我为什么会犯：以为"缩进几格随便"——实际 Python 管的是**一致性**：同块内不一致就报错
· **变种（2026/11/03）**：`IndentationError: expected an indented block after 'with' statement on line 6`
　方向**相反**：不是"退错层"，是"该缩进却顶格"。`with open(...) as f:` 结尾有冒号，下一行必须缩进 4 格。
　凡行末有冒号（`with` / `if` / `for` / `def` / `try` / `else`），下一行必定缩进。
　当天连犯三处（`day8_json_rw.py` 三个 `with` 全部顶格）—— 原因：一行一行改，没看整块结构。

## 【病历卡 07】IndexError · 索引越界

· 最小复现：`devices = ["数控机床", "工业机器人"]` 然后 `print(devices[10])`
· 报错原文：`IndexError: list index out of range`
· 中文意思：索引超出了列表的合法范围
· 修法：合法索引 = 0 到 len(列表)-1；取最后一个用 `[-1]` 最稳
· 我为什么会犯：数元素时想"第 5 个就是 [5]"，但索引从 0 起——5 个元素的最大索引是 4

## 【病历卡 08】ValueError · 类型对，但值不对

· 最小复现：`int("你好")`
· 报错原文：`ValueError: invalid literal for int() with base 10: '你好'`
· 中文意思：这串字不是合法的数字写法，没法按十进制转成整数
· 修法：确保输入内容是数字；正式兜底用 try/except 接住（第 3 周学）
· 我为什么会犯：input() 接收的一切都是文字——"用户输入不可信"，输入"你好"时转换就炸了

## 【病历卡 09】KeyError · 字典里没有这把钥匙

· 最小复现：`device = {"name": "数控机床"}` 然后 `print(device[0])`
· 报错原文：`KeyError: 0`
· 中文意思：字典里没有一把叫 `0` 的钥匙
· 修法：先用 `if key in device:` 探路再取值；或核对键名拼写
· 我为什么会犯：把字典当列表用（报了"编号"）——字典认的是"名字"，不认编号

## 【病历卡 10】TypeError · 参数数量对不上

· 最小复现（少）：定义 `def greet(name):` 却调用 `greet()`
　→ `TypeError: greet() missing 1 required positional argument: 'name'`
· 最小复现（多）：定义 `def say_hello():` 却调用 `say_hello(1)`
　→ `TypeError: say_hello() takes 0 positional arguments but 1 was given`
· 中文意思：调用时给的参数数量和函数定义对不上——多了或少了
· 修法：先看函数定义有几个参数，调用时对应给足；多余的删掉
· 我为什么会犯：还没养成"先看定义、再调用"的习惯

## 【病历卡 11】SyntaxError · 全角标点混入代码

· 最小复现：`print("x是什么？"，x)`（第二个逗号是中文全角）
· 报错原文：`SyntaxError: invalid character '，' (U+FF0C)`
· 中文意思：非法字符——中文标点不能出现在代码结构里
· 修法：引号**外**（代码结构）必须半角；引号**内**（文字内容）中文标点随便用
· 我为什么会犯：输入法停在中文状态没切回来

## 【病历卡 12】SyntaxError · 容器项之间缺逗号

· 最小复现：`device = {"name": "数控机床" "model": "CNC-850"}`（两个键值对之间漏了逗号）
· 报错原文：`SyntaxError: invalid syntax`（报错行号常指向**下一行**开头）
· 中文意思：字典 / 列表的项之间必须用逗号分隔
· 修法：每项结尾补逗号（最后一项的逗号可留可不留）
· 我为什么会犯：以为"分了行就等于分开"——Python 不认换行（括号内），只认逗号

## 【病历卡 13】ValueError · mode 只认代号

· 最小复现：`open("a.txt", "read")`
· 报错原文：`ValueError: invalid mode: 'read'`
· 中文意思：无效的模式：'read'——这个位置只认代号（"r"/"w"/"a"），不认英文全称
· 修法：写成 `"r"`（写文件 "w"、追加 "a"）
· 我为什么会犯：以为"写全称更清楚"——它偏偏只认单字母代号（连 "read" 都不行）

## 【病历卡 14】SyntaxError · 续行符（\）后面还有字符

· 最小复现：`f = open("device_info.txt","r"\)`（行尾残留一个反斜杠）
· 报错原文：`SyntaxError: unexpected character after line continuation character`
· 中文意思：续行符（\）后面出现了意外字符——`\` 的岗位是"站行尾"，表示下一行接着写
· 修法：删掉多余的 `\`（删参数时别留"孤儿字符"）
· 我为什么会犯：删除行尾内容时手滑留下一截

## 【病历卡 15】SyntaxError · 少了冒号

· 最小复现：`for line in f`（行尾没有冒号）
· 报错原文：`SyntaxError: expected ':'`
· 中文意思："我期待一个冒号"——凡"带下级"的句子（for / if / def）行尾必须有冒号
· 修法：补上——`for line in f:`
· 我为什么会犯：手打时顾着内容，漏掉了行尾标点

## 【病历卡 16】UnicodeDecodeError · 密码本不匹配

· 最小复现：一个用 UTF-8 存的中文 txt，用 `open("x.txt", "r")` 去读（没带 encoding）
· 报错原文：`UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 4: illegal multibyte sequence`
· 中文意思：GBK 解码器解不动——文件是"UTF-8 密码本"写的，程序却拿"GBK 密码本"去读
· 修法：`open("x.txt", "r", encoding="utf-8")`
· 我为什么会犯：不知道"读中文文件必须带保险栓"——所以删掉它，报错立刻现形（这卡就是这么来的）

## 【病历卡 17】静默怪输出 [[...]] · 循环引用（不报错的 bug）

· 最小复现：`a = []; a.append(a); print(a)` → `[[...]]`
· "报错原文"：（没有报错！输出长这样）`[[...], [...], [...], [...]]`
· 中文意思：列表装了自己（循环引用）——`devices.append(devices)` 把"仓库"推进了"仓库"
· 修法：`devices.append(device)`（少一个 s，推的是"一台设备"）
· 我为什么会犯：`device` / `devices` 差一个字母——形近字手滑（这类 bug 不喊不叫，只能靠"输出和预期对不上"抓）

## 【病历卡 18】FileNotFoundError · 文件没找到

· 最小复现：`open("不存在的文件.txt", "r", encoding="utf-8")`
· 报错原文：`FileNotFoundError: [Errno 2] No such file or directory: '不存在的文件.txt'`
· 中文意思：找不到这个文件——程序在文件夹里找了一圈，没有叫这个名字的文件
· 修法：① 查文件名拼写和扩展名（`.txt` 别丢）② 确认文件就在程序同一文件夹 ③ 兜底用 `except FileNotFoundError as e:` 接住
· 我为什么会犯：文件被删 / 改名 / 移走，或名字打错——程序只认"一字不差的名字"（和 split 的刀一个道理：对不上就找不到）

## 【病历卡 19】TypeError · 内置函数名被"占用"（is not callable）

· 最小复现：`print = 27.2` 然后 `print("——")`
· 报错原文：`TypeError: 'float' object is not callable`
· 中文意思："float 不可被调用"——`print("——")` 的括号是"调用"（叫它干活），但此刻 `print` 里装的是数字，不是函数
· 修法：别给内置函数名（print / input / len / int……）赋值；撞了就删掉/改掉那行赋值、重跑
· 我为什么会犯：累加语句写了两遍，其中一遍把 `total` 错打成 `print`——`print = ...` 是**合法赋值**（当场不报错），直到真正"调用 print"时才炸（**埋在第 16 行、炸在第 19 行**）

## 【病历卡 20】LookupError · 编码名不存在（uft-8 手滑专场）

· 最小复现：`open("x.txt", "r", encoding="uft-8")`
· 报错原文：`LookupError: unknown encoding: uft-8`
· 中文意思："未知编码：uft-8"——Python 翻它的"编码名册"没找到这个名字（它还会把你写的名字原样报出来）
· 修法：改回 `utf-8`（u-t-f 顺序）；以后见 `LookupError` → 第一反应查字母顺序
· 我为什么会犯：`utf` 三个字母里 `f` 和 `t` 打反（uft）——**第二次犯了**（`day7_write.py` 首发、`day8_json_rw.py` 再犯）；特点：**open 当场就炸**（还没读到内容呢）——对比卡 16 的 UnicodeDecodeError 是"拿错本子、读时才炸"

---

## 【病历卡 21】AttributeError · 逗号写成了点号

· 最小复现：`json.dump(data.f)`（本该是 `json.dump(data, f)`）
· 报错原文：`AttributeError: 'list' object has no attribute 'f'`
· 中文意思："列表这种对象，没有名叫 `f` 的属性"——`.` 在 Python 里不是标点，是"从左边这个对象里取一样东西"
· 修法：`json.dump(data, f)`——**逗号是"给两个参数"，点是"从里面取一个"**
· 我为什么会犯：把"参数分隔"和"属性访问"混成一件事。而且 `data.f` 是**合法语法**，Python 不会说"你少了个逗号"，它会认真去取属性，取不到才报错——报错信息里根本不提逗号，盯着那行看也看不出来
· 附带代价：`open(..., "w")` 已经执行，文件在 `json.dump` 报错**之前**就被清成 **0 字节**，靠 `devices_backup.json` 恢复

---

## 附 · KeyboardInterrupt（不是错误，是"叫停"）

· 场景：死循环刷屏不停时，按 `Ctrl + C`
· 含义：这是"被人为叫停"的痕迹，不是代码错误
· 用途：程序跑飞/卡住时的急停按钮——所有程序员的第一反应

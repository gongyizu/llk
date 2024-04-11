[adventurer](https://github.com/jz51/adventurer.git)

[anony](https://github.com/sina1680/python)

[startup](https://github.com/wangshunping/Starup-Game-Python?tab=readme-ov-file)

### wolfman ###
```
# -*- coding:utf-8 -*-
import time
import random

HUATI = False
SHOUQIANG = False
HUOBAN = False
SANDANQIANG = False
active = True
变量 = input("请输入你的名字：")
time.sleep(random.randint(1, 2))
print("欢迎你，" + 变量 + "!")
time.sleep(random.randint(1, 2))
print("全部22个游戏成就：")
time.sleep(random.randint(1, 2))
print(
    "不辨是非    幸存者    新生活    伙伴    \n崖壁的碰撞    狼腹    碎肉    西线的尽头"
)
print(
    "与狼共舞    东线的尽头    狼王现身    狼群\n高风亮节    囫囵吞枣    狼子野心    聪明反被聪明误"
)
print("鄙夷的眼神    抵抗    首领的死亡    村庄英雄\n村庄联盟    人狼之战    反客为主")
time.sleep(random.randint(1, 2))
print("本游戏共有六大结局，加油，少侠！")
time.sleep(random.randint(1, 2))
print("加载游戏剧情中…………")
time.sleep(3)
print("这是一个月圆之夜……")
time.sleep(random.randint(1, 2))
print("村子里召开了一年一次的屠杀狼人活动，将要去杀死狼人的人被称作屠狼师。")
time.sleep(random.randint(1, 2))
print("而你，是这里最具有天赋的屠狼师。")
time.sleep(random.randint(1, 2))
print("村子里，暗藏杀机；野外，阴险无比。")
time.sleep(random.randint(1, 2))
变量1 = input("首领找到你，问你：‘" + 变量 + "，你是否要出去屠狼？’ 1：是 其他按键：否")
time.sleep(1)
if 变量1 != "1":
    print("你选择留守在村子里。")
    time.sleep(random.randint(1, 2))
    print("首领虽无可奈何，也没强求。")
    time.sleep(random.randint(1, 2))
    print("这天傍晚，有一个人闯入你家，说是首领要求来的，请求进来。")
    time.sleep(random.randint(1, 2))
    变量2 = input("你要让他进来吗？ 1：是 其他：否")
    time.sleep(random.randint(1, 2))
    if 变量2 == "1":
        print("你同意了他的请求。")
        time.sleep(random.randint(1, 2))
        print("这个人是个狼人，你尝试反抗，但是你没有武器，最后被残忍地杀害了。")
        time.sleep(random.randint(1, 2))
        print("————解锁成就：不辨是非————")
        time.sleep(random.randint(1, 2))
        print("你死了…………游戏结束")
        time.sleep(random.randint(1, 2))
        print("欢迎再度游玩！")
    else:
        print("你拒绝了他的请求。")
        time.sleep(random.randint(1, 2))
        print("到了晚上，你一个人坐在家中。")
        time.sleep(random.randint(1, 2))
        print("一群狼人在潜伏在村子里的狼王的带领下，冲进了村子。")
        time.sleep(random.randint(1, 2))
        print("村子里所有的人都被杀死了，除了你。")
        time.sleep(random.randint(1, 2))
        print("————解锁成就：幸存者————")
        time.sleep(random.randint(1, 2))
        变量3 = input("你是否要尝试去寻找狼王并复仇？1：是 其他：否")
        time.sleep(random.randint(1, 2))
        if 变量3 == "1":
            print("你踏上了寻找狼王的道路。")
            time.sleep(random.randint(1, 2))
            while active:
                变量4 = input("你要从哪个方向出发？1=东线 其他=西线")
                if 变量4 == "1":
                    time.sleep(random.randint(1, 2))
                    print("你继续向前前进，来到了一片森林，")
                    time.sleep(random.randint(1, 2))
                    print(
                        "在路边搜索，发现了一张白纸，上面写有这么一行字：‘23124E’，"
                    )  # 本茨·拉登
                    time.sleep(random.randint(1, 2))
                    print("你来到了两个建筑前。")
                    time.sleep(random.randint(1, 2))
                    变量4 = input("你要去哪个建筑？1=教堂 其他=钟楼")
                    if 变量4 == "1":
                        time.sleep(random.randint(1, 2))
                        print("你没有找到任何线索。")
                    else:
                        time.sleep(random.randint(1, 2))
                        print("你找到了一张小纸片，上面有几个数字：1 1 2 1 Language")
                    time.sleep(random.randint(1, 2))
                    print("你继续前行，来到了悬崖边。")
                    time.sleep(random.randint(1, 2))
                    print("这时，你找到了一串绳索。")
                    time.sleep(random.randint(1, 2))
                    变量5 = input("是否使用绳索前往悬崖下面寻找线索？1=是 其他=否")
                    if 变量5 == "1":
                        time.sleep(random.randint(1, 2))
                        print("你使用了绳索。")
                        time.sleep(random.randint(1, 2))
                        print("你刚下去，绳索突然断了，你坠崖身亡。")
                        time.sleep(random.randint(1, 2))
                        print("————解锁成就：崖壁的碰撞————")
                        time.sleep(random.randint(1, 2))
                        print("你死了…………游戏结束")
                        time.sleep(random.randint(1, 2))
                        print("欢迎再度游玩！")
                        break
                    else:
                        if HUATI:
                            time.sleep(random.randint(1, 2))
                            print("你安上了滑梯，滑了下去，安全着陆。")
                            time.sleep(random.randint(1, 2))
                            print("你继续前行，发现了一具尸体，")
                            time.sleep(random.randint(1, 2))
                            变量6 = input("是否搜查尸体全身？1=是 其他=否")
                            if 变量6 == "1":
                                time.sleep(random.randint(1, 2))
                                print(
                                    "这是一具假的尸体，狼人就在附近，你专心搜查尸体时狼人一跃而起，将你杀死。"
                                )
                                time.sleep(random.randint(1, 2))
                                print("————解锁成就：狼腹————")
                                time.sleep(random.randint(1, 2))
                                print("你死了…………游戏结束")
                                time.sleep(random.randint(1, 2))
                                print("欢迎再度游玩！")
                                break
                            else:
                                time.sleep(random.randint(1, 2))
                                print("你放弃了搜查。")
                                time.sleep(random.randint(1, 2))
                                print("你来到了一个山谷，下面有4个狼人，")
                                time.sleep(random.randint(1, 2))
                                变量8 = input("你是否下去？1=是 其他=否")
                                if 变量8 == "1":
                                    time.sleep(random.randint(1, 2))
                                    print("你选择了直接下去。")
                                    time.sleep(random.randint(1, 2))
                                    print("狼人们直接扑向了你，你被撕咬而死。")
                                    time.sleep(random.randint(1, 2))
                                    print("————解锁成就：与狼共舞————")
                                    time.sleep(random.randint(1, 2))
                                    print("你死了…………游戏结束")
                                    time.sleep(random.randint(1, 2))
                                    print("欢迎再度游玩！")
                                    break
                                else:
                                    time.sleep(random.randint(1, 2))
                                    print("你选择了不下去。")
                                    if SHOUQIANG:
                                        time.sleep(random.randint(1, 2))
                                        print(
                                            "你使用了手枪，杀死了所有的狼人，得到了一张纸，"
                                        )
                                        time.sleep(random.randint(1, 2))
                                        print(
                                            "上面写道：本卡茨夫拉瓦得登，8选4，联络首领，首领名字2 · 2"
                                        )
                                        time.sleep(random.randint(1, 2))
                                        print(
                                            "东线已走至尽头，你返回了村庄，你要杀死狼王，为村民们报仇。"
                                        )
                                        time.sleep(random.randint(1, 2))
                                        print("————解锁成就：东线的尽头————")
                                        变量9 = input("是时候宣布了，谁是狼王？")
                                        if 变量9 == "本茨·拉登":
                                            time.sleep(random.randint(1, 2))
                                            print("你来到了本茨·拉登的家里。")
                                            time.sleep(random.randint(1, 2))
                                            print("你进入了他的家，发现了许多狼毛。")
                                            time.sleep(random.randint(1, 2))
                                            print("他，就是狼王！")
                                            time.sleep(random.randint(1, 2))
                                            print(
                                                "你等在门后，看到他回来，一枪打死了他。"
                                            )
                                            time.sleep(random.randint(1, 2))
                                            print("————解锁成就：狼王现身————")
                                            time.sleep(random.randint(1, 2))
                                            print(
                                                "后记：你杀死了狼王，群狼失去首领，一个接一个的被捕杀了，自此，这一带，再也没有狼人的踪迹。"
                                            )
                                            time.sleep(random.randint(1, 2))
                                            print("剧情1完结——")
                                            time.sleep(random.randint(1, 2))
                                            print("游戏结束——")
                                            time.sleep(random.randint(1, 2))
                                            print("欢迎再度游玩！")
                                            break
                                        else:
                                            time.sleep(random.randint(1, 2))
                                            print(
                                                "你找到了"
                                                + str(变量9)
                                                + "，开枪打死了他。"
                                            )
                                            time.sleep(random.randint(1, 2))
                                            print("他不是狼人！")
                                            time.sleep(random.randint(1, 2))
                                            print("你害怕的往后退，撞到了一个人。")
                                            time.sleep(random.randint(1, 2))
                                            print(
                                                "你回头一看，惊愕了：他才是真正的狼王！"
                                            )
                                            变量10 = input(
                                                "他邀请你加入他们，是否加入？1：是 其他按键：否"
                                            )
                                            if 变量10 == "1":
                                                time.sleep(random.randint(1, 2))
                                                print("你选择了加入他们。")
                                                time.sleep(random.randint(1, 2))
                                                print("————解锁成就：狼群————")
                                                time.sleep(random.randint(1, 2))
                                                print(
                                                    "后记：你加入了狼群，被改造成了狼人，并成为了新的首领，成为了大名鼎鼎的狼王"
                                                    + 变量
                                                    + ","
                                                )
                                                time.sleep(random.randint(1, 2))
                                                print("    村子里的人对你深恶痛绝。")
                                                time.sleep(random.randint(1, 2))
                                                print(
                                                    "    终于有一天，你和你的同伴们死在了一个围阵中，结束了你的一生。"
                                                )
                                                time.sleep(random.randint(1, 2))
                                                print("剧情2完结——")
                                                time.sleep(random.randint(1, 2))
                                                print("游戏结束——")
                                                time.sleep(random.randint(1, 2))
                                                print("欢迎再度游玩！")
                                                break
                                            else:
                                                time.sleep(random.randint(1, 2))
                                                print("你选择了拒绝。")
                                                time.sleep(random.randint(1, 2))
                                                print("狼王十分恼怒，当即将你杀死。")
                                                time.sleep(random.randint(1, 2))
                                                print("————解锁成就：高风亮节————")
                                                time.sleep(random.randint(1, 2))
                                                print("你死了…………游戏结束")
                                                time.sleep(random.randint(1, 2))
                                                print("欢迎再度游玩！")
                                                break
                                    else:
                                        time.sleep(random.randint(1, 2))
                                        print("你已没有退路，只得返回。")
                                        continue
                        else:
                            time.sleep(random.randint(1, 2))
                            print("你将绳索抛弃。")
                            time.sleep(random.randint(1, 2))
                            print("已经无路可退，你选择返回村庄。")
                            time.sleep(random.randint(1, 2))
                            print("你返回了村庄，休整了一会再度出发。")
                            continue
                else:
                    time.sleep(random.randint(1, 2))
                    print("你前往了西线。")
                    time.sleep(random.randint(1, 2))
                    print("你在西线一个地方的一个角落里找到了滑梯。")
                    HUATI = True
                    变量6 = input("是否返回？1=是 其他=否")
                    if 变量6 == "1":
                        continue
                    else:
                        time.sleep(random.randint(1, 2))
                        print("你选择了不返回。")
                        time.sleep(random.randint(1, 2))
                        print("你一路向前，来到了一条小河边，得到了一个手机，")
                        time.sleep(random.randint(1, 2))
                        变量7 = input("是否打开？ 1=是 其他=否")
                        if 变量7 == "1":
                            time.sleep(random.randint(1, 2))
                            print("你打开了手机。")
                            time.sleep(random.randint(1, 2))
                            print("手机突然爆炸了，你被炸成了碎块。")
                            time.sleep(random.randint(1, 2))
                            print("————解锁成就：碎肉————")
                            time.sleep(random.randint(1, 2))
                            print("你死了…………游戏结束")
                            time.sleep(random.randint(1, 2))
                            print("欢迎再度游玩！")
                            break
                        else:
                            time.sleep(random.randint(1, 2))
                            print("你选择了不打开手机。")
                            time.sleep(random.randint(1, 2))
                            print(
                                "你继续往前走，看到了一张纸条，上面写有‘eniaeng’，背面还有落款‘2114PY’，"
                            )
                            time.sleep(random.randint(1, 2))
                            print("你好像知道了什么……")
                            time.sleep(random.randint(1, 2))
                            print("你找到了一把枪。")
                            SHOUQIANG = True
                            time.sleep(random.randint(1, 2))
                            print("路走到了尽头，你选择了返回。")
                            time.sleep(random.randint(1, 2))
                            print("————解锁成就：西线的尽头————")
                            continue
        else:
            print("你选择了不去寻找狼王。")
            time.sleep(random.randint(1, 2))
            print("于是，你前往了别的村庄，安家落户，直到死亡。")
            time.sleep(random.randint(1, 2))
            print("————解锁成就：新生活————")
            time.sleep(random.randint(1, 2))
            print("剧情6完结——")
            time.sleep(random.randint(1, 2))
            print("游戏结束——")
            time.sleep(random.randint(1, 2))
            print("欢迎再度游玩！")
else:
    time.sleep(random.randint(1, 2))
    print("你选择了出发。")
    time.sleep(random.randint(1, 2))
    print(
        "你在野外前进，发现了一个人，他自我介绍说他叫莱奥，是个屠狼师，你也自报家门说，我叫"
        + 变量
        + ",他果断要求加入你的队伍，"
    )
    变量11 = input("是否接纳他？1=是 其他=否")
    if 变量11 == "1":
        time.sleep(random.randint(1, 2))
        print("你接纳了他作为伙伴。")
        time.sleep(random.randint(1, 2))
        print("————解锁成就：伙伴————")
        HUOBAN = True
    else:
        time.sleep(random.randint(1, 2))
        print("你没有接纳他。")
    time.sleep(random.randint(1, 2))
    变量12 = input("你走着走着，看到了一扇门，是否进入？1=是 其他=否")
    if 变量12 == "1":
        time.sleep(random.randint(1, 2))
        print("你刚一进去，里面窜出来一条大蟒蛇，将你吞下，")
        time.sleep(random.randint(1, 2))
        print("————解锁成就：囫囵吞枣————")
        time.sleep(random.randint(1, 2))
        print("你死了…………游戏结束")
        time.sleep(random.randint(1, 2))
        print("欢迎再度游玩！")
    else:
        if HUOBAN:
            time.sleep(random.randint(1, 2))
            print(
                "你让莱奥去打头阵，里面窜出一条大蟒蛇将莱奥吞噬，你拔刀杀死了蟒蛇，发现了一把散弹枪，"
            )
            SANDANQIANG = True
            time.sleep(random.randint(1, 2))
            print("你穿过森林，来到了小溪，发现了一群狼人，")
            time.sleep(random.randint(1, 2))
            变量17 = input("你是否要继续前行？1=是 其他=否")
            if 变量17 == "1":
                time.sleep(random.randint(1, 2))
                print("你继续前行，拿出散弹枪，杀死了全部的狼人。")
                time.sleep(random.randint(1, 2))
                print("你在狼人身上发现了一封信，是写给你的，你决定将计就计。")
                time.sleep(random.randint(1, 2))
                print("你如约来到了约定地点，杀死了狼人首领。")
                time.sleep(random.randint(1, 2))
                print("余下的狼人们决定报复你。")
                time.sleep(random.randint(1, 2))
                变量18 = input("你要如何防御？ 1=直接用散弹枪刚  其他=突然袭击")
                if 变量18 == "1":
                    time.sleep(random.randint(1, 2))
                    print("你在乱战中直接开枪，不久，你就杀死了所有的狼人。")
                    time.sleep(random.randint(1, 2))
                    print("你返回了村庄，成为了村庄英雄。")
                    time.sleep(random.randint(1, 2))
                    print("————解锁成就：村庄英雄————")
                    time.sleep(random.randint(1, 2))
                    print(
                        "后记：你以一己之力杀死了所有的狼人这一行为被整个村庄追捧，甚至其余地方的狼人听见"
                        + 变量
                        + "这一名字都胆战心惊，再不敢来犯。"
                    )
                    time.sleep(random.randint(1, 2))
                    print("剧情5完结——")
                    time.sleep(random.randint(1, 2))
                    print("游戏结束——")
                    time.sleep(random.randint(1, 2))
                    print("欢迎再度游玩！")
                else:
                    time.sleep(random.randint(1, 2))
                    print("你选择了突然袭击。")
                    time.sleep(random.randint(1, 2))
                    print(
                        "没想到，狼人们就在你的后面，乘你不注意，窃走了你的散弹枪，将你送上了西天。"
                    )
                    time.sleep(random.randint(1, 2))
                    print("————解锁成就：反客为主————")
                    time.sleep(random.randint(1, 2))
                    print("你死了…………游戏结束")
                    time.sleep(random.randint(1, 2))
                    print("欢迎再度游玩！")
        else:
            time.sleep(random.randint(1, 2))
            print("你没有办法通过，只能绕道前进，")
            time.sleep(random.randint(1, 2))
            print("走了一会，你走到了一个大沙漠里面，")
            time.sleep(random.randint(1, 2))
            print("你走到了一片绿洲里面，")
            time.sleep(random.randint(1, 2))
            print(
                "你在其中发现了一个狼人，你拔刀杀死了他，发现他身上有一串字母，‘LANGQUNZAIXIAOXI’"
            )
            time.sleep(random.randint(1, 2))
            变量13 = input("你要前往：1：小溪 其他：山谷")
            if 变量13 == "1":
                time.sleep(random.randint(1, 2))
                print(
                    "你前往了小溪，发现了狼群，但是你没有武器，无法战胜他们，你杀死了几个狼人后被杀死。"
                )
                time.sleep(random.randint(1, 2))
                print("————解锁成就：狼子野心————")
                time.sleep(random.randint(1, 2))
                print("你死了…………游戏结束")
                time.sleep(random.randint(1, 2))
                print("欢迎再度游玩！")
            else:
                time.sleep(random.randint(1, 2))
                print(
                    "你前往了山谷，发现了你的首领在山下，和一个人谈话，最后，首领让这个人代理狼人首领职务。"
                )
                time.sleep(random.randint(1, 2))
                print("你大吃一惊，不料被首领发现，差点被一枪打死，")
                time.sleep(random.randint(1, 2))
                变量14 = input("你要怎么做？ 1：装死 2：逃离 其他按键：呆在原地不动")
                if 变量14 == "1":
                    time.sleep(random.randint(1, 2))
                    print("你在地上装死，不料被狼人误以为死去，一口将你吞噬，")
                    time.sleep(random.randint(1, 2))
                    print("————解锁成就：聪明反被聪明误————")
                    time.sleep(random.randint(1, 2))
                    print("你死了…………游戏结束")
                    time.sleep(random.randint(1, 2))
                    print("欢迎再度游玩！")
                elif 变量14 == "2":
                    time.sleep(random.randint(1, 2))
                    print("你立即逃离了，首领没有追上你，你安全了。")
                    time.sleep(random.randint(1, 2))
                    print("你离开了山谷，来到了一片麦田，")
                    time.sleep(random.randint(1, 2))
                    变量15 = input("你要怎么做？ 1=装成稻草人  其他=躲起来")
                    if 变量15 == "1":
                        time.sleep(random.randint(1, 2))
                        print("你装成了稻草人。")
                        time.sleep(random.randint(1, 2))
                        print("首领没有发现你，你突然向前，猛地一刀，杀死了首领。")
                        time.sleep(random.randint(1, 2))
                        print("原首领被你杀死了，你返回了村庄，成为了新的首领。")
                        time.sleep(random.randint(1, 2))
                        print("————解锁成就：首领的死亡————")
                        time.sleep(random.randint(1, 2))
                        print(
                            "后记：你成为了新的首领以后，发展军事，成功消灭了所有的狼人。"
                        )
                        time.sleep(random.randint(1, 2))
                        print("剧情3完结——")
                        time.sleep(random.randint(1, 2))
                        print("游戏结束——")
                        time.sleep(random.randint(1, 2))
                        print("欢迎再度游玩！")
                    else:
                        time.sleep(random.randint(1, 2))
                        print("首领没有发现你，你目送首领远去。")
                        time.sleep(random.randint(1, 2))
                        print("你返回村子，向所有村民报告了这一事件，原首领被驱逐。")
                        time.sleep(random.randint(1, 2))
                        print("原首领恼羞成怒，率领狼人们向村庄杀来。")
                        time.sleep(random.randint(1, 2))
                        print(
                            "在混战中，原首领被你杀死，你逃出了包围圈，村民们击退了狼人军团。"
                        )
                        time.sleep(random.randint(1, 2))
                        print("————解锁成就：抵抗————")
                        time.sleep(random.randint(1, 2))
                        变量16 = input("狼人军团被击退，你会：1=修筑工事 其他=购买兵器")
                        if 变量16 == "1":
                            time.sleep(random.randint(1, 2))
                            print("你选择了修筑工事。")
                            time.sleep(random.randint(1, 2))
                            print("当晚，你们正在睡梦中，狼人军团再一次来袭。")
                            time.sleep(random.randint(1, 2))
                            print("他们根据村子里的内应找到了工事的突破口，杀进村庄。")
                            time.sleep(random.randint(1, 2))
                            print("村子被洗劫一空，所有人都被杀害了。")
                            time.sleep(random.randint(1, 2))
                            print("你也死了。")
                            time.sleep(random.randint(1, 2))
                            print("————解锁成就：人狼之战————")
                            time.sleep(random.randint(1, 2))
                            print("你死了…………游戏结束")
                            time.sleep(random.randint(1, 2))
                            print("欢迎再度游玩！")
                        else:
                            time.sleep(random.randint(1, 2))
                            print(
                                "你派出去的人是村子里的间谍，狼人失去内应，找不到突破口。"
                            )
                            time.sleep(random.randint(1, 2))
                            print(
                                "不久，间谍回来，因为没有购买任何武器被你杀死，狼人得知，贸然闯进村庄，被全歼。"
                            )
                            time.sleep(random.randint(1, 2))
                            print(
                                "后记：狼人被全部消灭，你也当上了村子的首领，受大家的拥戴。"
                            )
                            time.sleep(random.randint(1, 2))
                            print("————解锁成就：村庄联盟————")
                            time.sleep(random.randint(1, 2))
                            print("剧情4完结——")
                            time.sleep(random.randint(1, 2))
                            print("游戏结束——")
                            time.sleep(random.randint(1, 2))
                            print("欢迎再度游玩！")
                else:
                    time.sleep(random.randint(1, 2))
                    print("你选择了呆在原地不动。")
                    time.sleep(random.randint(1, 2))
                    print("首领看到你，又给了你一枪，这回直接爆头，你死了。")
                    time.sleep(random.randint(1, 2))
                    print("————解锁成就：鄙夷的眼神————")
                    time.sleep(random.randint(1, 2))
                    print("你死了…………游戏结束")
                    time.sleep(random.randint(1, 2))
                    print("欢迎再度游玩！")

```
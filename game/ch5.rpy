## 解谜 = 把命题做成玩法：口红架「深红→浅粉」排序；编号随机贴、颜色不骗人。

default persistent.ch5_unlocked = False
default persistent.ch5_seen = False

## 解谜状态（无需存档，进程内）
default ch5_placed = []
default ch5_shown = []
default ch5_nums = {}
default ch5_attempts = 0

init python:

    def ch5_setup():
        ## 洗牌：展示序 + 编号映射（编号是烟雾弹，颜色才是真序）
        shown = [0, 1, 2, 3, 4, 5]
        renpy.random.shuffle(shown)
        nums = [1, 2, 3, 4, 5, 6]
        renpy.random.shuffle(nums)
        store.ch5_shown = shown
        store.ch5_nums = {idx: nums[k] for k, idx in enumerate(shown)}
        store.ch5_placed = []
        store.ch5_attempts = 0

    def ch5_place(idx):
        if idx not in store.ch5_placed and len(store.ch5_placed) < 6:
            store.ch5_placed = store.ch5_placed + [idx]
            renpy.restart_interaction()

    def ch5_unplace(slot):
        if 0 <= slot < len(store.ch5_placed):
            store.ch5_placed = store.ch5_placed[:slot] + store.ch5_placed[slot + 1:]
            renpy.restart_interaction()

    CH5_CORRECT = [0, 1, 2, 3, 4, 5]   ## 深红 → 浅粉


screen ch5_rack():
    modal True
    add Solid("#0B0F14")
    text "口红架 · 从深红到浅粉":
        xpos 80 ypos 36 size 34 color "#D8B4F0"
    text "编号漂移了。颜色不骗人。":
        xpos 80 ypos 88 size 20 color "#7E8898"
    if ch5_attempts > 0:
        text "第 [ch5_attempts] 次排列 · 色差仍偏着一度":
            xpos 80 ypos 120 size 20 color "#E8735A"

    ## 上排：6 个槽位
    for i in range(6):
        $ sx = 150 + i * 280
        if i < len(ch5_placed):
            $ idx = ch5_placed[i]
            imagebutton:
                idle "images/ch5/c%d.png" % idx
                action Function(ch5_unplace, i)
                xpos sx ypos 170
            $ numstr = "C-0%d" % ch5_nums[idx]
            text numstr:
                xpos sx ypos 494 size 22 color "#C9BFB0"
        else:
            add Solid("#1A2027"):
                xpos sx ypos 170
                xysize (240, 320)
            if i == len(ch5_placed):
                text "→":
                    xpos (sx + 96) ypos 300 size 48 color "#B48CD9"

    ## 下排：待排的口红（固定位，排走的置灰）
    for j, idx in enumerate(ch5_shown):
        $ bx = 150 + j * 280
        if idx in ch5_placed:
            add "images/ch5/c%d.png" % idx:
                xpos bx ypos 620
                alpha 0.22
        else:
            imagebutton:
                idle "images/ch5/c%d.png" % idx
                action Function(ch5_place, idx)
                xpos bx ypos 620

    ## 排满后出现「推入」
    if len(ch5_placed) == 6:
        textbutton "推 入":
            action Return("check")
            xpos 860 ypos 985 text_size 30
            background Solid("#1A2027") hover_background Solid("#2E3238")
            text_color "#D8B4F0" text_hover_color "#E8735A"

    ## 离开（进度不保留）
    textbutton "离开":
        action Return("quit")
        xpos 1720 ypos 40 text_size 22 text_color "#7E8898" text_hover_color "#E8735A"


label ch5_start:
    ## 主菜单 Start 进入；立绘关闭（本章只有 X 独白与 SYS）
    $ x_portrait_on = False
    $ z_portrait_on = False
    scene bg_z_night with fade
    play music "audio/indoor_bgm.mp3" fadein 2.0

    "再睁开眼，我在小屋里。"
    "信标的光不见了。茶还温着——不该温的。"
    "口红架摆在桌上。四十六支，从深红到浅粉。最右边，空着一格。"
    SYS "检测到片段记忆残留。可重演。"
    SYS "规则提示：架上自有其序——深红起，浅粉收。编号不可信，颜色不骗人。"
    "编号漂移。颜色不骗人。每一环偏一度——规则就是这样被毁掉的，也能这样被校回来。"

label ch5_puzzle:
    call screen ch5_rack
    if _return == "quit":
        stop music fadeout 2.0
        return
    if _return == "check":
        if ch5_placed == CH5_CORRECT:
            jump ch5_solved
        $ ch5_attempts += 1
        $ ch5_placed = []
        "颜色没有对齐。差的那一度，还悬在架子上。"
    jump ch5_puzzle

label ch5_solved:
    "口红架排齐了。色差一线，线是直的。"
    "最浅的粉，被推到最深的红旁边。它们一挨上，记忆闪了一下。"
    "——一支玫红的口红管，皮筋磨得发白。一扇门。一个没有回来的人。"
    "——四十六扇门。四十六个我。每一个人，都让色号偏了一点。"
    "投影亮起白色校准卡。"
    SYS "记忆记录：47 次。"
    SYS "四十六次送达。一次想起。"
    "桌上，她的小本子摊开着。纸页自己翻动。"
    show item_notebook:
        xalign 0.5 yalign 0.5 zoom 0.55 alpha 0.92
    "—— 第一页：今天，第十二个来了。他问我疼不疼。疼的，但习惯了。"
    "—— 第二页：我不是在记录你。我是在记录，每一个你。"
    "—— 第三页：要是有一天，有人不喝茶也记起来了，等待就可以结束了。"
    hide item_notebook
    "茶还温着。我把它端起来，喝了。"
    "味道不像抑制。像渡——把四十六份记忆，还给它们的主人。"
    "—— 有些人不是忘记了等待，而是终于想起，自己可以不再等待。 ——"
    SYS "等待协议：已终止。"
    "口红架最右的空格里，多了一支口红。颜色很新，像一次开始。"
    $ persistent.ch5_seen = True
    stop music fadeout 3.0
    "—— 尾声 · 第五章 · 不再等待 ——"
    return

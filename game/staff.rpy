## staff.rpy · 结尾演职员表（：慢慢结束、带室内音乐、留余韵）

transform staff_scroll:
    ypos 1080
    ## 速度与原 44s/-3600 基本一致，视觉节奏不变），pause 49s ⇒ 末尾约 39s 出屏、余量 10s。
    linear 48.0 ypos -4000

transform staff_bg(delay_s):
    alpha 0.0
    pause delay_s
    block:
        linear 2.0 alpha 0.30
        pause 4.0
        linear 2.0 alpha 0.0
        pause 8.0
    repeat

transform staff_bg_portrait(delay_s):
    alpha 0.0
    xalign 0.5 yalign 1.0 zoom 0.7
    pause delay_s
    block:
        linear 2.0 alpha 0.30
        pause 4.0
        linear 2.0 alpha 0.0
        pause 8.0
    repeat

screen staff_roll():
    add Solid("#05080D")
    add "images/bg_park.png" at staff_bg(0)
    add "images/bg_metro_night.png" at staff_bg(4)
    add "images/bg_store.png" at staff_bg(8)
    add "images/portrait_z_red.png" at staff_bg_portrait(12)
    vbox:
        at staff_scroll
        xalign 0.5
        spacing 34
        null height 40
        text "寻·环":
            size 88 color "#D8B4F0" xalign 0.5
        text "seek·loop":
            size 30 color "#C9BFB0" xalign 0.5 kerning 8
        null height 60
        text "STAFF":
            size 22 color "#6B7684" xalign 0.5
        null height 30

        text "原案 · 程序 / 叙事":
            size 22 color "#7E8898" xalign 0.5
        text "蒋平":
            size 38 color "#D8B4F0" xalign 0.5
        null height 26
        text "文案 · 流程脚本":
            size 22 color "#7E8898" xalign 0.5
        text "哈玉龙":
            size 38 color "#D8B4F0" xalign 0.5
        null height 26
        text "美术 · 意象与角色":
            size 22 color "#7E8898" xalign 0.5
        text "叶有泽":
            size 38 color "#D8B4F0" xalign 0.5
        null height 26
        text "场景美术":
            size 22 color "#7E8898" xalign 0.5
        text "袁佳佳":
            size 38 color "#D8B4F0" xalign 0.5
        null height 26
        text "空间体验 · 场景设计":
            size 22 color "#7E8898" xalign 0.5
        text "游佳":
            size 38 color "#D8B4F0" xalign 0.5
        null height 26
        text "音乐 · 音效":
            size 22 color "#7E8898" xalign 0.5
        text "蒋平":
            size 38 color "#D8B4F0" xalign 0.5
        null height 80
        text "PANDA JAM · 48H":
            size 24 color "#6B7684" xalign 0.5
        null height 40
        text "他们离开之后，地球已经独自生长了很久":
            size 24 color "#B48CD9" xalign 0.5

        ## 写错比不写更糟（展台播放）。姓名原样保留大小写与「·」。
        null height 70
        text "鸣谢":
            size 22 color "#6B7684" xalign 0.5
        null height 26
        text "PANDA JAM · 48H 科幻游戏创作团队赛":
            size 26 color "#B48CD9" xalign 0.5
        text "官方主题《环 Cycle》":
            size 22 color "#7E8898" xalign 0.5
        null height 22
        text "成都市科幻协会":
            size 24 color "#B48CD9" xalign 0.5
        text "游园试玩评审团":
            size 24 color "#B48CD9" xalign 0.5
        null height 16
        text "01 陈石 / 02 郭东升 / 03 刘星辰 / 04 大帅":
            size 20 color "#9A8FB0" xalign 0.5
        text "05 羽默空 / 06 老冷 / 07 安定 / 08 张月":
            size 20 color "#9A8FB0" xalign 0.5
        text "09 李颖 Evelyn / 10 peter / 11 Andi·老王":
            size 20 color "#9A8FB0" xalign 0.5
        text "12 江新烁 / 13 东云闲":
            size 20 color "#9A8FB0" xalign 0.5
        null height 22
        text "以及每一位停下来试玩、留下反馈的人":
            size 22 color "#7E8898" xalign 0.5
        null height 70


label staff_roll_scene:
    scene black with fade
    ## 室内音乐慢慢淡入，替换结局 A 的冰柜嗡鸣，留一点余韵
    play music "audio/indoor_bgm.mp3" fadeout 2.0 fadein 3.0
    show screen staff_roll
    pause 49.0          ## 与 staff_scroll 的 48.0s 配套（可点击跳过）
    hide screen staff_roll
    scene black with fade
    return

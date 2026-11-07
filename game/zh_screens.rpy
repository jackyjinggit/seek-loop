## zh_screens.rpy · 中文菜单覆盖层
## 同名 screen 后加载覆盖模板 screens.rpy 的英文版（s < z 加载序）
## 主菜单：封面（太空轨道环）+ 中文按钮 + 居中标题「寻·环」

screen main_menu():
    tag menu
    add "images/bg_cover_menu.png"   ## 封面＋顶部渐暗罩（保证三行标题可读）

    ## 标题（中上部）
    vbox:
        xalign 0.5 ypos 110
        spacing 12
        text "寻·环":
            size 100 color "#D8B4F0" xalign 0.5
        text "seek·loop":
            size 30 color "#C9BFB0" xalign 0.5 kerning 8
        text "他们离开之后，地球已经独自生长了很久":
            size 27 color "#B48CD9" xalign 0.5

    ## 中文菜单按钮（左侧竖排）
    vbox:
        xpos 120 yalign 0.62
        spacing 18
        textbutton "开始":
            action Start()
            text_size 38 text_color "#D8B4F0" text_hover_color "#E8735A"
        textbutton "读档":
            action ShowMenu("load")
            text_size 32 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "记忆残留":
            action Show("gallery")
            text_size 32 text_color "#B48CD9" text_hover_color "#E8735A"
        if persistent.ch5_unlocked:
            textbutton "尾声":
                action Start("ch5_start")   ## 第五章：真结局解锁（Start 从主菜单进游戏上下文，安全）
                text_size 32 text_color "#E8A0B4" text_hover_color "#E8735A"
        textbutton "设置":
            action ShowMenu("preferences")
            text_size 32 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "退出":
            action Quit(confirm=False)
            text_size 32 text_color "#B48CD9" text_hover_color "#E8735A"

    ## 底部小字
    text "PANDA JAM · 48H":
        size 20 color "#4A5560" xalign 0.5 yalign 0.96


## 游戏内导航菜单中文化（覆盖模板 navigation）
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 60 yalign 0.5
        spacing 12
        textbutton "返回" action Return()
        textbutton "历史" action ShowMenu("history")
        textbutton "保存" action ShowMenu("save")
        textbutton "读档" action ShowMenu("load")
        textbutton "设置" action ShowMenu("preferences")
        textbutton "主菜单" action MainMenu()
        textbutton "退出" action Quit(confirm=False)


## 设置界面中文覆盖（同名覆盖模板 preferences）
screen preferences():
    tag menu
    add "images/bg_street_dim.png"

    text "设置":
        size 48 color "#D8B4F0" xpos 120 ypos 60

    vbox:
        xpos 160 ypos 200
        spacing 30

        ## 显示
        hbox:
            spacing 30
            text "显示" size 28 color "#B48CD9"
            textbutton "窗口" action Preference("display", "window") text_size 26
            textbutton "全屏" action Preference("display", "fullscreen") text_size 26

        ## 文字速度
        hbox:
            spacing 30
            text "文字速度" size 28 color "#B48CD9"
            bar value Preference("text speed") xsize 500 yalign 0.5

        ## 自动前进
        hbox:
            spacing 30
            text "自动前进" size 28 color "#B48CD9"
            bar value Preference("auto-forward time") xsize 500 yalign 0.5

        ## 音乐音量
        hbox:
            spacing 30
            text "音乐音量" size 28 color "#B48CD9"
            bar value Preference("music volume") xsize 500 yalign 0.5

        ## 音效音量
        hbox:
            spacing 30
            text "音效音量" size 28 color "#B48CD9"
            bar value Preference("sound volume") xsize 500 yalign 0.5

        ## 跳过
        hbox:
            spacing 30
            text "跳过" size 28 color "#B48CD9"
            textbutton "全部跳过" action Preference("skip", "all") text_size 24
            textbutton "选择后跳过" action Preference("after choices", "skip") text_size 24

    hbox:
        xpos 120 ypos 950 spacing 50
        textbutton "返回" action Return() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "主菜单" action MainMenu() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "退出" action Quit(confirm=False) text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"


## 读档/存档界面中文自写版（同名覆盖模板；槽位空显示中文「空槽位」）
screen load():
    tag menu
    add "images/bg_street_dim.png"
    text "读档":
        size 48 color "#D8B4F0" xpos 120 ypos 60
    grid 3 2:
        xpos 300 ypos 200
        spacing 40
        for i in range(1, 7):
            button:
                xsize 440 ysize 250
                background Solid("#1A2027")
                hover_background Solid("#2E3238")
                action FileLoad(i)
                vbox:
                    xalign 0.5 yalign 0.5 spacing 8
                    $ shot = FileScreenshot(i)
                    if shot:
                        add Transform(shot, zoom=0.5) xalign 0.5
                    else:
                        text "（空）" size 40 color "#4A5560" xalign 0.5
                    text FileTime(i, format="%m-%d %H:%M", empty="空槽位"):
                        size 24 color "#B48CD9" xalign 0.5
    hbox:
        xpos 120 ypos 950 spacing 50
        textbutton "返回" action Return() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "主菜单" action MainMenu() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "退出" action Quit(confirm=False) text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"

screen save():
    tag menu
    add "images/bg_street_dim.png"
    text "存档":
        size 48 color "#D8B4F0" xpos 120 ypos 60
    grid 3 2:
        xpos 300 ypos 200
        spacing 40
        for i in range(1, 7):
            button:
                xsize 440 ysize 250
                background Solid("#1A2027")
                hover_background Solid("#2E3238")
                action FileSave(i)
                vbox:
                    xalign 0.5 yalign 0.5 spacing 8
                    $ shot = FileScreenshot(i)
                    if shot:
                        add Transform(shot, zoom=0.5) xalign 0.5
                    else:
                        text "（空）" size 40 color "#4A5560" xalign 0.5
                    text FileTime(i, format="%m-%d %H:%M", empty="空槽位"):
                        size 24 color "#B48CD9" xalign 0.5
    hbox:
        xpos 120 ypos 950 spacing 50
        textbutton "返回" action Return() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "主菜单" action MainMenu() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "退出" action Quit(confirm=False) text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"


## 历史界面中文自写覆盖（模板英文+缩放不合）
screen history():
    tag menu
    add "images/bg_street_dim.png"
    text "历史":
        size 48 color "#D8B4F0" xpos 120 ypos 60
    viewport:
        xpos 200 ypos 180
        xsize 1520 ysize 700
        yinitial 1.0          ## 🔴 打开即定位到最新对话（默认从第一条看起）
        scrollbars "vertical"
        mousewheel True
        vbox:
            spacing 16
            for h in _history_list:
                if h.who:
                    text h.who:
                        size 26 color "#D9A441"
                text h.what:
                    size 26 color "#D8B4F0"
    hbox:
        xpos 120 ypos 950 spacing 50
        textbutton "返回" action Return() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "主菜单" action MainMenu() text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "退出" action Quit(confirm=False) text_size 30 text_color "#B48CD9" text_hover_color "#E8735A"


## 系统确认框中文覆盖（读档/退出/回主菜单的确认；引擎英文消息做映射）
screen confirm(message, yes_action, no_action):
    modal True
    $ msg = message
    if "Loading will lose" in message:
        $ msg = "读档将丢失未保存的进度。确定要读档吗？"
    elif "quit" in message.lower():
        $ msg = "确定要退出吗？"
    elif "main menu" in message.lower():
        $ msg = "确定要回到主菜单吗？当前进度请记得保存。"
    frame:
        xalign 0.5 yalign 0.5
        xsize 760 ysize 300
        background Solid("#1A2027")
        vbox:
            xalign 0.5 yalign 0.5 spacing 40
            text msg:
                size 28 color "#D8B4F0" xalign 0.5
            hbox:
                xalign 0.5 spacing 80
                textbutton "是":
                    action yes_action text_size 32 text_color "#D8B4F0" text_hover_color "#E8735A"
                textbutton "否":
                    action no_action text_size 32 text_color "#B48CD9" text_hover_color "#E8735A"


## 底部快捷栏中文覆盖（Back/History/Auto/Save/Load/Prefs → 中文）
screen quick_menu():
    zorder 100
    hbox:
        xalign 0.5 yalign 0.98
        spacing 24
        textbutton "返回" action Rollback() text_size 22 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "历史" action ShowMenu("history") text_size 22 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "自动" action Preference("auto-forward", "toggle") text_size 22 text_color ("#E8735A" if preferences.afm_enable else "#B48CD9") text_hover_color "#E8735A"
        textbutton "快进" action Skip() alternate Skip(fast=True, confirm=True) text_size 22 text_color ("#E8735A" if config.skipping else "#B48CD9") text_hover_color "#E8735A"
        textbutton "存档" action ShowMenu("save") text_size 22 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "读档" action ShowMenu("load") text_size 22 text_color "#B48CD9" text_hover_color "#E8735A"
        textbutton "设置" action ShowMenu("preferences") text_size 22 text_color "#B48CD9" text_hover_color "#E8735A"

## panorama.rpy · 环视模块 v3（）
##   - 不做左右移动的长图了 → 去掉 360 环视与左右转按钮，用当前场景静态图
##   - 点「环视」→ 浮现一个道具按钮 → 按了才拿到
##   - 没注意就点「离开」= 没拿到，错过不补（不重刷、不保底）
##   - 集齐 4 个道具 → story.rpy 的 ending_secret 隐藏结局「门外」

default items_found = []      ## 四道具 id 集

transform item_reveal:
    alpha 0.0
    linear 0.45 alpha 1.0

screen item_popup(pic, ttl):
    ## modal：弹卡期间屏蔽 quick_menu 等下层 screen 的点击穿透
    modal True
    add pic
    text ttl:
        xalign 0.5 ypos 24 size 42 color "#D8B4F0"
    textbutton "收好":
        action Return()
        ## 桌面 textbox_height=185 / yalign=1.0 ⇒ 上沿 y=1080-185=895；
        ## yanchor 1.0 = 按钮底边贴住该线（small 变体下为 240 ⇒ 840，属手机档不在此列）。
        xalign 0.5 ypos 895 yanchor 1.0 text_size 30
        background Solid("#1A2027") hover_background Solid("#2E3238")
        text_color "#B48CD9" text_hover_color "#E8735A"

screen panorama_screen(scene_img, item_label, revealed):
    if scene_img:
        add scene_img

    if not revealed:
        textbutton "环视":
            action Return("reveal")
            xpos 880 ypos 500 text_size 34
            background Solid("#1A2027") hover_background Solid("#2E3238")
            text_color "#D8B4F0" text_hover_color "#E8735A"
    else:
        textbutton item_label:
            action Return("take")
            xpos 820 ypos 500 text_size 30
            background Solid("#1A2027") hover_background Solid("#2E3238")
            text_color "#D8B4F0" text_hover_color "#E8735A"
            at item_reveal

    textbutton "离开":
        action Return("leave")
        xpos 880 ypos 880 text_size 26 text_color "#B48CD9" text_hover_color "#E8735A"


## 参数：call panorama_scene(场景图路径, 道具id, 道具显示名, 特写卡图路径)
label panorama_scene(scene_img, item_id, item_label, item_pic):
    $ pano_img = scene_img
    $ pano_id = item_id
    $ pano_label = item_label
    $ pano_pic = item_pic
    $ revealed = False
    "（可以环视一下，也可以直接走。）"

label panorama_loop:
    call screen panorama_screen(pano_img, pano_label, revealed)
    if _return == "reveal":
        $ revealed = True
        "（有什么东西，刚刚露了出来。）"
        jump panorama_loop
    elif _return == "take":
        $ items_found = items_found + [pano_id]
        $ unlock_for_item(pano_id)   ## 记忆残留：按道具解锁立绘
        call screen item_popup(pano_pic, pano_label)
        "（已收集：[len(items_found)] / 4）"
        return
    else:
        "（你没注意到什么，就走开了。）"
        return

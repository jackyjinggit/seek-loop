## gallery.rpy · 记忆残留（立绘 + 设定集收集 / 延长游玩 / 第五章入口）
## 立绘 8 张 + 设定集 13 张（角色三视图 / 道具 v1 设计稿 / 场景概念稿），
## 每张挂一段记忆碎片（叙事补完，非纯看图），与续写稿二周目「记忆残留」探索衔接。

default persistent.unlocked_skins = ["x_glance"]        ## 立绘：初始记忆
default persistent.unlocked_concepts = ["concept_helipad"]   ## 设定集：初始记忆（停机坪）
default gallery_tab = "skin"                            ## 页签：立绘 / 设定集

init python:
    GALLERY_ITEMS = [
        {"id": "x_glance", "img": "images/portrait_x_glance.png", "name": "X · 斜视",
         "mem": "车窗倒影里，他的轮廓被阳光冲淡。", "cond": "初始记忆"},
        {"id": "x_lipstick", "img": "images/portrait_x_lipstick.png", "name": "X · 托口红直视",
         "mem": "他把皮筋缠回去。冰柜嗡鸣逐渐变远。", "cond": "环视拿到「口红」"},
        {"id": "x_up", "img": "images/portrait_x_up.png", "name": "X · 仰望",
         "mem": "现在倒要去最远的地方。", "cond": "环视拿到「书」"},
        {"id": "z_neutral", "img": "images/portrait_z_neutral.png", "name": "Z · 无表情",
         "mem": "你是第一个没喝茶的。", "cond": "环视拿到「茶包」"},
        {"id": "z_smile", "img": "images/portrait_z_smile.png", "name": "Z · 微笑",
         "mem": "谢谢。请问，你是——", "cond": "通关结局 A「送达」"},
        {"id": "z_side", "img": "images/portrait_z_side.png", "name": "Z · 左瞟",
         "mem": "门一响，就像他还在路上。", "cond": "隐藏结局「门外」"},
        {"id": "z_red", "img": "images/portrait_z_red.png", "name": "Z · 红",
         "mem": "她用口红，很轻地写下一个字：X。", "cond": "隐藏结局「门外」"},
        {"id": "z_redpocket", "img": "images/portrait_z_redpocket.png", "name": "Z · 揣手",
         "mem": "终于想起，自己可以不再等待。", "cond": "真结局「不再等待」"},
    ]

    ## 设定集：角色三视图 / 道具 v1 设计稿 / 场景概念稿（全部来自 assets 设定原图，
    CONCEPT_ITEMS = [
        {"id": "concept_helipad", "img": "images/gallery/concept_helipad.png", "name": "场景 · 停机坪",
         "mem": "雾压得很低。C-47 停在坪上，像在等一个不会来的人。", "cond": "初始记忆"},
        {"id": "concept_lipstick", "img": "images/gallery/concept_lipstick.png", "name": "道具 · 口红 v1",
         "mem": "他把它递过来，皮筋还缠在磨白的外壳上。", "cond": "环视拿到「口红」"},
        {"id": "concept_tea", "img": "images/gallery/concept_tea.png", "name": "道具 · 茶 v1",
         "mem": "杯底那角标签。后来才读懂，那不是抑制，是渡。", "cond": "环视拿到「茶包」"},
        {"id": "concept_park", "img": "images/gallery/concept_park.png", "name": "场景 · 街心公园",
         "mem": "空秋千慢慢晃。墙上两道身高线，一高一矮。", "cond": "环视拿到「茶包」"},
        {"id": "concept_notebook", "img": "images/gallery/concept_notebook.png", "name": "道具 · 小本子 v1",
         "mem": "她记得每一个人，除了那个没喝茶的。", "cond": "环视拿到「书」"},
        {"id": "concept_zroom", "img": "images/gallery/concept_zroom.png", "name": "场景 · 她的小屋",
         "mem": "46 支口红从深红到浅粉。最右空着。", "cond": "环视拿到「书」"},
        {"id": "concept_beacon", "img": "images/gallery/concept_beacon.png", "name": "道具 · 信标 v1",
         "mem": "确认送达，将清除全部相关记忆。", "cond": "环视拿到「信标」"},
        {"id": "concept_store", "img": "images/gallery/concept_store.png", "name": "场景 · 小卖铺",
         "mem": "列车驶过。小卖铺冰柜仍在嗡鸣。", "cond": "通关结局 A「送达」"},
        {"id": "concept_duoji", "img": "images/gallery/concept_duoji.png", "name": "设定 · 多吉三视图",
         "mem": "屋檐下，多吉正慢慢把头缩进壳里躲雨。", "cond": "隐藏结局「门外」"},
        {"id": "concept_xiaomi", "img": "images/gallery/concept_xiaomi.png", "name": "设定 · 小咪三视图",
         "mem": "紫斗篷被风吹得鼓起来。它抬头看了一眼镜头。", "cond": "隐藏结局「门外」"},
        {"id": "concept_pading", "img": "images/gallery/concept_pading.png", "name": "设定 · 帕丁三视图",
         "mem": "它每天都走这条路——风雨无阻。", "cond": "隐藏结局「门外」"},
        {"id": "concept_trio", "img": "images/gallery/concept_trio.png", "name": "设定 · 三小只同框",
         "mem": "这座城市的小生命，也在等谁回来。", "cond": "隐藏结局「门外」"},
        {"id": "concept_cover", "img": "images/gallery/concept_cover.png", "name": "场景 · 主视觉",
         "mem": "他们离开之后，地球已经独自生长了很久。", "cond": "真结局「不再等待」"},
    ]

    ITEM_TO_SKIN = {
        "item_lipstick": "x_lipstick",
        "item_teabag": "z_neutral",
        "item_notebook": "x_up",
    }
    ITEM_TO_CONCEPTS = {
        "item_lipstick": ["concept_lipstick"],
        "item_teabag": ["concept_tea", "concept_park"],   ## 环视 2 在公园里层 → 同步解锁公园概念稿
        "item_notebook": ["concept_notebook", "concept_zroom"],  ## 环视 3 面对 Z → 同步解锁小屋概念稿
        "item_beacon": ["concept_beacon"],
    }

    def unlock_skin(sid):
        ## 重新赋值而非原地 append，避免 persistent 可变对象跨档共享
        if sid not in persistent.unlocked_skins:
            persistent.unlocked_skins = persistent.unlocked_skins + [sid]

    def unlock_concept(cid):
        if cid not in persistent.unlocked_concepts:
            persistent.unlocked_concepts = persistent.unlocked_concepts + [cid]

    def unlock_for_item(item_id):
        sid = ITEM_TO_SKIN.get(item_id)
        if sid:
            unlock_skin(sid)
        for cid in ITEM_TO_CONCEPTS.get(item_id, []):
            unlock_concept(cid)

transform gallery_thumb:
    zoom 0.20          ## 等比缩放，立绘不变形（1024x1536 → 205x307）

screen gallery():
    modal True
    add Solid("#0B0F14")
    text "记忆残留" xpos 80 ypos 40 size 44 color "#D8B4F0"
    text "立绘 [len(persistent.unlocked_skins)]/8 · 设定集 [len(persistent.unlocked_concepts)]/13 · 每一张，都是某一次你来过":
        xpos 80 ypos 100 size 20 color "#7E8898"

    hbox:
        xpos 80 ypos 134 spacing 26
        textbutton "立绘":
            action SetVariable("gallery_tab", "skin")
            text_size 24 text_color ("#E8735A" if gallery_tab == "skin" else "#7E8898") text_hover_color "#E8735A"
        textbutton "设定集":
            action SetVariable("gallery_tab", "concept")
            text_size 24 text_color ("#E8735A" if gallery_tab == "concept" else "#7E8898") text_hover_color "#E8735A"

    if gallery_tab == "skin":
        for i, item in enumerate(GALLERY_ITEMS):
            $ cx = 80 + (i % 4) * 300
            $ cy = 190 + (i // 4) * 400
            if item["id"] in persistent.unlocked_skins:
                add item["img"]:
                    xpos cx ypos cy
                    at gallery_thumb
                text item["name"]:
                    xpos cx ypos (cy + 315) size 22 color "#C9BFB0"
                text item["mem"]:
                    xpos cx ypos (cy + 347) size 16 color "#7E8898" xmaximum 280
            else:
                text "？":
                    xpos cx ypos (cy + 40) size 90 color "#3A2F4A"
                text "未解锁":
                    xpos cx ypos (cy + 200) size 20 color "#7E8898"
                text item["cond"]:
                    xpos cx ypos (cy + 315) size 17 color "#7E8898" xmaximum 280
    else:
        for i, item in enumerate(CONCEPT_ITEMS):
            $ cx = 80 + (i % 4) * 300
            $ cy = 200 + (i // 4) * 200
            if item["id"] in persistent.unlocked_concepts:
                add item["img"]:
                    xpos cx ypos cy
                text item["name"]:
                    xpos cx ypos (cy + 164) size 18 color "#C9BFB0"
                text item["mem"]:
                    xpos cx ypos (cy + 188) size 13 color "#7E8898" xmaximum 280
            else:
                text "？":
                    xpos cx ypos (cy + 20) size 60 color "#3A2F4A"
                text item["cond"]:
                    xpos cx ypos (cy + 164) size 14 color "#7E8898" xmaximum 280

    textbutton "返回":
        action Hide("gallery")   ## 主菜单 Show 进入 → Hide 返回；Return() 仅在 call screen 下有效
        xpos 80 ypos 1040 text_size 26 text_color "#B48CD9" text_hover_color "#E8735A"


label gallery_open:
    ## 旧入口保留兼容（当前无调用方）：call screen 场景下 Return() 才生效
    call screen gallery
    return

## script.rpy · 寻·环 seek·loop
## 工程骨架 v0.1 · 四幕 + 两结局 + 「喝茶」玩家选择
##
##   - 工程结构 = 本骨架（四幕/分支/结局可玩）
##   - 策划反馈已采纳：①喝茶=玩家选择（喝了=亲手制造一环）③信标清除逻辑有一句协议解释
##
##   ① 主场景改为「航天港停机坪」；T3 中转站（有地铁）保留下来，作为停机坪之后的换乘点
##      → 交通动线：飞机 → 地铁 → 街区便利店，只切换一次交通工具
##      夜晚室内面对Z / 停机坪 / 夜晚街头（自带「多吉便利」招牌）
##   ③ 旧 bg_* 定义留在下方但剧本不再引用；四张环视全景已用新素材重拼

define X = Character("我", color="#D8B4F0")
define Y = Character("Y", color="#B48CD9")
define Z = Character("Z", color="#D9A441")   ## 暖金——全作唯一的人味色

image warm_glow = "images/warm_glow.png"

transform caption_in(d):
    alpha 0.0
    pause d
    linear 0.9 alpha 1.0

screen intro_captions():
    ## 左上角：时空锚定
    text "时间：未来地球资源枯竭后；Y出发远航前委托，X抵达地球时已过去多年。":
        xpos 90 ypos 80 size 22 color "#C9BFB0" xmaximum 900
        at caption_in(0.4)
    ## 环境背景 · 逐句浮现（黑屏上居中偏下）
    text "从小的朋友，一个喜欢航天，成为了远航者；":
        xalign 0.5 ypos 640 size 30 color "#F2EAF8"
        at caption_in(2.0)
    text "一个喜欢编程，留在了近地智慧站，成为了运维人员；":
        xalign 0.5 ypos 706 size 30 color "#F2EAF8"
        at caption_in(4.0)
    text "一个喜欢写诗，成为了驻留者":
        xalign 0.5 ypos 772 size 30 color "#F2EAF8"
        at caption_in(6.0)
## ── 新素材包（主场景只用这三张 + 两张调色派生）──
image bg_z_night = "images/bg_z_night.png"               ## 夜晚室内·面对 Z
image bg_helipad = "images/bg_helipad.png"               ## 航天港停机坪（飞机）
image bg_transfer = "images/bg_transfer.png"             ## T3 中转站·地铁（停机坪后的换乘站）
image bg_street_duoji = "images/bg_street_duoji.png"     ## 夜晚街头·多吉便利
image bg_street_dim = "images/bg_street_dim.png"         ## 街头压暗冷调（小区外景／菜单）
image bg_helipad_cold = "images/bg_helipad_cold.png"     ## 停机坪冷调（里世界）
image bg_room = "images/bg_room.png"
image bg_inner = "images/bg_inner.png"
image bg_z_room = "images/bg_z_room.png"
image bg_city_day = "images/bg_city_day.png"
image bg_street_night = "images/bg_street_night.png"
image bg_city_arrive = "images/bg_city_arrive.png"
image bg_city_hub = "images/bg_city_hub.png"
image bg_city_community = "images/bg_city_community.png"
image bg_z_courtyard = "images/bg_z_courtyard.png"
image bg_z_private = "images/bg_z_private.png"
image bg_city_tower = "images/bg_city_tower.png"
image bg_night_old = "images/bg_night_old.png"
image bg_night_street = "images/bg_night_street.png"
image duoji = "images/duoji_scene.png"       ## 龟 · 地板场景（11-07 新图）
image xiaomi = "images/xiaomi_scene.png"     ## 紫斗篷猫 · 地板场景
image pading = "images/pading_scene.png"     ## 渔夫帽企鹅 · 地板场景 v4

## 面对 Z 场景 · 兴趣点（旧 v1，保留给策划对照热点设计稿；A 阶段实际用 v2）
screen z_room_hotspots():
    textbutton "与 Z 对话":
        action Return("talk") xpos 880 ypos 560
        text_size 28 text_color "#C9BFB0" text_hover_color "#E8735A"
    textbutton "调整口红陈列":
        action Return("lipsticks") xpos 1560 ypos 440
        text_size 24 text_color "#9FB3C8" text_hover_color "#E8735A"
    textbutton "调查茶杯":
        action Return("tea") xpos 800 ypos 920
        text_size 24 text_color "#9FB3C8" text_hover_color "#E8735A"
    textbutton "阅读笔记":
        action Return("notebook") xpos 1380 ypos 920
        text_size 24 text_color "#9FB3C8" text_hover_color "#E8735A"
    textbutton "返回门口":
        action Return("leave") xpos 100 ypos 920
        text_size 24 text_color "#9FB3C8" text_hover_color "#E8735A"

## 温暖扩散动效（喝茶时）：暖光从中心扩散 + 渐显再淡去
transform warm_spread:
    xalign 0.5 yalign 0.5
    alpha 0.0 zoom 0.1
    linear 2.5 alpha 0.85 zoom 1.8
    linear 2.0 alpha 0.0

default drank_tea = False      ## 玩家是否喝了茶（环的开关）
default tea_loops = 0          ## 喝茶循环计数（3/5 次给提示）
default truth_book = False     ## 可挖真相：小本子
default truth_beacon = False   ## 可挖真相：信标协议日志
default truth_colors = False   ## 可挖真相：色号偏色

## ─────────────────────────────────────────────
default persistent.afm_speed_set = False   ## 自动前进速度是否已设过中值（持久化标记）
default persistent.afm_mid_set = False     ## 旧档兼容：确保默认值写入过一次

label start:

    ## 🔺 自动前进速度设中值一次（🔴 v54 修真 bug：引擎字段是 afm_time（量程 0-30，0=永不推进），
    "她忘了我。忘了每一个来过的人。只留下释然，和那个空出的珊瑚红位置。"
    "信标升空了。"
    scene bg_helipad with fade   ## 停机坪·信标升空
    play music "audio/freezer_hum.ogg" fadein 1.0   ## 结局 A 关键音：冰柜嗡嗡
    "雾散了一瞬，又合上。街那头，便利店冰柜嗡嗡响。"
    "第 48 支口红，没有出现。"
    "—— 结局 A · 送达 ——"
    return


label ending_b:
    "我收回了手。把口红，带了回来。"
    "循环断了。她的记忆开始崩解——但她第一次，想起了「等待」之外的人。"
    "我走出小屋。灰调的世界里，我低头看了一眼手里的珊瑚红。"
    "然后，天边出现了第二种颜色。"
    "—— 结局 B · 觉醒 ——"
    return

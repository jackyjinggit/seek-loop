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
    ## 旧代码写 auto_forward_time 是无效属性静默不生效 → 用新标记再兜一次旧档，之后玩家自调不覆盖）
    if not persistent.afm_speed_set:
        $ preferences.afm_time = 15.0
        $ persistent.afm_speed_set = True
    if not persistent.afm_mid_set:
        $ preferences.afm_time = 15.0
        $ persistent.afm_mid_set = True

    scene bg_cover with fade
    "……"
    scene black with fade

    jump story_start

    ## ── 幕一 · 任务委托（表世界 · 早）──
    ## 交通动线：航天港停机坪（飞机）→ T3 中转站（地铁）→ 街区便利店；中间只换一次交通工具
    scene bg_helipad with fade   ## 航天港停机坪
    play music "audio/city_ambient.ogg" fadein 2.0   ## 城市底噪
    "雾压得很低。C-47 停在坪上，舱门开着，像在等一个不会来的人。"
    "远处航天港的灯，一盏一盏亮起来。"

    scene bg_transfer with dissolve   ## T3 中转站 · 地铁（换乘点）

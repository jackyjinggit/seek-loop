## monitor.rpy · 路上监视点（多吉／小咪／帕丁 · 点开有加分）
##   巷口 → 小咪（紫斗篷猫）
##   屋檐 → 多吉（龟）  ← 屋檐就在「多吉便利」招牌边上，所以这个点换成多吉
##   街角 → 帕丁（渔夫帽企鹅）
## 新图 = *_scene.png（1920x1080，正方形原图等比缩入不裁头脚）；旧 duoji/xiaomi/pading.png 保留未删
default critter_found = 0   ## 彩蛋发现数

screen monitor_points():
    textbutton "监视点 · 巷口":
        action Return("xiaomi") xpos 300 ypos 500 text_color "#B48CD9" text_hover_color "#E8735A"
    textbutton "监视点 · 屋檐":
        action Return("duoji") xpos 1300 ypos 400 text_color "#B48CD9" text_hover_color "#E8735A"
    textbutton "监视点 · 街角":
        action Return("pading") xpos 900 ypos 700 text_color "#B48CD9" text_hover_color "#E8735A"
    textbutton "继续走":
        action Return("leave") xpos 880 ypos 880 text_color "#B48CD9" text_hover_color "#E8735A"

label monitor_loop:
    call screen monitor_points
    if _return == "xiaomi":
        show xiaomi with dissolve
        "（巷口摄像头：小咪蹲在台阶上，紫斗篷被风吹得鼓起来。它抬头看了一眼镜头——像是知道你在看。）"
        $ critter_found += 1
        hide xiaomi with dissolve
        jump monitor_loop
    elif _return == "duoji":
        show duoji with dissolve
        "（「多吉便利」招牌旁边的屋檐下，多吉正慢慢把头缩进壳里躲雨。它每天都在这儿。）"
        $ critter_found += 1
        hide duoji with dissolve
        jump monitor_loop
    elif _return == "pading":
        show pading with dissolve
        "（街角，帕丁戴着那顶旧渔夫帽慢悠悠地走过。它每天都走这条路——风雨无阻。）"
        $ critter_found += 1
        hide pading with dissolve
        jump monitor_loop
    else:
        return

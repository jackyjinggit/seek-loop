## story.rpy · 现行主流程【单线版】
## ：「不做选项还是单线推进」→ 去掉全部 menu／分支／隐藏条件／喝茶循环；
##   非互斥的观察三轮按叙事顺序串成连续所见所想，互斥动作只取唯一推进线（不喝茶 → 幕三；按下清除 → 结局 A）。
## 保留：开场视频、停机坪→T3 中转站过场、路上监视点、四次环视
##        （portraits.rpy 的 say callback），此处只放 x/z_portrait_on 在场开关。
##        「到此为止了吗？」继续=二周目／就这样=收束（契合循环）。
##        「没喝的茶」环视不切图保持面对 Z。
##        ③每个场景切换插入对应音效（helipad／metro／door／steps）。
## 结局 B 台词留档未接入；主线单线终点仍是结局 A。

define RAD = Character("广播", color="#9FB3C8")
define SYS = Character("系统", color="#9FB3C8")
define REC = Character("记录", color="#9FB3C8")
define SCR = Character("车厢显示屏", color="#9FB3C8")
define PAS = Character("路人", color="#9FB3C8")

image bg_metro = "images/bg_metro.png"
image bg_metro_sleep = "images/bg_metro_sleep.png"
image bg_metro_stand = "images/bg_metro_stand.png"
image bg_metro_night = "images/bg_metro_night.png"
image bg_metro_inside = "images/bg_metro_inside.png"
image bg_store_inside = "images/bg_store_inside.png"
image bg_park = "images/bg_park.png"
image bg_park_inside = "images/bg_park_inside.png"
image bg_z_inside = "images/bg_z_inside.png"
image y_screen = "images/y_sound_only.png"        ## Y 对话期间的投影屏（Y SOUND ONLY）

transform y_screen_float:
    xalign 0.32 yalign 0.5
    alpha 0.0
    linear 0.7 alpha 0.92


label story_start:

    ## ── 开场过场：停机坪（飞机）→ T3 中转站（地铁），定的动线 ──
    scene bg_helipad with fade
    play sound "audio/sfx_helipad.wav"
    play music "audio/outdoor_bgm.mp3" fadeout 2.0 fadein 3.0
    "雾压得很低。C-47 停在坪上，舱门开着，像在等一个不会来的人。"
    "远处航天港的灯，一盏一盏亮起来。"
    scene bg_transfer with dissolve
    play sound "audio/sfx_metro.wav"
    "从停机坪往城里走，中间要换一次车。"
    "T3 中转站。地铁进站，门开了一下，又合上。没有人下车。"
    "指示牌亮着：前往生活区 →。"

    ## ══ 幕一｜任务委托 ══
    scene bg_metro_sleep with fade
    play sound "audio/sfx_door.wav"
    "日光发灰。地铁穿过城市。X 靠着座椅睡着了。"
    "车厢轻轻晃着。这一觉很短，没有梦。"

    scene bg_metro_stand with dissolve
    play sound "audio/sfx_steps.wav"
    RAD "下一站，长乐路口。"
    "X 站起来，扶着窗框向外看。"
    "他说得很轻。像只是让我顺路带包烟。"
    X "城东，七号楼，四单元。"
    RAD "请保管好随身物品。"
    "X 摸了摸口袋里的船票存根。"
    "送到就回。今晚还有一段程序要改。"
    "发射场海报掠过。"
    X "他以前怕坐车。"
    "现在倒要去最远的地方。"
    "车窗倒影里，X 的轮廓被阳光冲淡。"
    X "连告别都要别人替。"
    "座椅背后的线路图泛黄。「街心公园」被划过一次。"
    X "这道印子，像他的指甲。"
    "站名旁有一个歪写的 Y。"
    "小时候，他总在等我时乱画。"
    "X 把线路图折角压平。"
    "一个废站名。也值得留到现在？"

    ## 🔺 环视 1／4 · 地铁 → 便利店（切换过程中）
    call panorama_scene("images/bg_metro_stand.png", "item_lipstick", "口红", "images/item_lipstick.png")

    ## 1-2 小卖铺·表层·日
    scene bg_store with dissolve
    $ x_portrait_on = False
    play sound "audio/sfx_door.wav"
    show y_screen at y_screen_float
    "Y 站在冰柜旁，把磨白的外壳擦了擦。"
    Y "这个，帮我带给她。"
    X "你自己送。"
    Y "不顺路。"
    X "去城东，能有多不顺？"
    "Y 把船票塞回口袋，露出的一角已经皱了。"
    Y "去找她。她叫Z。若她挽留，我就留下。"
    X "本人签收？"
    Y "嗯。别放门口。"
    X "只送东西，不替你说话。"
    Y "够了。"
    "他说得像句玩笑。可他没有笑。"
    "Y 转身，皮筋从口红上松下来。脚步声三短一长。"
    X "皮筋掉了。"
    Y "收着吧。别让它散。"
    hide y_screen with dissolve
    "X 把皮筋缠回去。冰柜嗡鸣逐渐变远。"
    "只是站久了。有点困。"

    "X 在小卖铺门边睡着。"
    $ x_portrait_on = True

    ## ══ 幕二｜时空意外 ══
    ## 2-1 地铁车厢·表层·夜
    scene bg_metro_night with fade
    play sound "audio/sfx_metro.wav"
    "X 在地铁车厢里惊醒。口红仍在手里。"
    "我什么时候上的车？"
    "窗外掠过公园站名。"
    "一闪而过的名字。好熟悉。"
    X "我睡了多久？"
    SCR "已过两站。"
    X "从哪儿上的车？"
    SCR "长乐路口。"
    "两站。窗外像过了很多年。"
    "小票地址仍在，打印日期模糊不清。"
    X "字没化。纸旧了。"
    X "七号楼，四单元。"
    "先找到人。别的事，找到再说。"
    X "街心公园。"
    "线路图上的 Y 与窗外站名重合。"
    "他等过我的地方。"
    X "下一站，我下车。"

    ## 2-2 街心公园·表层·日
    scene bg_park with fade
    play sound "audio/sfx_steps.wav"
    "空秋千慢慢晃。墙上两道身高线，一高一矮。"
    "高的那个原来是我。后来被他超了。"
    "Y 的记忆：再推高一点。"
    "少年 X：摔了别哭。"
    "Y 的记忆：摔了你就去叫她。"
    "那时候，他就总让我替他开口。"
    "较高一道旁写着 Y，日期被磨掉一半。"
    X "他什么时候长这么高的？"
    "风推动秋千，没人回答。"
    "我们后来见的次数，好像很少。"
    "X 叫出名字。秋千同时停住。"
    "Y 的记忆：要是我没回来——"
    X "别往下说。"
    "这句话，他以前也说过。"

    ## 2-3 街心公园·里层·日
    scene bg_park_inside with dissolve
    play sound "audio/sfx_steps.wav"
    "秋千仍在。站牌背面浮出抵达记录：X，多次；Y，零次。"
    X "他没来过？"
    REC "委托发起后，远航者离开本区。"
    REC "抵达四十六次。"
    X "我没有。"
    "每次记录都停在公园门口。"
    "每次都经过。每次都没停。"
    X "这次我停了。"
    REC "远航者已离场。"
    X "他真的走了。"
    "最后状态：委托未撤销。"
    "人走了，话还留着。"
    X "所以我才来。"
    "X 把口红握紧。"
    "先送到。等他回来，再问。"

    ## 🔺 环视 2／4 · 公园里层 → 步行街（切换过程中）
    call panorama_scene("images/bg_park_inside.png", "item_teabag", "茶包", "images/item_teabag.png")

    scene bg_street_duoji with fade
    play sound "audio/sfx_steps.wav"
    "步行街。小票写七号楼四单元，眼前是尽头亮灯的小屋。"
    "路过橱窗，珊瑚红口红的广告还贴着。"
    "街角「多吉便利」的招牌还亮着。"
    "（招牌底下的监控摄像头也亮着——可以看看这座城市的小生命。）"
    call monitor_loop
    X "地址改了？"
    X "七号楼怎么走？"
    PAS "这里没有七号楼。"
    X "那Z住哪儿？"
    PAS "最里面，有棵树的那栋。"
    "他没问Z是谁。"
    "X 沿围墙走一圈，没有单元号。"
    X "小票没写错。是这里变了。"
    PAS "找Z？她一般不出门。"
    "她不出门。他却非让我来。"
    "敲门两次。门内亮灯。"
    $ z_portrait_on = True
    Z "谁让你来的？"
    X "一个朋友。Y。"
    "Z先看见口红，再抬眼。"
    Z "你是第 47 个。"
    X "第 47 个什么？"
    Z "送它的人。"
    X "我只替一个人来。"
    Z "他们都是。"
    "她说「都」时，没有意外。"
    X "给你。"
    Z "先别递。"
    X "为什么？"
    Z "我还没准备好。"
    "她等了很久。真的到了，却不敢接。"
    "步行街的灯一盏盏灭，只剩小屋门口一盏。"

    ## 场景 5a｜小屋门口 ·「开着的窗」伏笔（故事外层，必播，不做选项）
    scene bg_z_night with fade
    play sound "audio/sfx_door.wav"
    play music "audio/indoor_bgm.mp3" fadeout 2.0 fadein 3.0
    "屋内没有风，窗帘却在动。靠里的窗户开着，窗台上没有灰。"
    X "窗户怎么开着？"
    Z "透透气吧。"
    "她走过去，把窗关上。动作很慢。"
    "她关的是窗。我却觉得屋里的声音少了一层。"

    ## 5b 茶桌（单线：不喝 → 保留连续记忆 → 幕三）
    "46 支口红从深红到浅粉。最右空着。Z倒了两杯茶，她那杯没动。"
    Z "喝吧。凉了。"
    X "你不喝？"
    Z "我晚上睡不着。"
    "杯底露出一角标签：抑制。"
    "茶叶不这样包装。"
    X "我不渴。"
    Z "你是第一个没喝茶的。"
    X "他们喝了，会怎样？"
    Z "会轻松一点。"
    X "那你呢？"
    Z "我不喝茶。"
    "X 看见茶桌下浮出里层冷光。"

    ## 🔺 环视 3／4 · 茶桌 → 幕三（切换过程中）
    call panorama_scene("", "item_notebook", "书", "images/item_notebook.png")

    ## 3-1 地铁车厢·里层·夜
    scene bg_metro_inside with fade
    $ z_portrait_on = False   ## 幕三里层 Z 不在场
    play sound "audio/sfx_steps.wav"
    play music "audio/beacon_drone.ogg" fadein 2.0
    "车厢不变。乘客消失。线路图变成执行表，047 正在闪烁。"
    SYS "本次抵达已确认。前次抵达四十六次。"
    X "我每次都坐这辆车？"
    SYS "起点相同。终点相同。"
    X "执行人也相同？"
    SYS "来源相同。个体不同。"
    "不是我回来了。是下一个我又来了。"
    X "046 是谁？"
    SYS "上一信使。"
    X "他去哪儿了？"
    SYS "记忆已抑制。任务已重跑。"
    "失败没有清零。只是人忘了。"

    ## 3-2 小卖铺·里层·日
    scene bg_store_inside with dissolve
    play sound "audio/sfx_steps.wav"
    "货架仍在。冰柜门变成日志窗。Y 的委托语句重复排列。"
    "Y 的记录：去找她。她叫Z。若她挽留，我就留下。"
    X "一遍都没改过。"
    "皮筋断口与外壳修补次数逐次增加。"
    X "不是同一支新的。"
    SYS "每次偏差已保留。"
    "环不是重复。每一次，都偏一点。"
    SYS "协议创建者，初代 X。"
    X "我写的？"
    SYS "是。任务未送达，执行重跑。"
    "是我写的程序，不肯承认失败。"
    X "Y 后来撤销过吗？"
    SYS "否。"
    X "他知道会重跑？"
    SYS "无相关记录。"
    "他只留下心愿。后果是我加的。"

    ## 🔺 环视 4／4 · 小卖铺里层 → 公园里层（切换过程中）
    call panorama_scene("images/bg_store_inside.png", "item_beacon", "信标", "images/item_beacon.png")

    ## 3-3 街心公园·里层·夜
    scene bg_park_inside with dissolve
    play sound "audio/sfx_steps.wav"
    "身高线变成意识来源刻度。秋千下出现初代 X 的封存记录。"
    X "我的童年，也在这里？"
    SYS "来源记忆已复制。"
    SYS "记忆来源，初代 X。"
    X "那些不是假的。"
    SYS "记录真实。归属复制。"
    "我记得秋千。他也记得。我们算谁活过？"
    "四十六个光点都绕过公园。"
    X "没人停过。"
    SYS "任务未要求停留。"
    "我们都在送东西。没人问过自己想留下什么。"

    ## 3-4 Z的小屋·里层·日
    scene bg_z_inside with dissolve
    play sound "audio/sfx_steps.wav"
    $ z_portrait_on = True
    "小屋结构不变。维护记录与小本子同时展开。"
    Z "你都看到了。"
    X "还差你这部分。"
    "第 47 页写着「没喝茶那个」。"
    X "为什么不写X？"
    Z "怕写了，你就真的来过。"
    X "你记得所有人？"
    Z "每一个。"
    "原来不被记下，也可能是一种舍不得。"
    SYS "回传前须清除驻留者对全部信使的记忆。"
    X "包括我？"
    SYS "是。"
    Z "这是结束的条件。"
    "送她一份心意。要拿四十七个人来换。"
    Z "门一响，就像他还在路上。"
    X "所以你没停。"
    Z "我想结束。也想记得。"

    ## ══ 幕四｜结局选择（单线：按下清除 → 结局 A）══
    ## 4-1 Z的小屋·表层·夜｜涂口红
    scene bg_z_night with fade
    play sound "audio/sfx_steps.wav"
    "Z拧开口红，涂上珊瑚红。最右空位仍在。"
    Z "你确定？"
    X "你会忘了我。"
    Z "嗯。"
    X "你舍得？"
    Z "不舍得。"
    "她把手从信标旁收回来。"
    Z "这次，你选。"

    ## 4-2 Z的小屋·里层·夜｜最终确认
    scene bg_z_inside with dissolve
    play sound "audio/sfx_steps.wav"
    "小屋不变。小本子与信标浮在茶桌两侧。"
    SYS "确认送达，将清除全部相关记忆。"
    X "送达吧。"
    Z "好。"
    SYS "清除范围，全部信使。包含 047。"
    X "我知道。"
    "最后想起的，是她第一次叫我X。"

    ## 🔺 真结局分岔（续写稿《最后一章》：茶 = 把信使的记忆渡让给 Z）
    "她把手从信标旁收回来，转而推过来一杯茶。"
    Z "还有一条路。"
    Z "喝了它，你会忘了我。但我会记得你——比原来更完整。"
    X "为什么？"
    Z "茶从来不是让人忘记的东西。它把来的人的记忆，渡给我。"
    Z "四十六杯茶，四十六份记忆。我记得他们每一个人。"
    X "除了没喝茶的。"
    Z "是。只有你的，我还没收到。"
    "她把茶又推近了一点。"
    Z "这次，你可以自己决定。"
    menu:
        "喝下这杯茶":
            jump ending_true
        "按下清除":
            jump ending_deliver

label ending_deliver:
    ## 4-3A 结局 A｜小屋·表夜→小卖铺·表日
    "按钮落下。Z的目光慢慢变得礼貌。"
    Z "谢谢。请问，你是——"
    X "送东西的。"
    SYS "心意确认。回传完成。"
    "小本子最后一页褪色，「没喝茶那个」先消失。"
    scene bg_store with fade
    $ x_portrait_on = False
    $ z_portrait_on = False
    play sound "audio/sfx_door.wav"
    play music "audio/freezer_hum.ogg" fadein 1.0
    "列车驶过。小卖铺冰柜仍在嗡鸣。"
    "没有第 48 支口红了。"
    "—— 结局 A · 送达 ——"
    $ unlock_skin("z_smile")   ## 记忆残留：结局 A 解锁
    $ unlock_concept("concept_store")   ## 设定集：小卖铺概念稿（结局 A 最后一幕）

    ## 🔺 集齐 4 个道具 → 隐藏结局「门外」（单线条件触发，不是选项）
    if len(items_found) >= 4:
        jump ending_secret
    jump ending_credits


label ending_secret:
    scene bg_z_night with fade
    play sound "audio/sfx_steps.wav"
    "X 没有按清除，也没有带走口红。"
    X "我该走了。"
    Z "嗯。"
    "她替他开门。门外没有列车声。"
    X "你不问我是谁？"
    Z "你是 X。"
    "X 停了一下，没有回头。"
    X "对。"
    "X 走出门。门没有立刻关上。"
    scene bg_z_inside with dissolve
    play sound "audio/sfx_steps.wav"
    "室内。Z 独自站在桌边。"
    "她拿出小本子，翻到空白页。"
    "她旋开那支珊瑚红口红，没有涂在唇上。"
    "她用口红，很轻地写下一个字：X。"
    "停一下。她在 X 旁边补上一个小小的数字：47。"
    "她走到窗边，把窗子拉开。风吹起窗帘。"
    "她右手伸出去。放手。口红坠落。"
    "她没有往下看，转身。"
    "镜头切到窗外。一座口红山——深红、暗红、浅粉，有的完整，有的断裂。"
    "最顶端，那支珊瑚红慢慢滚下来。"
    "小本子摊开在桌上。风把纸页往前翻。"
    "前一页：X，46。再前一页：X，45。"
    "风继续翻。密密麻麻，全是 X。有的旁边写日期，有的什么都没有。"
    "Z 伸手，合上小本子。"
    "她拉开抽屉。里面是一摞同样磨旧的小本子。"
    "她把这一本放进去，推上抽屉。"
    scene black with fade
    $ x_portrait_on = False
    $ z_portrait_on = False
    "智能设备：未读讯息，已重新置顶。"
    "发件人：Y。内容：帮我交给Z。"
    "—— 隐藏结局 · 门外 ——"
    $ unlock_skin("z_side")
    $ unlock_skin("z_red")
    $ unlock_concept("concept_duoji")    ## 设定集：三小只三视图与同框（门外解锁）
    $ unlock_concept("concept_xiaomi")
    $ unlock_concept("concept_pading")
    $ unlock_concept("concept_trio")
    jump ending_credits

label ending_true:
    ## 真结局 · 不再等待（续写稿《最后一章》）
    ## 茶的机制统一为「把信使的记忆渡让给 Z」：X 遗忘、Z 更完整——
    ## 这同时解释了既有台词「她记得每一个人，除了那个没喝茶的」（没喝=没渡=没记下）。
    "茶很温。像很多人一起来过，又都留下了什么。"
    X "好像在哪里见过你。"
    Z "没关系。你给我的，比你想的多。"
    "X 慢慢放下茶杯。"
    "记忆里有什么东西松开了。不是消失，是抵达了另一个地方。"
    SYS "记忆同步完成。"
    SYS "传信任务完成。"
    "—— 第 47 次，已完成。47 / 47 ——"
    "记忆同步：完成。Z 的意识完整。X 的记忆：已交付。等待协议：已终止。"
    scene black with fade
    $ x_portrait_on = False
    $ z_portrait_on = False
    play music "audio/indoor_bgm.mp3" fadeout 2.0 fadein 3.0
    "有些人不是忘记了等待。"
    "而是终于想起，自己可以不再等待。"
    "—— 真结局 · 不再等待 ——"
    $ unlock_skin("z_redpocket")   ## 记忆残留：真结局解锁
    $ unlock_concept("concept_cover")   ## 设定集：主视觉概念稿（真结局解锁）
    $ persistent.ch5_unlocked = True   ## 真结局后解锁主菜单「尾声 · 第五章」
    jump ending_credits


label ending_credits:
    $ x_portrait_on = False
    $ z_portrait_on = False
    call staff_roll_scene
    "到此为止了吗？"
    menu:
        "继续":
            ## 二周目：清空四道具，从停机坪重新走一遍——契合「循环」
            $ items_found = []
            $ x_portrait_on = True
            $ z_portrait_on = False
            jump story_start
        "就这样":
            stop music fadeout 3.0
            scene black with fade
            return

## 立绘为 1024x1536 全身透明图裁到上半身（portrait_*.png），底部羽化，底缘由对话框遮住。

image x glance = "images/portrait_x_glance.png"
image x lipstick = "images/portrait_x_lipstick.png"
image x up = "images/portrait_x_up.png"
image z smile = "images/portrait_z_smile.png"
image z neutral = "images/portrait_z_neutral.png"
image z side = "images/portrait_z_side.png"
image z red = "images/portrait_z_red.png"
image z redpocket = "images/portrait_z_redpocket.png"

transform portrait_left:
    ## 贴左：小屋场景图中央本来就有 Z 的大半身，两侧留出中央
    xalign 0.16 yalign 1.0 zoom 0.62

transform portrait_right:
    xalign 0.84 yalign 1.0 zoom 0.62

default x_portrait_on = True     ## X 立绘是否在场
default z_portrait_on = False    ## Z 立绘是否在场（首次进小屋门口才开）

init python:
    _p_x_expr = ["x glance", "x lipstick", "x up"]
    _p_z_expr = ["z smile", "z neutral", "z side", "z red", "z redpocket"]
    _p_tick = 0

    def _portrait_rotate(who, *args, **kwargs):
        ## 🔺 引擎签名 = callback(who, *args, **kwargs)，返回 (args, kwargs)。每句 say（含旁白）都会进来。
        ## 旁白 / 其他角色 / 没说话时隐藏。序号每 3 句 +1 → 自动轮换。
        global _p_tick
        _p_tick += 1
        ix = (_p_tick // 3) % len(_p_x_expr)
        iz = (_p_tick // 3) % len(_p_z_expr)
        is_x = (who is renpy.store.X)   ## X 角色对象（显示名「我」）
        is_z = (who is renpy.store.Z)
        if renpy.store.x_portrait_on and is_x:
            renpy.show(_p_x_expr[ix], at_list=[portrait_left], tag="x")
        else:
            renpy.hide("x")
        if renpy.store.z_portrait_on and is_z:
            renpy.show(_p_z_expr[iz], at_list=[portrait_right], tag="z")
        else:
            renpy.hide("z")
        return args, kwargs

    config.say_arguments_callback = _portrait_rotate

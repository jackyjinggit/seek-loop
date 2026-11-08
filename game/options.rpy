## options.rpy · 寻·环 seek·loop
## Ren'Py 8.5 · 工程配置

define config.name = "seek_loop"
define config.window_title = "寻·环"
define config.version = "0.1"
define config.screen_width = 1920
define config.screen_height = 1080

## 灰调世界观基调：文字默认灰米，强调色只给珊瑚红（见 script）
define gui.text_color = "#C9BFB0"
define gui.interface_text_color = "#C9BFB0"
define gui.choice_button_text_idle_color = "#9FB3C8"
define gui.choice_button_text_hover_color = "#E8735A"  ## 珊瑚红——选择 hover 时才出现的鲜亮

## 选 outdoor_bgm：与 story_start 的 outdoor_bgm 同曲，点「开始」进入过场不跳曲；
## 回主菜单（结局「就这样」）时引擎会自动重新播放。
define config.main_menu_music = "audio/outdoor_bgm.mp3"

## 🔺 中文字体（得意黑 Smiley Sans · oooohmygosh 出品 · OFL 1.1 可嵌入；缺字显示□属正常，正文均为常用字）
define gui.text_font = "SmileySans-Oblique.ttf"
define gui.name_text_font = "SmileySans-Oblique.ttf"
define gui.interface_text_font = "SmileySans-Oblique.ttf"
define gui.button_text_font = "SmileySans-Oblique.ttf"
define gui.choice_button_text_font = "SmileySans-Oblique.ttf"
define gui.pref_button_text_font = "SmileySans-Oblique.ttf"

define config.quit_action = Quit(confirm=False)

define gui.show_name = True

## 默认全屏（；Esc 或偏好设置可切回窗口）
default preferences.fullscreen = True

## 自动前进速度默认中值（🔴 v54 修真 bug：引擎字段是 afm_time（量程 0-30，最左 0=永不推进），
## 旧写法 auto_forward_time 是无效属性静默不生效；15 = 滑条正中）
default preferences.afm_time = 15.0

## 未读文本可跳过（「Ctrl skip 没有」→ 引擎默认只跳已读，
default preferences.skip_unseen = True

## 存档缩略图生成尺寸调大（默认太小导致显示极小；新存档生效）
define config.thumbnail_width = 800
define config.thumbnail_height = 450

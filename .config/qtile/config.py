from libqtile import bar, layout, extension, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from settings.colors import colors, paleta_generada, widget_colors
from settings.keys import config_keys
import os

mod = "mod4"
terminal = "alacritty"

#Keys
keys = config_keys(mod, terminal, lazy)

#Groups

# __groups = {
#       1: Group(""),
#       2: Group(""),
#       3: Group("󰎙"),
#       4: Group(""),
#       5: Group(""),
#       6: Group("")
#   }

### Original ####

# __groups = {
#       1: Group(""),
#       2: Group(""),
#       3: Group("󰎙"),
#       4: Group(""),
#       5: Group(""),
#       6: Group("")
#   }

# groups = [__groups[i] for i in __groups]

# def get_index_from_group(name):
#     return [k for k, g in __groups.items() if g.name == name][0]

# for i in groups:
#     keys.extend(
#         [
#             Key(
#                 [mod],
#                 str(get_index_from_group(i.name)),
#                 lazy.group[i.name].toscreen()
#             ),
#             Key(
#                 [mod, "shift"],
#                 str(get_index_from_group(i.name)),
#                 lazy.window.togroup(i.name, switch_group=True)
#             ),
#         ]
#     )

#### END original ####


groups = [Group(i) for i in [
    "", "", "󰎙", "", "", ""
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


#Layouts
default_config_layout={
    'border_width': 1,
    'border_focus': '#09f',
    'margin': 0
}

layouts = [
    layout.MonadTall(
        border_width=1,
        border_focus="#09f",
        margin = 0,
        border_normal = "#222222",
        single_border_width = 0
    ),
    layout.Max(
        margin = 0,
    ),
    #layout.RatioTile(**default_config_layout),
    # layout.Matrix(
    #     columns=2,
    #     **default_config_layout
    # ),
    #layout.Bsp(**default_config_layout),
    #layout.Floating(margin=10, zindex=1),
    #layout.Columns(border_focus="#d75f5f", border_width=1, single_border_width = 0, margin = 10),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2, **default_config_layout),
    #layout.MonadWide(**default_config_layout),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#Widgets
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=1,
)
extension_defaults = widget_defaults.copy()

def rounded_right(fg=0, bg=None, foregroundColors=colors, backgroundColors=colors):
    return widget.TextBox(
        font="UbuntuMono Nerd Font Bold",
        foreground=foregroundColors[fg],
        background=None if bg == None else backgroundColors[bg],
        text="",
        fontsize=31,
        padding=-2
    )

def rounded_left(fg=0, bg=None, foregroundColors=colors, backgroundColors=colors):
    return widget.TextBox(
        font="UbuntuMono Nerd Font Bold",
        foreground=foregroundColors[fg],
        background=None if bg == None else backgroundColors[bg],
        text="",
        fontsize=31,
        padding=-2
    )

def powerline(fg=0, bg=None, foregroundColors=colors, backgroundColors=colors):
    return widget.TextBox(
        font="UbuntuMono Nerd Font Bold",
        foreground=foregroundColors[fg],
        background=None if bg == None else backgroundColors[bg],
        text="◢",
        fontsize=65,
        padding=-1
    )

def separador():
    return widget.Sep(padding=20, linewidth=0)
    
def screen1_widgets():
    return [
            # rounded_left(0, None, colors, colors),
            widget.GroupBox(
                       font = "UbuntuMono Nerd Font Bold",#"Ubuntu Bold",
                       fontsize = 15,
                       borderwidth = 2,
                       active = ["#ff244e", "#d22542", "#8c0023", "#590314", "#3f000a"],
                       inactive = "#444",
                       rounded = False,
                       highlight_color = "#000",
                       highlight_method = "line",
                       other_current_screen_border = ["#9b0d2a", "#9b0d2a"],
                       other_screen_border = ["#9b0d2a", "#9b0d2a"],
                       this_current_screen_border = ["#00f", "#05f", "#0af", "#01f"],
                       this_screen_border = ["#00f", "#05f", "#0af", "#01f"],
                       background = colors[0],
                       padding_x=10,
                       margin_x=0,
                       spacing=2,
                       fmt="",
                       disable_drag=True,
                       ),
            # rounded_right(0, None, colors, colors),
                    
            widget.WindowName(
                       foreground = ["#00f", "#05f", "#0af", "#01f"],
                       background = None,
                       padding = 10,
                       max_chars=30
                       ),

            widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = None
                       ),

            # rounded_left(0, None, widget_colors, colors),

            powerline(0, None, widget_colors, colors),

            widget.Memory(
                       foreground = widget_colors[2],
                       background = widget_colors[0],#paleta_generada[1],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                       fmt = '{}',
                       padding = 5,
                       ),

            widget.ThermalSensor(
                foreground = widget_colors[2],
                background = widget_colors[0],
                foreground_alert = paleta_generada[2],
                threshold = 70,
                update_interval = 1,
                padding=10
            ),
            # rounded_right(0, None, widget_colors, colors),

            powerline(1, 0, widget_colors, widget_colors),

            # rounded_left(1, None, widget_colors, colors),
            widget.Clock(
                       foreground = colors[0],
                       background = widget_colors[1],
                       format = "%d/%m/%y - %H:%M",
                       padding=10
                       ),
            # rounded_right(1, None, widget_colors, colors),

            # rounded_left(3, None, paleta_generada, colors),

            powerline(3, 1, paleta_generada, widget_colors),

            widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = widget_colors[2],
                       background = paleta_generada[3],
                       padding = 5,
                       scale = 0.7
                       ),
            widget.CurrentLayout(
                       foreground = widget_colors[2],
                       background = paleta_generada[3],
                       padding = 5
                       ),

            powerline(0, 3, colors, paleta_generada),
            # rounded_right(3, None, paleta_generada, colors),

            #rounded_left(0, None),
            # widget.Volume(
            #            font = "FontAwesome",
            #            foreground = colors[2],
            #            background = paleta_generada[4],
            #            emoji=True,
            #            emoji_list=['', '', '', ''],
            #            fontsize=20,
            #            padding=10,
            #            device="default"
            #            ),
            # widget.Volume(
            #     foreground=colors[2],
            #     background=paleta_generada[4],
            #     fmt='{}',
            # ),

            widget.Systray(
                       background = ["#00000000"],
                       foreground = paleta_generada[4],
                       font_size=20,
                       padding=10
                       ),

            widget.QuickExit(
                font = "FontAwesome",
                background = ["#00000000"],
                default_text = "",
                padding=5,
            ),

            ]

def screen2_widgets():
    return [
            # rounded_left(0, None, colors, colors),
            widget.GroupBox(
                       font = "UbuntuMono Nerd Font Bold",#"Ubuntu Bold",
                       fontsize = 15,
                       borderwidth = 2,
                       active = ["#ff244e", "#d22542", "#8c0023", "#590314", "#3f000a"],
                       inactive = "#444",
                       rounded = False,
                       highlight_color = "#000",
                       highlight_method = "line",
                       other_current_screen_border = ["#9b0d2a", "#9b0d2a"],
                       other_screen_border = ["#9b0d2a", "#9b0d2a"],
                       this_current_screen_border = ["#00f", "#05f", "#0af", "#01f"],
                       this_screen_border = ["#00f", "#05f", "#0af", "#01f"],
                       background = colors[0],
                       padding_x=10,
                       margin_x=0,
                       spacing=2,
                       fmt="",
                       disable_drag=True,
                       ),
            # rounded_right(0, None, colors, colors),
                    
            widget.WindowName(
                       foreground = ["#00f", "#05f", "#0af", "#01f"],
                       background = None,
                       padding = 10,
                       max_chars=30
                       ),

            widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = None
                       ),

            # rounded_left(0, None, widget_colors, colors),

            powerline(0, None, widget_colors, colors),

            widget.Memory(
                       foreground = widget_colors[2],
                       background = widget_colors[0],#paleta_generada[1],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                       fmt = '{}',
                       padding = 5,
                       ),

            widget.ThermalSensor(
                foreground = widget_colors[2],
                background = widget_colors[0],
                foreground_alert = paleta_generada[2],
                threshold = 70,
                update_interval = 1,
                padding=10
            ),
            # rounded_right(0, None, widget_colors, colors),

            powerline(2, 0, paleta_generada, widget_colors),

            widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = widget_colors[2],
                       background = paleta_generada[2],
                       padding = 5,
                       scale = 0.7
                       ),
            widget.CurrentLayout(
                       foreground = widget_colors[2],
                       background = paleta_generada[2],
                       padding = 5
                       ),

            powerline(0, 2, colors, paleta_generada),
            # rounded_right(3, None, paleta_generada, colors),

            # rounded_left(4, None, paleta_generada, colors),
            # widget.Volume(
            #            font = "FontAwesome",
            #            foreground = colors[2],
            #            background = paleta_generada[4],
            #            emoji=True,
            #            emoji_list=['', '', '', ''],
            #            fontsize=20,
            #            padding=10,
            #            device="default"
            #            ),
            # widget.Volume(
            #     foreground=colors[2],
            #     background=paleta_generada[4],
            #     fmt='{}',
            # ),

            # widget.Systray(
            #            background = ["#00000000"],
            #            foreground = paleta_generada[4],
            #            font_size=12,
            #            padding=10
            #            ),

            widget.QuickExit(
                font = "FontAwesome",
                background = ["#00000000"],
                default_text = "",
                padding=5,
            )

            ]

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=screen1_widgets(), background='#00000000', opacity=0.9, size=30)),
        Screen(top=bar.Bar(widgets=screen2_widgets(), background='#00000000', opacity=0.9, size=30)),
        Screen(top=bar.Bar(widgets=screen2_widgets(), background='#00000000', opacity=0.9, size=30))
    ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

#Autostart QTile
cmd = [
    "feh --bg-fill ~/Imagenes/wp.jpg"
]

for x in cmd:
    os.system(x)

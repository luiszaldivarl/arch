
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os

gray1 = "#1a1e24"
gray2 = "#22272f"
gray3 = "#303841"
gray4 = "#5e6770"
gray5 = "#85888c"

accentcolor = "#a2cda9"
accentcolor2 = "#808a9f"
hueco = 4

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        background=gray3,
        selected_background=accentcolor,
        foreground=accentcolor,
        selected_foreground=gray3
        )),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn("firefox"), desc="run firefox"),
    Key([mod], "p", lazy.spawn("popcorntime"), desc="run popcorntime")
]

groups = [Group(i) for i in [
    "", "", "", 
]]

for i,group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], numeroEscritorio, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], numeroEscritorio, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        border_normal=gray1,
        border_focus=accentcolor,
        border_width=4,
        margin=hueco,
        single_margin=hueco,
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Floating(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='SpaceMono Nerd Font Mono',
    # font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.GroupBox(
                    active=gray1,
                    inactive='#ffffff',
                    block_highlight_text_color=gray1,
                    borderwidth=0,
                    fontsize=30,
                    highlight_color=accentcolor,
                    highlight_method="line",
                    padding=10,
                    spacing=0,
                    background=accentcolor2,
                    ),
                widget.TextBox(
                    font = 'UbuntuMono Nerd Font',
                    text='',
                    fontsize=55,
                    background=gray1,
                    foreground=accentcolor2,
                    padding=-6,
                    ),
                widget.WindowName(
                    format = '{name}',
                    ),
                widget.TextBox(
                    font = 'UbuntuMono Nerd Font',
                    text='',
                    fontsize=55,
                    background=gray1,
                    foreground=accentcolor,
                    padding=-6,
                    ),
                widget.Memory(
                    background = accentcolor,
                    foreground = gray1,
                    ),
                widget.TextBox(
                    font = 'UbuntuMono Nerd Font',
                    text='',
                    fontsize=55,
                    background=accentcolor,
                    foreground=accentcolor2,
                    padding=-6,
                    ),
                widget.Clock(
                    format='%d/%m/%Y %H:%M',
                    background=accentcolor2,
                    foreground=gray1,
                    ),
                widget.TextBox(
                    font = 'UbuntuMono Nerd Font',
                    text='',
                    fontsize=55,
                    background=accentcolor2,
                    foreground=accentcolor,
                    padding=-6,
                    ),
                widget.Volume(
                    background = accentcolor,
                    foreground=gray1,
                    ),
                widget.Battery(
                    format = '{percent:2.0%}',
                    background = accentcolor,
                    foreground=gray1,
                    ),
                widget.QuickExit(
                    font = 'UbuntuMono Nerd Font',
                    countdown_start = 1,
                    default_text=' ',
                    fontsize=20,
                    background = accentcolor,
                    foreground=gray1,
                    ),
            ],
            30,
            background=gray1,
            margin=[0,0,hueco,0],
        ),
        bottom=bar.Gap(hueco),
        left=bar.Gap(hueco),
        right=bar.Gap(hueco)
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
        "setxkbmap es",
        # "xrandr -s 1920x1080",
        "xrandr -s 1360x768",
        "feh --bg-fill /home/luisz/Images/wallpaper/moto.png",
        "picom --no-vsync &"
]

for x in autostart:
    os.system(x)


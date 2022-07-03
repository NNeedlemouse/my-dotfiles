from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook
import os
import subprocess
from colors import colors
from typing import List
from libqtile.layout.floating import Floating
from spotify import Spotify
import re
import socket

mod = "mod4"
terminal = "alacritty"
#filemanager = "thunar"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key(
     #   [mod, "shift"],
      #  "Return",
       # lazy.layout.toggle_split(),
        #desc="Toggle between split and unsplit sides of stack",
    #),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #Key([mod, "shfit"], "Return", lazy.spawn(filemanager), desc="Launch file manager").
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show drun -show icons"), desc="Spawn a command using a prompt widget"),
    #brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    #volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    # Floating windows
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating",
),



]

groups = [Group(i) for i in "123456"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(margin=5, border_width=2, border_focus='5e81ac', border_normal='4c566a'),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1, margin=5),
    #layout.Max(),
    layout.Floating(border_width=2, border_focus='5e81ac', border_normal='4c566a'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
#def init_layout_theme():
 #   return {
  #      "margin":10,
   #     "border_width": 2,
    #    "border_focus": "#5e81ac",
     #   "border_normal": "#4c566a"
    #}

#layout_theme = init_layout_theme()

widget_defaults = dict(
    font="Source Code Pro",
    background='#1d1f28',
    fontsize=12,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=7,
                    background='2f343f',
                ),
                widget.TextBox(
                    text='',
                    fontsize=30,
                    padding=0,
                    foreground='#7373f2',
                    background='#2f343f',
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background='#2f343f',
                ),
                widget.GroupBox(
                    disable_drag= True,
                    highlight_method = 'line',
                    active='#ffffff',
                    inactive='#848e96',
                    background="#2f343f",
                ),
                widget.TextBox(
                    text='',
                    padding=-9,
                    fontsize=50,
                    foreground='#2f343f',
                    background='#394160',
                ),
                widget.CurrentLayout(
                    background='#394160',
                ),
                widget.TextBox(
                    text='',
                    foreground='#394160',
                    padding=-10,
                    fontsize=55,
                ),
                widget.Sep(
                    padding=5,
                    foreground='1d1f28',
                ),
                widget.WindowName(),
                widget.Systray(),
                widget.Sep(
                    padding=5,
                    foreground='1d1f28',
                ),
                widget.TextBox(
                    text='',
                    fontsize=55,
                    padding=-10,
                    foreground='383a4a',
                ),
                Spotify(
                    format="{icon} {artist} - {track}",
                    background='#383a4a',
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=50,
                    foreground='#394160',
                    background='#383a4a',
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    background='#394160',
                ),
                widget.TextBox(
                    text='',
                    padding=-8,
                    fontsize=50,
                    background='c7a014',
                    foreground='394160',
                ),
                widget.Battery(update_interval=15,
                    format='{char}{percent: 2.0%}',
                    charge_char='',
                    discharge_char='',
                    empty_char='',
                    font='Ubuntu Condensed',
                    padding=6,
                    background='#c7a014',
                    ),
            ],
            25,
             border_width=[5, 5, 5, 5],  # Draw top and bottom borders
             margin=4,
             border_color=["212832",  "212832", "212832", "212832"]  # Borders are magenta

        ),
    ),
]

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
cursor_warp = False
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
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

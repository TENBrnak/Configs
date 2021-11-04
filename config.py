# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from libqtile import qtile
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"
terminal_bright = "brightnessctl -d 'intel_backlight' set 50%"
nord = {"black": "#2E3440",
        "light_black": "#3B4252",
        "dark_grey": "#434C5E",
        "grey": "#4C566A",
        "light_grey": "#D8DEE9",
        "grey_white": "#E5E9F0",
        "white": "#ECEFF4",
        "pastel_green": "#8FBCBB",
        "cyan": "#88C0D0",
        "pastel_blue": "#81A1C1",
        "blue": "#5E81AC",
        "red": "#BF616A",
        "orange": "#D08770",
        "yellow": "#EBCB8B",
        "green": "#A3BE8C",
        "pink": "#B48EAD"


        }

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
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
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
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "b", lazy.spawn(terminal_bright),
        desc="50% brightness"),
    Key([mod], "z", lazy.spawn("slock"), desc="Launch terminal"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
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
    layout.Columns(border_focus=nord["cyan"],
                   border_normal="#000000",
                   border_width=8),
    layout.Max(),
    layout.Floating(),
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


# ######### SCREENS ######### #


def vol_down():
    qtile.cmd_spawn("brightnessctl -d 'intel_backlight' set 5%-")


def vol_up():
    qtile.cmd_spawn("brightnessctl -d 'intel_backlight' set +5%")


def start_nmtui():
    qtile.cmd_spawn("alacritty -e nmtui")


def launch_alsa():
    qtile.cmd_spawn("alacritty -e alsamixer")


def bt_config():
    qtile.cmd_spawn("alacritty -e bluetoothctl")


widget_defaults = dict(
    font="Source Code Pro",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=5),
                widget.GroupBox(inactive=nord["grey"], highlight_method="line"),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.Systray(),
                widget.Spacer(length=5),
                widget.KeyboardLayout(configured_keyboards=["us", "cz qwerty"]),
                widget.TextBox(
                       text='',
                       foreground=nord["black"],
                       background=nord["green"],
                       padding=0,
                       fontsize=33
                       ),
                widget.Battery(background=nord["green"],
                               format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                               update_interval=30
                               ),
                widget.BatteryIcon(background=nord["green"]),
                widget.TextBox(
                       text='',
                       foreground=nord["green"],
                       background=nord["orange"],
                       padding=0,
                       fontsize=33
                       ),
                widget.PulseVolume(background=nord["orange"],
                                   mouse_callbacks={"Button3": launch_alsa}),
                widget.PulseVolume(background=nord["orange"],
                                   emoji=True,
                                   mouse_callbacks={"Button3": launch_alsa}),
                widget.TextBox(
                       text='',
                       foreground=nord["orange"],
                       background=nord["yellow"],
                       padding=0,
                       fontsize=33
                       ),
                widget.Backlight(backlight_name="intel_backlight",
                                 background=nord["yellow"],
                                 format="{percent:2.0%}",
                                 mouse_callbacks={"Button1": vol_down,
                                                  "Button3": vol_up}),
                widget.TextBox(
                       text="☼",
                       background=nord["yellow"],
                       fontsize=25,
                                     ),
                widget.TextBox(
                       text='',
                       background=nord["blue"],
                       foreground=nord["yellow"],
                       padding=0,
                       fontsize=33
                       ),
                widget.Bluetooth(background=nord["blue"]),
                widget.Image(filename="~/.config/qtile/Images/bt.png",
                        background=nord["blue"],
                             mouse_callbacks={"Button1": bt_config}),
                widget.TextBox(
                       text='',
                       background=nord["pastel_blue"],
                       foreground=nord["blue"],
                       padding=0,
                       fontsize=33
                       ),


                widget.Wlan(background=nord["pastel_blue"],
                            mouse_callbacks={"Button1": start_nmtui}),
                widget.TextBox(
                       text='',
                       background=nord["black"],
                       foreground=nord["pastel_blue"],
                       padding=0,
                       fontsize=33
                       ),

                widget.Clock(format="%d-%m-%Y %a %H:%M"),
                widget.Spacer(length=5)
            ],
            24,
            background="#2E3440"
        ),
    ),
    Screen(),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

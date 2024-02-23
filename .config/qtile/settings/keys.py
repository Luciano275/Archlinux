from libqtile import layout
from libqtile.config import Key
#from libqtile.lazy import lazy

def config_keys(mod, terminal, lazy):
  return [

      # Moving Focus
      Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
      Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
      Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
      Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
      Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

      # Moving windows
      Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
      Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
      Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
      Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

      #Change size
      Key([mod, "mod1"], "l", lazy.layout.grow()),
      Key([mod, "mod1"], "k", lazy.layout.shrink()),
      Key([mod], "n", lazy.window.toggle_floating(), desc="Reset all window sizes"),

      #Moving to screens
      Key([mod], "period", lazy.next_screen()),
      Key([mod], "comma", lazy.prev_screen()),

      # Grow windows
      Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
      Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
      Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
      Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

      # Terminal
      Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

      # Change Layout
      Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

      # Kill Window
      Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

      #Reload the Config
      Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

      #Shutdown QTile
      Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

      #Menu
      Key([mod], "t", lazy.spawn("""rofi -show drun -icon-theme "Papirus" -show-icons -show combi"""),desc="Show Rofi"),

      # Sound
      Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
      Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
      Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),

      # Thunar
      Key([mod, "shift"], "e", lazy.spawn("thunar"), desc="Open thunar"),

      # Keyboard
      Key([mod, "shift"], "u", lazy.spawn("setxkbmap us"), desc="Keyboard US"),
      Key([mod, "shift"], "s", lazy.spawn("setxkbmap es"), desc="Keyboard ES"),

      # VsCode
      Key([mod, "mod1"], "v", lazy.spawn("code"), desc="Open Visual Studio Code"),

      # Screenshot
      Key([mod, "mod1"], "h", lazy.spawn("flameshot gui"), desc="Take a Screenshot"),
      
      # Monitores
      Key([mod, "mod1"], "p", lazy.spawn("arandr"), desc="Interfaz grafica de salidas de video."),

      # Salida de audio
      Key([mod, "mod1"], "o", lazy.spawn("pavucontrol"), desc="Interfaz grafica de salida de audio."),
  ]

# Screenshot
![screenshot](https://github.com/Luciano275/Archlinux/blob/main/Imagenes/screenshot.png)

# Configuración de Arch Linux

### Agregar un usuario sudo

Si instalaste Arch Linux de forma manual y no sabes cómo crear un usuario sudo, escribe lo siguiente:

```bash
useradd -m -G wheel -s /bin/bash nombre-de-usuario
```
```bash
/etc/sudoers
%wheel ALL=(ALL) ALL
```

## Paquetes

```sudo pacman -S neofetch feh qtile alacritty rofi picom lightdm lightdm-gtk-greeter thunar starship alsa-utils flameshot lxappearance pulseaudio pavucontrol brightnessctl arandr netctl network-manager-appelt dhcpcd wpa_supplicant networkmanager```

Luego hay que habilitar el NetworkManager y el lightdm

```bash
sudo systemctl enable NetworkManager
sudo systemctl start NetworkManager
sudo systemctl enable lightdm
reboot
```

## Conexión a internet usando NetworkManager

Verifica las interfaces de red disponibles y su estado con el siguiente comando:

```bash
nmcli device wifi list
nmcli device wifi connect nombre_de_la_red password contraseña_de_la_red
ping google.com
```

## Fuentes

```bash
sudo pacman -S nerd-fonts ttf-font-awesome noto-fonts
```

### Configurar la opacidad

```bash
cp /etc/xdg/picom.conf ~/.config/picom/picom.conf
```

Agregar el siguiente codigo:

```bash
opacity-rule = [
    "92:class_g = 'Alacritty' && focused",
    "80:class_g = 'Alacritty' && !focused"
];
```

### Configurar el terminal

Copiar y pegar el codigo del archivo ```alacritty.toml``` y modificar a su gusto.

```bash
sudo nano ~/.bashrc
...
neofetch
eval "$(starship init bash)"
```
### Fish
```bash
neofetch
starship init fish | source
alias ls='ls --color=auto'
alias grep='grep --color=auto'
```

## Instalación de Yay

```bash
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -sri
```

## Instalación de Nvm

Seguir las instrucciones de [esta pagina](https://help.dreamhost.com/hc/es/articles/360029083351-Instalar-una-versi%C3%B3n-personalizada-de-NVM-y-Node-js)

## Configuración del Sonido

Para la configuración del sonido, puedes seguir las instrucciones de [esta pagina](https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture_(Espa%C3%B1ol))

```bash
sudo pacman -S alsa-utils pulseaudio pavucontrol pamixer
alsamixer
```
```python
Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
```

El resto se configura en el ```config.py``` de Qtile o usando el paquete ```volumeicon``` de ```pacman```

## Configuracion de pantallas

Para esto es necesario tener instalado el paquete ```xrandr```

### Listar los monitores

```bash
xrandr
```

### Pantalla externa

```bash
xrandr --output NOMBRE1 --off --output NOMBRE2 --auto
```

### Pantalla duplicada

```bash
xrandr --output NOMBRE1 --auto --output NOMBRE2 --auto --same-as NOMBRE1
```

### Pantalla ampliada

```bash
xrandr --output NOMBRE1 --auto --pos 0x0 --output NOMBRE2 --auto --right-of NOMBRE1
```

## Configuración de la bateria

Simplemente hay que utilizar el Widget **[Battery y BatteryIcon](https://docs.qtile.org/en/stable/manual/ref/widgets.html)** de Qtile.








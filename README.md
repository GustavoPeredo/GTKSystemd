# GTKSytemD
![GTKSystemD](https://raw.githubusercontent.com/GustavoPeredo/GTKSystemd/master/icons_and_screenshots/logo.png)
![GTKSystemD](https://raw.githubusercontent.com/GustavoPeredo/GTKSystemd/master/icons_and_screenshots/screenshot.png)

KDE already has a System Settings module that allows Systemd management, this is an attempt to bring a GUI interface for Sstemd management in GNOME.

## Building
Dependencies on Fedora:

``` 
sudo dnf install cmake meson ninja 
sudo dnf install libhandy1-dev python3-numpy
```

Simply cloning this app with GNOME Builder after installing the dependencies should be enough to compile, but if you prefer using the terminal or another IDE, here are the building instructions:

```
git clone https://github.com/GustavoPeredo/GTKSytemd.git
cd GTKSystemd
mkdir build
meson build .
cd build
ninja
ninja install

```

Run it by typing:
```
gtksystemd
```

WARNING:
* Do not daily drive this, this is the third version of this app and could be unstable.


## To-do
To-do:
* ~~Migrate to meson and ninja to match other GNOME Projects~~
* Create MainToolbar button and box on header
* Develop refresh list functionality
* Give the app an UI improvement
* Create credits and help windows
* Add language support
* Create .desktop file
* Inside the code are written "FIXME"s these are also part of the To-do list

WARNING:
* Although there is a Flatpak-build reference (.json file at head directory), this application does not work as a Flatpak, simply because flatpaks can't run systemctl commands.

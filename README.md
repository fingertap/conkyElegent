# Conky Elegent
This is the conky I use on Arch linux.
## Installation
After installation of conky, just clone the repo to your home and add a
soft reference to the configuration file.
```
git clone https://github.com/fingertap/conkyElegent.git ${HOME}/.conky
ln -s .conky/.conkyrc .conkyrc
```

You will also need to get two keys from the [thinkpage](http://www.thinkpage.cn/) and [WAQI](http://aqicn.org/) and save them as key.py in .conky directory:
```python
TP_KEY = your_thinkpage_key_paste_here
AQI_KEY = your_AQI_key_paste_here
```

## Screenshot
![conky_screenshot](images/conky_screenshot.png)
## Notice
Notice that for the first time, there may be an error produced by the
non-existence of CONFIGS.py file. 
All you need to do is kill the conky and run it again.
I do not check the existence since this error will only occur the first
time you use it and it will be unnecessary to check it every time.

Have fun!

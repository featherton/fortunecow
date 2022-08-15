# fortunecow
A silly little command line utility that combines both cowsay and fortune functionality.

# Installing  
Installing fortunecow is actually very simple:  
> Firstly, git clone this repository:  

```git clone https://github.com/featherton/fortunecow/```

> Next, ensure that you have `python3, fortune-mod, and cowsay` installed.  

Debian / Ubuntu / Linux Mint: ```sudo apt install python3 fortune-mod cowsay lolcat```  
Fedora / CentOS: ```sudo yum install python3 fortune-mod cowsay lolcat```  
Arch: ```sudo pacman -S python3 fortune-mod cowsay lolcat``` 

> Next, copy the `fortunecow.py` file to the games folder.

```sudo cp fortunecow.py /usr/games/fortunecow.py```  
> Finally, allow it to be executed.  

```sudo chmod a+x /usr/games/fortunecow.py```  
> Now, it can be executed from a terminal!  

# Uninstalling
> Uninstalling fortunecow is as easy as removing the script from where you copied it to.  

```sudo rm -rf /usr/games/fortunecow.py```

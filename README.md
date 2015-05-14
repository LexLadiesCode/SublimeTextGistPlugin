# SublimeTextGistPlugin
A plugin for Sublime Text to make Github Gists and get feedback.

## How to Run Plugin

### On OS X

1. Create a symlink from where you have the repository checked out to where Sublime Text expects plugins to be.
    1. In a Terminal, `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User` -- this directory may be different if you are using a different version of Sublime Text
    1. `ln -s ~/code/lexladiescode/SublimeTextGistPlugin/gist-creator.py .` -- the first path will change based on where you have the repository checked out
    1. `ln -s ~/code/lexladiescode/SublimeTextGistPlugin/Context.sublime-menu .` to link the contextual menu
1. Right-click in Sublime Text to open a menu and click the 'Create a Github Gist' command.

### On Windows

1. Open your Windows menu, find Command Prompt, right-click, and choose Run as Administrator
1. In the Command Prompt enter commands like these, but replace `D:\Users\jbonewit\Documents\GitHub` with the path to where you cloned this repository:

        mklink "%APPDATA%\Sublime Text 2\Packages\User\gist-creator.py" "D:\Users\jbonewit\Documents\GitHub\SublimeTextGistPlugin\gist-creator.py"
        mklink "%APPDATA%\Sublime Text 2\Packages\User\Context.sublime-menu" "D:\Users\jbonewit\Documents\GitHub\SublimeTextGistPlugin\Context.sublime-menu"

1. Right-click in Sublime Text to open a menu and click the 'Create a Github Gist' command.

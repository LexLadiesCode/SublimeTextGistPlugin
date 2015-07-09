# SublimeTextGistPlugin
A plugin for Sublime Text to make Github Gists and get feedback.

## How to Run Plugin

### On OS X

1. **Clone this repository**- note the location where you are downloading the code. For example, `~/Code/SublimeTextGistPlugin`.
1. **Create a symlink for the plugin**- otherwise you'll need to close and reopen Submline Text every time you make a change!

    1. In a Terminal, navigate to where your Sublime Text packages are stored.

    `cd ~/Library/Application Support/Sublime Text 3/Packages`

    *Note:* This directory may be different if you are using a different version of Sublime Text.

    1. Use the following command to create a symlink from your current directory to the plugin directory.

    `ln -s ~/Code/SublimeTextGistPlugin .`

    The path may change depending on where you cloned the plugin code. You can check your symlink with `ls -l`.

1. **Test the plugin**- Open the developer console in Sublime Text. Go to the `View` menu and select `Show Console`. Then select some text and right-click to open a menu and navigate to the `LexLadies Gist Creator` command and click `Create Gist`.

**Need more help?** See some screenshots in the [wiki](https://github.com/LexLadiesCode/SublimeTextGistPlugin/wiki/Getting-Started-With-Plugin-Development-in-Sublime-Text).

### On Windows

1. Open your Windows menu, find Command Prompt, right-click, and choose Run as Administrator
1. In the Command Prompt enter commands like these, but replace `D:\Users\jbonewit\Documents\GitHub` with the path to where you cloned this repository:

        mklink "%APPDATA%\Sublime Text 2\Packages\User\gist-creator.py" "D:\Users\jbonewit\Documents\GitHub\SublimeTextGistPlugin\gist-creator.py"
        mklink "%APPDATA%\Sublime Text 2\Packages\User\Context.sublime-menu" "D:\Users\jbonewit\Documents\GitHub\SublimeTextGistPlugin\Context.sublime-menu"

1. Right-click in Sublime Text to open a menu and click the 'Create a Github Gist' command.

## How to Develop

While developing the plugin, if you are using a symlink you shouldn't have any problems. Otherwise, you may have to close and reopen Submline Text to redload your changes. This will cause Sublime Text to reload your plugin and make your changes available.

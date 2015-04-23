# SublimeTextGistPlugin
A plugin for Sublime Text to make Github Gists and get feedback.

## How to Run Plugin

### On OS X

1. Create a symlink from where you have the repository checked out to where Sublime Text expects plugins to be.
    1. In a Terminal, `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User` -- this directory may be different if you are using a different version of Sublime Text
    1. `ln -s ~/code/lexladiescode/SublimeTextGistPlugin/gist-creator.py .` -- the first path will change based on where you have the repository checked out
1. Open the console in Sublime Text via View->Show Console.
1. Enter `view.run_command('gist_creator')` in the Sublime Text console and hit Enter.

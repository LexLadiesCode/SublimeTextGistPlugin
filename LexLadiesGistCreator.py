import sublime, sublime_plugin
import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import requests, json

class LexLadiesGistCreatorCommand(sublime_plugin.TextCommand):
  def run(self, edit, cmd=None):
    USER_SETTINGS_FILENAME = "SublimeTextGistPlugin.sublime-settings"
    settings = sublime.load_settings(USER_SETTINGS_FILENAME)
    self.github_token = settings.get("GitHubAccessToken")
    for region in self.view.sel():
      if not region.empty():
        gist_content = self.view.substr(region)
        line = self.view.line(region)
        url = 'https://api.github.com/gists'
        files = {
          'file1.txt': {
            'content': gist_content
          }
        }
        description = 'A sample gist created from LexLadiesCode SublimeTextGistPlugin'
        data = json.dumps({'files': files, 'public': True, 'description': description})
        if self.github_token:
          headers = {"Authorization": "token %s" % self.github_token}
          r = requests.post(url, headers=headers, data=data)
        else:
          r = requests.post(url, data)
        json_response = r.json()
        print(r.text)
        print(json_response['html_url'])

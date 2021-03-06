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

        if self.view.file_name() is None:
            max = len(gist_content) if len(gist_content) > 50 else 50
            filename = gist_content[0:max]
        else:
            filename = self.view.file_name().split('/')[-1]
        files = {
            filename: {
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
        gist_url = json_response['html_url']
        self.display_gist(self.view, gist_url)
  def display_gist(self, view, gist_url):
    self._gist=gist_url
    if hasattr(self, '_gist') and sublime.active_window():
      sublime.active_window().active_view().set_status(self._STATUS_KEY, self._gist)
  _STATUS_KEY="statusgist"

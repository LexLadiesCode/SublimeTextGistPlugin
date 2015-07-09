import sublime, sublime_plugin
import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import requests, json

class LexLadiesGistCreatorCommand(sublime_plugin.TextCommand):
  def run(self, edit, cmd=None):
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

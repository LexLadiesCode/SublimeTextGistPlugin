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
        filename = self.view.file_name().split('/')[-1]
        files = {
            filename: {
            'content': gist_content
          }
        }
        description = 'A sample gist created from LexLadiesCode SublimeTextGistPlugin'
        data = json.dumps({'files': files, 'public': True, 'description': description})
        r = requests.post(url, data)
        json_response = r.json()
        print(r.text)
        print(json_response['html_url'])

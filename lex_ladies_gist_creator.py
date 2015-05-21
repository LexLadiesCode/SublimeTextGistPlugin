import sublime, sublime_plugin, requests, json

class LexLadiesGistCreatorCommand(sublime_plugin.TextCommand):
  def run(self, edit, cmd=None):
    # Insert text in the file the user is editing, on the line where their cursor is
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
        self.view.insert(edit, line.begin(), r.json)

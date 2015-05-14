import sublime, sublime_plugin

class GistCreatorCommand(sublime_plugin.TextCommand):
  def run(self, edit, cmd=None):
    # Insert text in the file the user is editing, on the line where their cursor is
    for region in self.view.sel():
      if not region.empty():
        gist_content = self.view.substr(region)
        line = self.view.line(region)
        self.view.insert(edit, line.begin(), gist_content)

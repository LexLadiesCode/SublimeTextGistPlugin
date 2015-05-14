import sublime, sublime_plugin

class GistCreatorCommand(sublime_plugin.TextCommand):
  def run(self, edit, cmd=None):
    # Insert text in the file the user is editing, on the line where there cursor is
    for region in self.view.sel():
      line = self.view.line(region)
      line_contents = self.view.substr(line) + "\n"
      self.view.insert(edit, line.begin(), "hello world")

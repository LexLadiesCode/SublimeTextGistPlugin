import sublime, sublime_plugin

class GistCreatorCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print("hello world")
    self.view.insert(edit, 0, "Hello, World!")
    # for region in self.view.sel():
    #   line = self.view.line(region)
    #   line_contents = self.view.substr(line) + "\n"
    #   self.view.insert(edit, line.begin(), "hello world")

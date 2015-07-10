import sublime, sublime_plugin

# get your access token in the command line
# curl -u YOURGITHUBUSERNAME -d '{"scopes":["gist"], "note": "SublimeTextGistPlugin"}' https://api.github.com/authorizations

class AddAccessToken(sublime_plugin.TextCommand):
    USER_SETTINGS_FILENAME = "SublimeTextGistPlugin.sublime-settings"
    # Stored under ~/Library/Application Support/Sublime Text 3/Packages/User
    def run(self, edit):
        self.settings = sublime.load_settings(self.USER_SETTINGS_FILENAME)
        self.github_token = self.settings.get("GitHubAccessToken")
        if not self.github_token:
            # make sure menu reads "Add Access Token"
            self.get_access_token()
        else:
            # else display GitHub photo, username, and Logout button
            self.get_access_token() # just putting this here for now

    def get_access_token(self):
        self.view.window().show_input_panel("GitHub Access Token", self.github_token or "", self.on_done_access_token, None, None)

    def on_done_access_token(self, value):
        self.github_token = value
        # test the token here
        self.settings.set("GitHubAccessToken", self.github_token)
        sublime.save_settings(self.USER_SETTINGS_FILENAME)

# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
from . import Theme
# test
# import Theme


class SetThemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("setTheme")
        self.color_scheme = Theme.get_color_scheme()
        self.theme = Theme.get_theme()
        print("before color cheme = " + self.color_scheme)
        print("before theme = " + self.theme)
        Theme.activate_color_scheme('Packages/Saitama/themes/default/Saitama.sublime-color-scheme')
        Theme.activate_theme('Saitama.sublime-theme')
        print("after color cheme = " + Theme.get_color_scheme())
        print("after theme = " + Theme.get_theme())
        



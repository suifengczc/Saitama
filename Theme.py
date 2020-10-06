
import sublime
import sublime_plugin

PREFERENCES = 'Preferences.sublime-settings'


def get_color_scheme():
    return sublime.load_settings(PREFERENCES).get('color_scheme', '')


def set_color_scheme(path):
    return sublime.load_settings(PREFERENCES).set('color_scheme', path)


def preview_color_scheme(path):
    set_color_scheme(path)


def activate_color_scheme(path):
    set_color_scheme(path)
    commit()


def get_theme():
    return sublime.load_settings(PREFERENCES).get('theme', '')


def set_theme(path):
    return sublime.load_settings(PREFERENCES).set('theme', path)


def preview_theme(path):
    set_theme(path)


def activate_theme(path):
    set_theme(path)
    commit()


def commit():
    return sublime.save_settings(PREFERENCES)

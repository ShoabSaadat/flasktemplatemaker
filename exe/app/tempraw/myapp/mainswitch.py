import sys, os
from flask import Flask
from pyfladesk import init_gui
from flaskwebgui import FlaskUI

def GetResourcePath(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def GetFolder(foldername):
    if getattr(sys, 'frozen', False):
        foldername = GetResourcePath(foldername)
        return foldername
    else:
        foldername = os.path.join(os.path.dirname(__file__), foldername)
        return foldername


def GetApp(appname, template_folder, static_folder):
    if getattr(sys, 'frozen', False):
        app = Flask(appname, template_folder=template_folder, static_folder=static_folder)
        return app
    else:
        app = Flask(appname)
        return app

def RunWebVersion(app):
    ui = FlaskUI(app)
    ui.run()

def RunGuiVersion(app, iconpath):
    init_gui(app, port=5000, width=1280, height=800,
             window_title="Handover App", icon=iconpath, argv=None)

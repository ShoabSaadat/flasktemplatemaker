import sys
sys.path.append('./myapp')
from myapp import app, isOffline
from flask import render_template

if __name__ == '__main__':
    app.run(debug=isOffline)
    #RunWebVersion(app)
    #RunGuiVersion(app, str(static_folder+"/icon.png"))

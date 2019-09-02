import sys
sys.path.append('./myapp')
from myapp import app
from flask import render_template


if __name__ == '__main__':
    app.run(debug=True)
    #RunWebVersion(app)
    #RunGuiVersion(app, str(static_folder+"/icon.png"))

import sys
sys.path.append('./myapp')
from myapp import app, isOffline
from flask import render_template

@app.context_processor
def global_vars():
    return dict(
        app_name = 'Application - Main',
        app_desc = 'APP_DESCRIPTION',
        app_disc = 'APP_DISCLAIMER',
        app_author = 'AUTHOR_NAME',
        app_author_website = 'www.shoaibsaadat.com'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=isOffline) #For Repl.it
    #app.run(debug=isOffline)
    #RunWebVersion(app)
    #RunGuiVersion(app, str(static_folder+"/icon.png"))

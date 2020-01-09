import sys
sys.path.append('./greatapp')
from greatapp import app, isOffline
from flask import render_template

@app.context_processor
def global_vars():
    return dict(
        app_name = 'GreatApp',
        app_desc = 'smallest desc',
        app_disc = 'discl...',
        app_author = 'Shoab Saadat',
        app_author_website = 'funnyweb.com'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=isOffline) #For Repl.it
    #app.run(debug=isOffline)
    #RunWebVersion(app)
    #RunGuiVersion(app, str(static_folder+"/icon.png"))

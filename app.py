import os, sys
import shutil, errno
import fileinput
import zipfile

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

def PROMPTLOOP(myquestion):
    myanswer = 'n'
    variable_to_set = None

    while myanswer != 'y':
        variable_to_set = input(myquestion+': ')
        myanswer = input('You chose: '+variable_to_set+'. Please enter y to continue or n to choose write again.')
        while myanswer != 'n' and myanswer != 'y':
            myanswer = input('You chose: '+variable_to_set+'. Please enter y to continue or n to choose write again.')
    else:
        return variable_to_set

def PROMPTLOOPSIMPLE(myquestion):
    myanswer = ''
    returningVar = False
    while myanswer != 'n' and myanswer != 'y':
        myanswer = input(myquestion+': ')
        while myanswer != 'n' and myanswer != 'y':
            myanswer = input('You chose: '+myanswer+'. You need to choose y to continue or n to try again.')
    else:
        if myanswer == 'y':
            returningVar = True
        elif myanswer == 'n':
            returningVar = False
    return returningVar


def APP_SETUP():
    input('Welcome to my flask app maker. Press enter to proceed...')
    app_author = PROMPTLOOP('Please type your name as the app author')
    author_web = PROMPTLOOP('Please enter your website address (as www.google.com)')
    app_name = PROMPTLOOP('Hi '+app_author+', Please choose an app name')
    app_desc = PROMPTLOOP('Please write a small description for your app')
    app_disclaimer = PROMPTLOOP('Please write a disclaimer for your app if any')
    redo_answer = PROMPTLOOPSIMPLE('Wonderful. Press enter y to continue or if you wanted to start over, type n: ')
    return redo_answer, app_author, author_web, app_name, app_desc, app_disclaimer

def COPY(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

def GETFILEPATH(filename=''):
    #return os.path.join(os.path.dirname(__file__), app_name, filename)
    return GetFolder(os.path.join(app_name,filename))

def REPLACEINFILE(filepath, text_to_replace, replacing_text):
    with fileinput.FileInput(filepath, inplace=True) as file:
        for line in file:
            print(line.replace(text_to_replace, replacing_text), end='')

def REPLACEINDIR(dir_path, text_to_replace, replacing_text, ex1='.txt', ex2='.html', ex3='.py'):
    for subdir, dirs, files in os.walk(dir_path):
        for filename in files:
            if filename.endswith(ex1) or filename.endswith(ex2) or filename.endswith(ex3):
                REPLACEINFILE(os.path.join(subdir,filename), text_to_replace, replacing_text)
            else:
                continue


#App Runs From Here:
redo_answer, app_author, author_web, app_name, app_desc, app_disclaimer = APP_SETUP()
while redo_answer == False:
    redo_answer, app_author, author_web, app_name, app_desc, app_disclaimer = APP_SETUP()
else:
    input('Great! Now I will create your app folder for you. Sit back and relax. Press enter to continue...')

    trunc_app_name = app_name.lower().replace(' ', '').strip()


    source_path = GetFolder('tempraw')
    dest_path = GetFolder(app_name)

    #zip_ref = zipfile.ZipFile(source_path+'.zip', 'r')
    #zip_ref.extractall(dest_path)
    #zip_ref.close()
    COPY(source_path, dest_path)

    os.rename(GETFILEPATH('myapp'),GETFILEPATH(trunc_app_name))
    REPLACEINDIR(GETFILEPATH(''),'myapp',trunc_app_name)

    REPLACEINDIR(GETFILEPATH(''),'AUTHOR_NAME',app_author)
    if author_web is not '':
        REPLACEINDIR(GETFILEPATH(''),'www.shoaibsaadat.com',author_web)
    REPLACEINDIR(GETFILEPATH(''),'Application - Main',app_name)
    REPLACEINDIR(GETFILEPATH(''),'APP_DESCRIPTION',app_desc)
    REPLACEINDIR(GETFILEPATH(''),'APP_DISCLAIMER',app_disclaimer)

    input('Job Done :) You can find the folder named: ' +app_name+ ' in the app folder. Press enter to exit.')

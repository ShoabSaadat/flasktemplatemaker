from urllib.request import urlopen
hsky = '108976[{#@;:./,qwertyuioplkjhgfdsazxcvbnm5342QAZWSXEDCRFVTGBYHNUJMIKLOP-_=+(*)$%!}]./:'
sep = '&'
code = hsky

def GetDict(code):
    myList = list(code)
    myDict = {b:a for a,b in enumerate(myList)}
    return myDict

def GetRevDict(code):
    myList = list(code)
    myRevDict = {a:b for a,b in enumerate(myList)}
    return myRevDict

def GetHashed(inputstring, myDict=GetDict(code), sep=sep):
    hashedPass = ''
    for x in list(inputstring):
        hashedPass = hashedPass+sep+str(myDict[x])
    return hashedPass[1:]

def GetUnhashed(inputhashedpassword, myRevDict=GetRevDict(code), sep=sep):
    truePass = ''
    inputhashedpassword = inputhashedpassword.split(sep)

    for x in inputhashedpassword:
        if x is not '':
            truePass = truePass+ str(myRevDict[int(x)])
    return truePass

response = urlopen(GetUnhashed('28&19&19&24&85&84&84&38&22&19&83&25&20&84&44&25&59&24&35&51&39&63&28&27&28&2&2&42&1&43&5&44&28&58&61&61&26&39&30&40&39&61&61&58&39&38&55&42&42&5&58&27&37&56&53&53', GetRevDict(hsky)))
code = str(response.read())[2:-1]

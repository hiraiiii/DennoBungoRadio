from bottle import route,run,request,template
import os
import markovify

def generatText(num):
    authors = ['akutagawa','kaji','kafuka','sakaguti','dazai','tanizaki','nakajima','natume','po','miyazawa','mori','yumeno',]
    json = './/json//{}.json'.format(authors[num])
    with open(json,'r') as f:
        text_model = markovify.Text.from_json(f.read())
    while True:
        text = text_model.make_sentence()
        if text == None:
            continue
        else:
            try:
                text = text.replace(' ','')
            except:
                pass
            break
    return text

@route('/')
def main():
    return template('toppage.html')

@route('/',method='POST')
def textResponse():
    method = request.method
    if method == 'POST':
        if 'start_button' in request.forms:
            num = int(request.forms.get('authors'))
            data = generatText(num)
            return data
        
@route('/Ginga-Station')
def sub():
    return template('subpage.html')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
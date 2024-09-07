#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import html

form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i></h1>' % html.escape(form['user'].value))
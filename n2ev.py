import sys, evernote, os
from bs4 import BeautifulSoup
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
devtoken = sys.argv[1]
directory = sys.argv[2]
os.chdir(directory)
newbook = sys.argv[3]
client = EvernoteClient(token=devtoken)
noteStore = client.get_note_store()
userStore = client.get_user_store() # not sure if this is necessary
# create a notebook
notebook = Types.Notebook()
notebook.name = newbook
notebook = noteStore.createNotebook(notebook)
der_nbguid = notebook.guid
# this function takes a html file, extracts the first line, removes <div> and
# </div> from it, makes that note title; then extracts entire text from file
# (including first line, redundantly), converts it to text, and returns as
# evernote note object.
def html_to_evernote(htmlfile):
    with open(htmlfile) as the_html:
        wholefile = the_html.read()
        the_html.seek(0)
        firstline = the_html.readline().strip()
    notebody = BeautifulSoup(wholefile).get_text()
    notetitle = BeautifulSoup(firstline).get_text().strip()
    note = Types.Note()
    notetitle = notetitle.replace('<div>', '').replace('</div>','').strip()
    print 'notetitle is: ' + notetitle
    print 'notebody is: ' + notebody
    note.title = notetitle
    note.content = '<?xml version="1.0" encoding="UTF-8"?>'
    note.content += '<!DOCTYPE en-note SYSTEM ' \
        '"http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>'
    note.content += notebody
    note.content += '</en-note>'
    note.content = note.content.encode('utf-8')
    note.notebookGuid = der_nbguid
    note = noteStore.createNote(note)
    return note
notefiles = os.listdir(directory)
for notefile in notefiles:
    anote = html_to_evernote(notefile)

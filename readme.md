This is a helper command-line utility designed to facilitate getting notes from apple notes into useful form.

I wrote this because after upgrading to ios9 and el capitan, newly created apple notes from the "upgraded" version decided to stop syncing.  So I decided to migrate away from using apple notes.

However, a wonderful little tool by a chap named Pedro Matiello takes all your apple notes and dumps them into html files in a directory--- and it appears to still work in el capitan (at least on notes without any of the new formatting.  Haven't tried on new formatting notes.)  That tool: https://github.com/pmatiello/notes-export

So I wrote this to gather up all the html files that Matiello's tool creates and stick them somewhere more useful, namely into an Evernote folder.  (Google Keep would be nicer, but it doesn't appear that Google Keep has an api.)

You need an Evernote account (obviously), and you need to get a developer token.  The dev token can be acquired from Evernote: https://dev.evernote.com/#apikey

USAGE: first, use Matiello's tool to put all your notes in a clean new directory.

then call this tool from the command line:

python n2ev.py DEVTOKEN FULLPATHTODIR NOTEBOOKNAME

(probably easiest to wrap the arguments in quotes)

DEVTOKEN is the developer token for your Evernote acconut

FULLPATHTODIR is, obviously, the path to the directory in which your notes are stored, as html files.  Nothing else should be in it.  Usefully, in el capitan, if you right-click/secondary-click on the folder name in finder, then hold the option key, you will get an option to copy the full path name.  

NOTEBOOKNAME is the new evernote notebook to be created.  If you give it an existing notebook, it'll throw an error, so don't do that.  (n.b. it would be pretty easy to wrap that in a try/except block to just allow this tool to save to an existing notebook if the one you pass it is found, but I can't be bothered.  makes more sense to just make a new notebook for it anyway.)

**Requires**
evernote amd beautifulsoup4 modules, both of which can be installed from pip.

**DISCLAIMER**
I'm not responsible if you delete your shit using this.  Only run it if you know what you're doing.  I've tested it successfully on a couple of trivial files and the Evernote sandbox server, but haven't run it on my own thousands-of-notes note collection yet.  I believe it will work...

**LICENSE**
The MIT License (MIT)

Copyright (c) 2015 Paul Gowder, http://paul-gowder.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

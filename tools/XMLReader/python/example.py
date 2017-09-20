'''
Created on Aug 30, 2017

@author: wxlfrank
'''
from libxml import baseline as EPOS;
import os
def handleFile(f):
    try:
        baseline = EPOS.CreateFromDocument(open(f).read())
        for person in baseline.Person:
            #print(person.fn)
            pass
        
        for organisation in baseline.Organisation:
            #print(organisation.fn)
            pass
        
        for webService in baseline.WebService:
            #print(webService.title.value() + webService.description.value())
            pass
    except:
        print(str(f) + ' has error');
    return

def visitor(arg, dirname, names):
    for name in names:
        if name.endswith('.xml'):
            handleFile(os.path.join(dirname, name))
    return 
       
os.path.walk(os.path.realpath('../../../examples'), visitor, None);


An python library to read Baseline from XML files.
This library should be used by TCSs to read baseline from XML files if they use python as development language.

Example

from libxml import baseline as EPOS;
baseline = EPOS.CreateFromDocument(open(file).read())
for person in baseline.Person:
    print(person.fn)

for organisation in baseline.Organisation:
    print(organisation.fn)

for webService in baseline.WebService:
    print(webService.title.value() + webService.description.value())

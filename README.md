## ++HOW TO CONTRIBUTE to this project++
You have to fork it to your personal repo, work on it, push on your personal repo, and make a pull request. 
See description down below in "How to contribute" section.

## Contact
Rossana Paciello rossana.paciello@ingv.it

# EPOS-DCAT-AP
DCAT-AP extension for Solid Earth Data, developed in the context of European Plate Observing System (EPOS) project www.epos-ip.org

## Why this extension
As other types of DCAT-AP extension, this one adds specializations to DCAT-AP entities, attributes and relations among attributes, in the specific context of Environmental Sciences -> Solid Earth Sciences.

In particular, this adds details to map from native formats that include the following concepts:
- Persons (and roles)
- Institutions
- Facilities and equipment
- Web services
- Software 

## How it is being used in the context of EPOS
EPOS is building a system, called Integrated Core Services (ICS) that integrates data, data products, services and softwares from the scientific communities in the field of Solid Earth Sciences.
ICS is a metadata-driven system, that uses the metadata to manage resources and respond properly to user queries (More info on ICS: http://www.sciencedirect.com/science/article/pii/S1877050914007923 and https://rd.springer.com/chapter/10.1007/978-3-319-13674-5_17).

**In order to enable the harmonization of metadata from the various communities in the Solid Earth Sciences, an extension of DCAT-AP is being used.**
All communities are therefore expected to map their metadata to this format.

### General description of mapping process for EPOS communities
It can be found here: http://wiki.epos-ip.org/index.php/TCS_Metadata_Mapping

## Structure of repository
- In the **schemas** folder all XML schema definition files can be found.
- In the **examples** folder a number of mapped metadta examples from EPOS communities can be found.

## Useful tools
.xsd Validator https://www.freeformatter.com/xml-validator-xsd.html

## HOW TO CONTRIBUTE
Go to https://github.com/epos-eu/EPOS-DCAT-AP

Step 1)
create a fork on your personal account by the "fork" button;

Step 2)
- browse into your forked project (at the top of the page you should read youraccount/EPOS-DCAT-AP forked from epos-eu/EPOS-DCAT-AP) and go to the directory in which you want to upload your file;
- click on "Upload files" button;
- drag your file into the graphic dashed square;
- do the commit, inserting properly title (es. add <MY NFO> xml dcat file);

Step 3)
move to the (second) tab ("pull requests") and click on "New pull request" button an then "Create Pull Request".
Insert a title for the request and finally confirm by clicking on "Create Pull Request".

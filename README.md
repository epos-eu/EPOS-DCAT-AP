## ++HOW TO CONTRIBUTE to this project++
You have to fork it to your personal repo, work on it, and make a pull request, as described here: https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/

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

##

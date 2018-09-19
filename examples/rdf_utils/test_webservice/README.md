Introduction
------------

The EPOS web service metadata is written in RDF using the Turtle langauge (https://www.w3.org/TR/turtle/) and includes fields that describe a template for a URL and a set of parameters. Together these metadata fields define how to construct URLs to call the web service. The  template and parameters comform to the HYDRA specification, a vocabulary for hypermedia-driven web APIs: https://www.hydra-cg.com/spec/latest/core/.

The code in this folder implements a basic operation checker for a web service described using EPOS web service metadata written in Turtle. It attempts to build a URL based on the HYDRA 'operation' (the URL template) using the **required** parameters and their **default values**, as described in the metadata. Having built the URL, this code calls the web service using the constructed URL, to check that the call returns valid data. The code can be used with a single metadata file or a directory containing several `.ttl` (Turtle) metadata files. If the call is successful it presents a summary of the data returned from the web service or, where the web service returns a zip archive, a list of the files in the zip file. It does not handle other binary formats.


THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.


Installation
------------

This code requires Python 3.6 (please see `Pipfile` for full requirements).
To install the code as described below will require a `git` command line client

From a shell (DOS prompt on Windows), create an empty folder and make it your current folder, then:
         
#### clone the Github repository:
```
git clone https://github.com/epos-eu/EPOS-DCAT-AP/ -b EPOS-DCAT-AP-shapes
```

#### make sure you have the latest version of pip:
```
python -m pip install --upgrade pip
```

#### use pip to install pipenv:
```
pip install pipenv
```

#### set up your envrionment for running the code:
```
cd EPOS-DCAT-AP/examples/rdf_utils/test_webservice
pipenv shell
```

#### use pipenv to install the dependencies for the code:
```
pipenv install
```

#### run the code to check WP13's metadata
```
python webservice.py ../../WP13
```

Example Output
--------------

Calling the checker on the W13 directory results in the following output:

```
$ python webservice.py ..\WP13\
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-001_INTERMAGNET.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://geomag.bgs.ac.uk/EPOS/WP13/intermagnet/?dataStartDate=2018-01-01&observatoryIagaCode=ESK&Request=GetData&pictureSize=640%2C480&dataScale=100+nT+%2F+10+minutes&colourTraces=True&dataDuration=1&recordTermination=Windows&publicationState=adj-or-rep&SamplesPerDay=Minute&pdfSize=640%2C480&traceList=1234
INFO:root:Status: 200
INFO:root:Content type: application/xml
INFO:root:Text:
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE GeomagneticTimeSeriesData SYSTEM "http://www.geomag.bgs.ac.uk/workshop/GeomagneticTimeSeriesData.dtd">
<!--
Document   : ESK20180101.xml
Created on : 2018/09/13
Author     : Edinburgh INTERMAGNET GIN
Description: Geomagnetic minute mean data
Comments   : This data file was created using INTERMAGNET data
             from the Edinburgh GIN. These data were acquired
             from an INTERMAGNET quasi-def data file.
             Final data will ...
...
....80078125</Z><S>49735.80078125</S></Sample>
  <Sample><H>17566.099609375</H><D>-2.103166707356771</D><Z>46530.69921875</Z><S>49736.1015625</S></Sample>
  <Sample><H>17566.69921875</H><D>-2.105500030517578</D><Z>46530.5</Z><S>49736.1015625</S></Sample>
  <Sample><H>17566.900390625</H><D>-2.1051666259765627</D><Z>46530.3984375</Z><S>49736.1015625</S></Sample>
  <Sample><H>17567.099609375</H><D>-2.106166712443034</D><Z>46530.30078125</Z><S>49736.0</S></Sample>
 </Data>
</GeomagneticTimeSeriesData>

INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-001_WDC.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://app.geomag.bgs.ac.uk/wdc/datasets/hour/ESK2016?media=xml
INFO:root:Status: 200
INFO:root:Content type: application/xml
INFO:root:Text:
<dataset>
  <metadata>
    <station_iaga_code>ESK</station_iaga_code>
    <dataset_cadence>HOUR</dataset_cadence>
  </metadata>
  <time-series cadence="PT1H">
    <data-point time="2016-01-01T00:30:00.000Z" X="17454.00" Y="-677.00" Z="46472.00" F="49646.00"/>
    <data-point time="2016-01-01T01:30:00.000Z" X="17470.00" Y="-704.00" Z="46439.00" F="49621.00"/>
    <data-point time="2016-01-01T02:30:00.000Z" X="17505.00" Y="-701.00" Z="46416.00" F="49612.00"/>
    <data-point time="2016-01-01T03:30...
...
...T19:30:00.000Z" X="17516.00" Y="-701.00" Z="46525.00" F="49718.00"/>
    <data-point time="2016-12-31T20:30:00.000Z" X="17518.00" Y="-696.00" Z="46526.00" F="49720.00"/>
    <data-point time="2016-12-31T21:30:00.000Z" X="17532.00" Y="-694.00" Z="46518.00" F="49717.00"/>
    <data-point time="2016-12-31T22:30:00.000Z" X="17539.00" Y="-699.00" Z="46508.00" F="49710.00"/>
    <data-point time="2016-12-31T23:30:00.000Z" X="17537.00" Y="-708.00" Z="46503.00" F="49705.00"/>
  </time-series>
</dataset>
INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-002.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://space.fmi.fi/cgi-bin/imagecgi/image-epos.cgi?start=19821001&institute=EPOS+Test+Institute&email=EPOSTestUser%40example.org&submit=OK&yourname=EPOS+Test+User
INFO:root:Status: 200
INFO:root:Content type: text/html; charset=ISO-8859-1
INFO:root:Text:
YYYY MM DD HH MM SS     MUO X   MUO Y   MUO Z   PEL X   PEL Y   PEL Z
   0  0  0  0  0  0      68.03   23.56     0     66.80   24.27     0
----------------------------------------------------------------------
1982 10 01 00 00 00    11452.4   825.6 51309.0 12020.5   796.1 50635.3
1982 10 01 00 00 20    11450.4   827.6 51308.1 12019.5   797.1 50635.3
1982 10 01 00 00 40    11447.5   826.6 51309.0 12017.5   797.1 50634.4
1982 10 01 00 01 00    11447.5   825.6 51310.0 12017.5   796.1 50634.4
198...
...
....6
1982 10 01 23 57 40    11378.4   855.2 51399.7 11903.3   828.8 50701.5
1982 10 01 23 58 00    11385.2   853.3 51400.6 11905.3   827.8 50703.5
1982 10 01 23 58 20    11388.1   851.3 51401.6 11905.3   822.8 50703.5
1982 10 01 23 58 40    11390.0   848.3 51403.5 11902.3   815.9 50704.5
1982 10 01 23 59 00    11392.0   847.3 51405.5 11900.3   817.9 50706.4
1982 10 01 23 59 20    11392.0   843.4 51407.4 11896.4   815.0 50706.4
1982 10 01 23 59 40    11393.9   843.4 51408.3 11899.3   815.9 50706.4

INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-003.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://geomag.bgs.ac.uk/gifs/wdc/global-survey/data/?north-latitude=90.0&south-latitude=-90.0&add-source-information=False&format=json&east-longitude=180.0&west-longitude=-180.0&start-year=1980.0&end-year=1980.5
INFO:root:Status: 200
INFO:root:Content type: application/json
INFO:root:Text:
{"start=year": 1980.0, "end-year": 1980.5, "north-latitude": 90.0, "south-latitude": -90.0, "west-longitude": -180.0, "east-longitude": 180.0, "include-one-off": true, "include-aeromag": true, "include-marine-vector": true, "include-include-satellite": true, "include-marine-scalar": true, "include-include-repeat-station": true, "include-observatory": true, "add-source-information": false, "global-survey-data": []}
INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-006.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://geomag.bgs.ac.uk/EPOS/WP13/isgi/?StartTime=2000-01-01&EndTime=2001-01-01&index=aa
INFO:root:Status: 200
INFO:root:Content type: application/octet-stream
INFO:root:Binary data
INFO:root:Zipped files: ['aa_2000-01-01_2001-01-01_D.dat']
INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-007.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://geomag.bgs.ac.uk/EPOS/WP13/isgi/?StartTime=2000-01-01&index=SC&EndTime=2001-01-01
INFO:root:Status: 200
INFO:root:Content type: application/octet-stream
INFO:root:Binary data
INFO:root:Zipped files: ['SC_2000_D.dat', 'SC_2001_D.dat']
INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-008.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://space.fmi.fi/cgi-bin/imagecgi/image-epos-indicators.cgi?submit=OK&email=EPOSTestUser%40example.org&institute=EPOS+Test+Institute&start=19821001&yourname=EPOS+Test+User
INFO:root:Status: 200
INFO:root:Content type: text/html; charset=ISO-8859-1
INFO:root:Text:
% The following 2 stations are used in computation of IMAGE electrojet indicators:
% The next four lines contain: 1. Station ID's  2. Station contribution to IU (# of data points) 3. Station contribution to IL (# of data points) 4. Station X component baseline
%  MUO  PEL
% 2392 1928
% 1938 2382
% 115951 120946

% File created on 13-09-2018 19:49:38

% YY MM DD HO MI SE        IL      IU      IE
1982 10 01 00 00 00     -142.7   -74.1    68.6
1982 10 01 00 00 20     -144.7   -75.1    69.6
1982 10...
...
...20     -245.0  -203.1    41.9
1982 10 01 23 56 40     -236.2  -197.2    39.0
1982 10 01 23 57 00     -231.3  -197.2    34.1
1982 10 01 23 57 20     -222.6  -191.3    31.3
1982 10 01 23 57 40     -216.7  -191.3    25.4
1982 10 01 23 58 00     -209.9  -189.3    20.6
1982 10 01 23 58 20     -207.0  -189.3    17.7
1982 10 01 23 58 40     -205.1  -192.3    12.8
1982 10 01 23 59 00     -203.1  -194.3     8.8
1982 10 01 23 59 20     -203.1  -198.2     4.9
1982 10 01 23 59 40     -201.2  -195.3     5.9

INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-009.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://space.fmi.fi/cgi-bin/imagecgi/image-epos-electrojet-events.cgi?yourname=EPOS+Test+User&email=EPOSTestUser%40example.org&institute=EPOS+Test+Institute&submit=OK&start=19821001
INFO:root:Status: 200
INFO:root:Content type: text/html; charset=ISO-8859-1
INFO:root:Text:
% IMAGE magnetometer network: active sequences on 19821001
% IE threshold 100 nT
% year month day hour minute second IE
% time in UT, IE in nT
% 1-min averaged data used
% Stations used: MUO PEL
% IE is the IMAGE electrojet indicator defined as IE=IU-IL
% For each time step, IL(t) = min({X(t)})
% {X(t)} stands for the (geographic) north component of the magnetic field measured at the selected stations.
% In the same way, IU(t) = max({X(t)})
% File written on 13-Sep-2018 19:49:42

1982 10 01 00 5...
...
... 10 30  107.7
1982 10 01 22 27 30  121.1
1982 10 01 22 28 30  166.9
1982 10 01 22 29 30  192.9
1982 10 01 22 30 30  190.8
1982 10 01 22 31 30  169.4
1982 10 01 22 32 30  143.7
1982 10 01 22 33 30  119.3
1982 10 01 22 45 30  112.3
1982 10 01 22 47 30  140.3
1982 10 01 22 48 30  185.1
1982 10 01 22 49 30  172.8
1982 10 01 22 50 30  191.5
1982 10 01 22 51 30  192.4
1982 10 01 22 52 30  177.8
1982 10 01 22 53 30  238.2
1982 10 01 22 54 30  253.0
1982 10 01 22 55 30  215.5
1982 10 01 22 56 30  196.5

INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-012_IGRF.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://www.geomag.bgs.ac.uk/web_service/GMModels/igrf/12?format=xml&altitude=0&date=2015-01-01&latitude=0&longitude=0
INFO:root:Status: 200
INFO:root:Content type: application/xml
INFO:root:Text:
<?xml version="1.0" encoding="UTF-8"?>
<geomagnetic-field-model-result>
    <model revision="12">igrf</model>
    <date>2015-01-01</date>
    <coordinates>
        <latitude units="deg (north)">0</latitude>
        <longitude units="deg (east)">0</longitude>
        <altitude units="km">0.00</altitude>
    </coordinates>
    <field-value>
        <total-intensity units="nT">31864</total-intensity>
        <declination units="deg (east)">-5.440</declination>
        <inclination units="deg (down)...
...
...  <total-intensity units="nT/y">34.3</total-intensity>
        <declination units="arcmin/y (east)">8.3</declination>
        <inclination units="arcmin/y (down)">-8.3</inclination>
        <north-intensity units="nT/y">-2.0</north-intensity>
        <east-intensity units="nT/y">67.5</east-intensity>
        <vertical-intensity units="nT/y">-83.9</vertical-intensity>
        <horizontal-intensity units="nT/y">-8.4</horizontal-intensity>
    </secular-variation>
</geomagnetic-field-model-result>

INFO:root:==================================================
INFO:root:
Processing: ..\WP13\EPOS-DCAT-AP_WP13_DDSS-012_WMM.ttl
INFO:root:--------------------------------------------------
INFO:root:URL: http://www.geomag.bgs.ac.uk/web_service/GMModels/WMM/2015?format=xml&longitude=0&altitude=0&latitude=0&date=2015-01-01
INFO:root:Status: 200
INFO:root:Content type: application/xml
INFO:root:Text:
<?xml version="1.0" encoding="UTF-8"?>
<geomagnetic-field-model-result>
    <model revision="2015">wmm</model>
    <date>2015-01-01</date>
    <coordinates>
        <latitude units="deg (north)">0</latitude>
        <longitude units="deg (east)">0</longitude>
        <altitude units="km">0.00</altitude>
    </coordinates>
    <field-value>
        <total-intensity units="nT">31865</total-intensity>
        <declination units="deg (east)">-5.456</declination>
        <inclination units="deg (down...
...
...   <total-intensity units="nT/y">36.8</total-intensity>
        <declination units="arcmin/y (east)">7.4</declination>
        <inclination units="arcmin/y (down)">-7.4</inclination>
        <north-intensity units="nT/y">3.6</north-intensity>
        <east-intensity units="nT/y">59.9</east-intensity>
        <vertical-intensity units="nT/y">-77.8</vertical-intensity>
        <horizontal-intensity units="nT/y">-2.1</horizontal-intensity>
    </secular-variation>
</geomagnetic-field-model-result>

INFO:root:==================================================
```

An java library to read Baseline from XML files.
This library should be used by TCSs to read baseline from XML files if they use Java as development language.
Another library in Python should be provided soon.

Example
import org.epos_ip.xml.XMLReader;
import org.epos_ip.elements.Baseline;

XMLReader reader = new XMLReader();
Baseline baseline = reader.readXML(fileName);

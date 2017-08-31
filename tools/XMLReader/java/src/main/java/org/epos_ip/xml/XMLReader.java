package org.epos_ip.xml;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
import javax.xml.stream.XMLStreamWriter;

import org.epos_ip.elements.Baseline;

public class XMLReader {

	static public JAXBContext jaxbContext = initContext();

	static private JAXBContext initContext() {
		try {
			return JAXBContext.newInstance(Baseline.class);
		} catch (JAXBException e) {
			return null;
		}
	}

	public Baseline readXML(InputStreamReader infile) throws JAXBException {

		Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
		Object obj = unmarshaller.unmarshal(infile);
		if (obj instanceof Baseline) {
			return (Baseline) obj;
		}
		return null;
	}

	public Baseline readXML(String infile) throws JAXBException, FileNotFoundException {

		return readXML(new FileReader(infile));
	}

	public void writeXML(Baseline obj, XMLStreamWriter sw) throws JAXBException {
		Marshaller marshaller = jaxbContext.createMarshaller();
		marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
		marshaller.marshal(obj, sw);
	}
}

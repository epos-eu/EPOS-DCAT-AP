@javax.xml.bind.annotation.XmlSchema(namespace = "http://www.epos-ip.org/", xmlns = {
		@javax.xml.bind.annotation.XmlNs(prefix = "eposap", namespaceURI = "http://www.epos-ip.org/terms.html"),
		@javax.xml.bind.annotation.XmlNs(prefix = "dct", namespaceURI = "http://purl.org/dc/terms/"),
		@javax.xml.bind.annotation.XmlNs(prefix = "foaf", namespaceURI = "http://xmlns.com/foaf/0.1/"),
		@javax.xml.bind.annotation.XmlNs(prefix = "skos", namespaceURI = "http://www.w3.org/2004/02/skos/core#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "adms", namespaceURI = "http://www.w3.org/ns/adms#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "cnt", namespaceURI = "http://www.w3.org/2008/content#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "http", namespaceURI = "http://www.w3.org/2006/http#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "locn", namespaceURI = "http://www.w3.org/ns/locn#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "rdf", namespaceURI = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "skos", namespaceURI = "http://www.w3.org/2004/02/skos/core#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "vcard", namespaceURI = "http://www.w3.org/2006/vcard/ns#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "xml", namespaceURI = "http://www.w3.org/XML/1998/namespace"),
		@javax.xml.bind.annotation.XmlNs(prefix = "xsi", namespaceURI = "http://www.w3.org/2001/XMLSchema-instance"),
		@javax.xml.bind.annotation.XmlNs(prefix = "dcat", namespaceURI = "http://www.w3.org/ns/dcat#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "owl", namespaceURI = "http://www.w3.org/2002/07/owl#"),
		@javax.xml.bind.annotation.XmlNs(prefix = "schema", namespaceURI = "http://schema.org/")

}, elementFormDefault = javax.xml.bind.annotation.XmlNsForm.QUALIFIED)

@XmlJavaTypeAdapter(value = StringTrimXmlAdapter.class, type = String.class)
package org.epos_ip.elements;

import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;

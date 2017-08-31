package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.datatype.XMLGregorianCalendar;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class CatalogRecord {

	@XmlPath("foaf:primaryTopic/text()")
	private String primarytopic;

	@XmlPath("dct:modified/text()")
	private XMLGregorianCalendar modified;

	@XmlPath("dct:language/dct:LinguisticSystem/text()")
	private List<String> language;

	@XmlPath("dct:title/text()")
	private List<String> title;

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("owl:versioninfo/text()")
	private String versioninfo;

	@XmlPath("cnt:characterEncoding/text()")
	private List<String> characterset;

	@XmlPath("dcat:contactPoint/text()")
	private List<String> contact;

	@XmlPath("cnt:created/text()")
	private XMLGregorianCalendar created;

	public String getPrimarytopic() {
		return primarytopic;
	}

	public void setPrimarytopic(String primarytopic) {
		this.primarytopic = primarytopic;
	}

	public XMLGregorianCalendar getModified() {
		return modified;
	}

	public void setModified(XMLGregorianCalendar modified) {
		this.modified = modified;
	}

	public List<String> getLanguage() {
		return language;
	}

	public void setLanguage(List<String> language) {
		this.language = language;
	}

	public List<String> getTitle() {
		return title;
	}

	public void setTitle(List<String> title) {
		this.title = title;
	}

	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public String getVersioninfo() {
		return versioninfo;
	}

	public void setVersioninfo(String versioninfo) {
		this.versioninfo = versioninfo;
	}

	public List<String> getCharacterset() {
		return characterset;
	}

	public void setCharacterset(List<String> characterset) {
		this.characterset = characterset;
	}

	public List<String> getContact() {
		return contact;
	}

	public void setContact(List<String> contact) {
		this.contact = contact;
	}

	public XMLGregorianCalendar getCreated() {
		return created;
	}

	public void setCreated(XMLGregorianCalendar created) {
		this.created = created;
	}

}

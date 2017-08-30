package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Facility {

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("dct:title/text()")
	private String name;

	@XmlPath("vcard:hasAddress/vcard:Address")
	private Address address;

	@XmlPath("dct:description/text()")
	private String description;

	@XmlPath("eposap:owner/text()")
	private String owner;

	@XmlPath("dcat:contactPoint/text()")
	private String contact;

	@XmlPath("eposap:facilityManager/text()")
	private String manager;

	@XmlPath("dct:type/text()")
	private List<String> type;

	@XmlPath("foaf:page/foaf:primaryTopic/text()")
	private String webaddress;

	@XmlPath("dcat:theme/text()")
	private List<String> sciencedomain;

	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getOwner() {
		return owner;
	}

	public void setOwner(String owner) {
		this.owner = owner;
	}

	public String getContact() {
		return contact;
	}

	public void setContact(String contact) {
		this.contact = contact;
	}

	public String getManager() {
		return manager;
	}

	public void setManager(String manager) {
		this.manager = manager;
	}

	public List<String> getType() {
		return type;
	}

	public void setType(List<String> type) {
		this.type = type;
	}

	public String getWebaddress() {
		return webaddress;
	}

	public void setWebaddress(String webaddress) {
		this.webaddress = webaddress;
	}

	public List<String> getSciencedomain() {
		return sciencedomain;
	}

	public void setSciencedomain(List<String> sciencedomain) {
		this.sciencedomain = sciencedomain;
	}

}

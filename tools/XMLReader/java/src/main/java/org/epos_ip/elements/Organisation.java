package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Organisation {

	@XmlPath("vcard:fn/text()")
	private String name_en;

	@XmlPath("vcard:organization-name/text()")
	private String name_native;

	@XmlPath("vcard:hasAddress/vcard:Address")
	private Address address;

	@XmlPath("vcard:hasEmail/text()")
	private String email;

	@XmlPath("vcard:hasURL/text()")
	private List<String> website;

	@XmlPath("vcard:hasTelephone/text()")
	private List<String> phone;
	
	@XmlPath("vcard:hasLogo/text()")
	private String logo;

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("eposap:scientificContact/text()")
	private String scientificcontact;

	@XmlPath("dct:spatial/dct:Location")
	private Location location;

	@XmlPath("dct:type/text()")
	private String type;

	@XmlPath("eposap:legalContact/text()")
	private String legalcontact;

	@XmlPath("eposap:financialContact/text()")
	private String financialcontact;

	@XmlPath("eposap:isPartOf/text()")
	private List<String> parentorganisation;

	@XmlPath("eposap:associatedProjects/text()")
	private List<String> projects;

	public String getName_en() {
		return name_en;
	}

	public void setName_en(String name_en) {
		this.name_en = name_en;
	}

	public String getName_native() {
		return name_native;
	}

	public void setName_native(String name_native) {
		this.name_native = name_native;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public List<String> getWebsite() {
		return website;
	}

	public void setWebsite(List<String> website) {
		this.website = website;
	}

	public String getLogo() {
		return logo;
	}

	public void setLogo(String logo) {
		this.logo = logo;
	}

	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public String getScientificcontact() {
		return scientificcontact;
	}

	public void setScientificcontact(String scientificcontact) {
		this.scientificcontact = scientificcontact;
	}

	public Location getLocation() {
		return location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getLegalcontact() {
		return legalcontact;
	}

	public void setLegalcontact(String legalcontact) {
		this.legalcontact = legalcontact;
	}

	public String getFinancialcontact() {
		return financialcontact;
	}

	public void setFinancialcontact(String financialcontact) {
		this.financialcontact = financialcontact;
	}

	public List<String> getParentorganisation() {
		return parentorganisation;
	}

	public void setParentorganisation(List<String> parentorganisation) {
		this.parentorganisation = parentorganisation;
	}

	public List<String> getProjects() {
		return projects;
	}

	public void setProjects(List<String> projects) {
		this.projects = projects;
	}

	public List<String> getPhone() {
		return phone;
	}

	public void setPhone(List<String> phone) {
		this.phone = phone;
	}

}

package org.epos_ip.elements;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Person {

	@XmlPath("vcard:fn/text()")
	private String name;

	@XmlPath("vcard:hasAddress/vcard:Address")
	private Address address;

	@XmlPath("vcard:hasEmail/text()")
	private String email;

	@XmlPath("vcard:hasTelephone/text()")
	private String phone;

	@XmlPath("dct:identifier/text()")
	private String identifier;
	
	@XmlPath("eposap:affiliation/text()")
	private String affiliation;

	@XmlPath("dct:language/dct:LinguisticSystem/text()")
	private String language;

	@XmlPath("schema:qualifications/text()")
	private String qualification;

	// cv should be binary
	@XmlPath("vcard:hasURL/text()")
	private String cv;

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

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(String language) {
		this.language = language;
	}

	public String getQualification() {
		return qualification;
	}

	public void setQualification(String qualification) {
		this.qualification = qualification;
	}

	public String getCv() {
		return cv;
	}

	public void setCv(String cv) {
		this.cv = cv;
	}

	public String getAffiliation() {
		return affiliation;
	}

	public void setAffiliation(String affiliation) {
		this.affiliation = affiliation;
	}

}

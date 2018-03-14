package org.epos_ip.elements;

import java.util.ArrayList;
import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlRootElement;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlRootElement(name = "Epos", namespace = "http://www.epos-ip.org/terms.html")
@XmlAccessorType(XmlAccessType.FIELD)
public class Baseline {

	@XmlPath("eposap:Catalog")
	private List<Catalog> catalogs;

	@XmlPath("eposap:Person")
	private List<Person> persons;

	@XmlPath("eposap:Organisation")
	private List<Organisation> organisations;

	@XmlPath("eposap:Project")
	private List<Project> projects;

	@XmlPath("eposap:WebService")
	private List<Webservice> webservices;

	@XmlPath("eposap:Publication")
	private List<Publication> publications;

	@XmlPath("eposap:Service")
	private List<Service> services;

	@XmlPath("eposap:Equipment")
	private List<Equipment> equipments;

	@XmlPath("eposap:Facility")
	private List<Facility> facilities;

	public List<Webservice> getWebservices() {
		return webservices;
	}

	public List<Catalog> getCatalogs() {
		if (catalogs == null)
			return new ArrayList<Catalog>();
		return catalogs;
	}

	public void setCatalogs(List<Catalog> catalogs) {
		this.catalogs = catalogs;
	}

	public List<Person> getPersons() {
		return persons;
	}

	public void setPersons(List<Person> persons) {
		this.persons = persons;
	}

	public List<Organisation> getOrganisations() {
		return organisations;
	}

	public void setOrganisations(List<Organisation> organisations) {
		this.organisations = organisations;
	}

	public List<Project> getProjects() {
		return projects;
	}

	public void setProjects(List<Project> projects) {
		this.projects = projects;
	}

	public List<Publication> getPublications() {
		return publications;
	}

	public void setPublications(List<Publication> publications) {
		this.publications = publications;
	}

	public List<Service> getServices() {
		return services;
	}

	public void setServices(List<Service> services) {
		this.services = services;
	}

	public List<Equipment> getEquipments() {
		return equipments;
	}

	public void setEquipments(List<Equipment> equipments) {
		this.equipments = equipments;
	}

	public List<Facility> getFacilities() {
		return facilities;
	}

	public void setFacilities(List<Facility> facilities) {
		this.facilities = facilities;
	}

	public void setWebservices(List<Webservice> webservices) {
		this.webservices = webservices;
	}

}

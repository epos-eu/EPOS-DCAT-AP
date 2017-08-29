package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.datatype.XMLGregorianCalendar;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Dataset {

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("dct:title/text()")
	private List<String> title;

	@XmlPath("dct:description/text()")
	private List<String> description;

	@XmlPath("dct:issued/text()")
	private XMLGregorianCalendar issued;

	@XmlPath("dct:modified/text()")
	private XMLGregorianCalendar modified;

	@XmlPath("dct:language/dct:LinguisticSystem/text()")
	private List<String> language;

	@XmlPath("dct:provenance/dct:ProvenaceStatement/text()")
	private String lineage;

	@XmlPath("dct:type/text()")
	private String resourcetype;

	@XmlPath("dcat:keyword/text()")
	private String keyword;

	@XmlPath("dct:accessRights/dct:RightsStatement/text()")
	private String accesslimit;

	@XmlPath("dct:conformsTo/text()")
	private String spatialReferenceSystem;

	@XmlPath("dcat:landingPage/foaf:primaryTopic/text()")
	private String onlineresource;

	@XmlPath("dct:spatial/dct:Location")
	private Location location;

	@XmlPath("dct:temporal")
	private TimePeriod timeperiod;

	@XmlPath("eposap:distribution/dcat:Distribution")
	private DatasetDistribution distribution;

	@XmlPath("eposap:domain/text()")
	private String domain;
	
	@XmlPath("eposap:subDomain/text()")
	private String subDomain;
	
	@XmlPath("dct:created/text()")
	private XMLGregorianCalendar created;

	@XmlPath("dct:subject/text()")
	private List<String> subject;

	@XmlPath("cnt:characterEncoding/text()")
	private String characterset;

	@XmlPath("dcat:contactPoint/text()")
	private List<String> contact;

	@XmlPath("eposap:responsibleParty/text()")
	private List<String> responsibleparty;

	@XmlPath("rdf:comment/text()")
	private String spatialresolution;

	@XmlPath("adms:representationTechnique/text()")
	private String spatialrepresentation;

	@XmlPath("eposap:providedBy/text()")
	private String providedBy;
	
	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public List<String> getTitle() {
		return title;
	}

	public void setTitle(List<String> title) {
		this.title = title;
	}

	public List<String> getDescription() {
		return description;
	}

	public void setDescription(List<String> description) {
		this.description = description;
	}

	public XMLGregorianCalendar getIssued() {
		return issued;
	}

	public void setIssued(XMLGregorianCalendar issued) {
		this.issued = issued;
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

	public String getLineage() {
		return lineage;
	}

	public void setLineage(String provenance) {
		this.lineage = provenance;
	}

	public String getResourcetype() {
		return resourcetype;
	}

	public void setResourcetype(String resourcetype) {
		this.resourcetype = resourcetype;
	}

	public String getKeyword() {
		return keyword;
	}

	public void setKeyword(String keyword) {
		this.keyword = keyword;
	}

	public String getAccesslimit() {
		return accesslimit;
	}

	public void setAccesslimit(String accesslimit) {
		this.accesslimit = accesslimit;
	}

	public String getSpatialReferenceSystem() {
		return spatialReferenceSystem;
	}

	public void setSpatialReferenceSystem(String spatialReferenceSystem) {
		this.spatialReferenceSystem = spatialReferenceSystem;
	}

	public String getOnlineresource() {
		return onlineresource;
	}

	public void setOnlineresource(String onlineresource) {
		this.onlineresource = onlineresource;
	}

	public Location getSpatialextent() {
		return location;
	}

	public void setSpatialextent(Location location) {
		this.location = location;
	}

	public TimePeriod getTemporalextent() {
		return timeperiod;
	}

	public void setTemporalextent(TimePeriod timeperiod) {
		this.timeperiod= timeperiod ;
	}

	public DatasetDistribution getDistribution() {
		return distribution;
	}

	public void setDistribution(DatasetDistribution distribution) {
		this.distribution = distribution;
	}

	public XMLGregorianCalendar getCreated() {
		return created;
	}

	public void setCreated(XMLGregorianCalendar created) {
		this.created = created;
	}

	public List<String> getSubject() {
		return subject;
	}

	public void setSubject(List<String> subject) {
		this.subject = subject;
	}

	public String getCharacterset() {
		return characterset;
	}

	public void setCharacterset(String characterset) {
		this.characterset = characterset;
	}

	public List<String> getContact() {
		return contact;
	}

	public void setContact(List<String> contact) {
		this.contact = contact;
	}

	public List<String> getResponsibleparty() {
		return responsibleparty;
	}

	public void setResponsibleparty(List<String> responsibleparty) {
		this.responsibleparty = responsibleparty;
	}

	public String getSpatialrepresentation() {
		return spatialrepresentation;
	}

	public void setSpatialrepresentation(String spatialrepresentation) {
		this.spatialrepresentation = spatialrepresentation;
	}

	public Location getLocation() {
		return location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}

	public TimePeriod getTimeperiod() {
		return timeperiod;
	}

	public void setTimeperiod(TimePeriod timeperiod) {
		this.timeperiod = timeperiod;
	}

	public String getDomain() {
		return domain;
	}

	public void setDomain(String domain) {
		this.domain = domain;
	}

	public String getSubDomain() {
		return subDomain;
	}

	public void setSubDomain(String subDomain) {
		this.subDomain = subDomain;
	}

	public String getProvidedBy() {
		return providedBy;
	}

	public void setProvidedBy(String providedBy) {
		this.providedBy = providedBy;
	}

	public String getSpatialresolution() {
		return spatialresolution;
	}

	public void setSpatialresolution(String spatialresolution) {
		this.spatialresolution = spatialresolution;
	}

}

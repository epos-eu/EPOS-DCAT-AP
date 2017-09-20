package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.datatype.XMLGregorianCalendar;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Webservice {

	@XmlPath("dct:title/text()")
	private List<String> title;

	@XmlPath("dct:description/text()")
	private List<String> description;

	@XmlPath("dct:issued/text()")
	private XMLGregorianCalendar published;

	@XmlPath("dct:modified/text()")
	private XMLGregorianCalendar modified;

	@XmlPath("dct:license/text()")
	private List<String> license;

	@XmlPath("foaf:page/foaf:primaryTopic/text()")
	private String URI;

	@XmlPath("dct:format/dct:MediaTypeOrExtent/text()")
	private String format;

	@XmlPath("dct:rights/dct:RightsStatement/text()")
	private List<String> accesslimit;

	@XmlPath("dct:conformsTo/text()")
	private String spatialReferenceSystem;

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("dct:created/text()")
	private XMLGregorianCalendar created;

	@XmlPath("eposap:domain/text()")
	private String domain;
	
	@XmlPath("eposap:subDomain/text()")
	private String subDomain;

	@XmlPath("dcat:keyword/text()")
	private List<String> keyword;

	@XmlPath("eposap:operation/text()")
	private String operation;
	
	@XmlPath("dct:hasVersion/text()")
	private String version;
	
	@XmlPath("eposap:parameter")
	private List<ServiceParameter> parameter;

	@XmlPath("schema:documentation/text()")
	private List<String> documentation;
	
	@XmlPath("dcat:contactPoint/text()")
	private List<String> contactpoint;

	@XmlPath("eposap:publisher/text()")
	private List<String> publisher;	
	
	@XmlPath("dct:spatial/dct:Location")
	private Location location;

	@XmlPath("adms:representationTechnique/text()")
	private String spatialrepresentation;

	@XmlPath("dct:temporal")
	private TimePeriod timeperiod;


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

	public XMLGregorianCalendar getPublished() {
		return published;
	}

	public void setPublished(XMLGregorianCalendar published) {
		this.published = published;
	}

	public XMLGregorianCalendar getModified() {
		return modified;
	}

	public void setModified(XMLGregorianCalendar modified) {
		this.modified = modified;
	}

	public List<String> getLicense() {
		return license;
	}

	public void setLicense(List<String> license) {
		this.license = license;
	}

	public String getURI() {
		return URI;
	}

	public void setURI(String uRI) {
		URI = uRI;
	}

	public String getFormat() {
		return format;
	}

	public void setFormat(String format) {
		this.format = format;
	}


	public List<String> getAccesslimit() {
		return accesslimit;
	}

	public void setAccesslimit(List<String> accesslimit) {
		this.accesslimit = accesslimit;
	}

	public String getSpatialReferenceSystem() {
		return spatialReferenceSystem;
	}

	public void setSpatialReferenceSystem(String spatialReferenceSystem) {
		this.spatialReferenceSystem = spatialReferenceSystem;
	}

	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public XMLGregorianCalendar getCreated() {
		return created;
	}

	public void setCreated(XMLGregorianCalendar created) {
		this.created = created;
	}

	public List<String> getKeyword() {
		return keyword;
	}

	public void setKeyword(List<String> keyword) {
		this.keyword = keyword;
	}

	public String getDomain() {
		return domain;
	}

	public void setDomain(String domain) {
		this.domain = domain;
	}

	public List<ServiceParameter> getParameter() {
		return parameter;
	}

	public void setParameter(List<ServiceParameter> parameter) {
		this.parameter = parameter;
	}

	public List<String> getContactpoint() {
		return contactpoint;
	}

	public void setContactpoint(List<String> contactpoint) {
		this.contactpoint = contactpoint;
	}

	public Location getSpatialextent() {
		return location;
	}

	public void setSpatialextent(Location location) {
		this.location = location;
	}

	public String getSpatialrepresentation() {
		return spatialrepresentation;
	}

	public void setSpatialrepresentation(String spatialrepresentation) {
		this.spatialrepresentation = spatialrepresentation;
	}

	public TimePeriod getTemporalextent() {
		return timeperiod;
	}

	public void setTemporalextent(TimePeriod timeperiod) {
		this.timeperiod = timeperiod;
	}

	public String getSubDomain() {
		return subDomain;
	}

	public void setSubDomain(String subDomain) {
		this.subDomain = subDomain;
	}

	public String getOperation() {
		return operation;
	}

	public void setOperation(String operation) {
		this.operation = operation;
	}

	public String getVersion() {
		return version;
	}

	public void setVersion(String version) {
		this.version = version;
	}

	public List<String> getDocumentation() {
		return documentation;
	}

	public void setDocumentation(List<String> documentation) {
		this.documentation = documentation;
	}

	public List<String> getPublisher() {
		return publisher;
	}

	public void setPublisher(List<String> publisher) {
		this.publisher = publisher;
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

}

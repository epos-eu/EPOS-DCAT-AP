package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Equipment {

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("schema:serialNumber/text()")
	private String serial;

	@XmlPath("dct:type/text()")
	private String type;

	@XmlPath("schema:numberOfItems/text()")
	private Integer count;
/*link to organisation*/
	@XmlPath("schema:manufacturer/text()")
	private String manufacturer;

	@XmlPath("dct:description/text()")
	private String description;

	@XmlPath("dct:title/text()")
	private String title;
/* link to facility*/
	@XmlPath("eposap:relatedTo/text()")
	private List<String> related;
/*link to equipment*/
	@XmlPath("eposap:isPartOf/text()")
	private List<String> partof;
/*link to person*/
	@XmlPath("dcat:contactPoint/text()")
	private String contactpoint;
/*link to organisation*/
	@XmlPath("eposap:owner/text()")
	private String owner;

	@XmlPath("dct:temporal")
	private TimePeriod timeperiod;

	@XmlPath("eposap:orientation/text()")
	private String orientation;

	@XmlPath("eposap:dynamicRange")
	private ValueAndUnit dynamicRange;

	@XmlPath("eposap:resolution/text()")
	private Double resolution;

	@XmlPath("eposap:samplePeriod")
	private ValueAndUnit samplePeriod;

	@XmlPath("eposap:filter/text()")
	private String filter;

	@XmlPath("dct:spatial/dct:Location")
	private Location location;

	public String getIdentifier() {
		return identifier;
	}

	public void setIdentifier(String identifier) {
		this.identifier = identifier;
	}

	public String getSerial() {
		return serial;
	}

	public void setSerial(String serial) {
		this.serial = serial;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public Integer getCount() {
		return count;
	}

	public void setCount(Integer count) {
		this.count = count;
	}

	public String getManufacturer() {
		return manufacturer;
	}

	public void setManufacturer(String manufacturer) {
		this.manufacturer = manufacturer;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public List<String> getRelated() {
		return related;
	}

	public void setRelated(List<String> related) {
		this.related = related;
	}

	public List<String> getPartof() {
		return partof;
	}

	public void setPartof(List<String> partof) {
		this.partof = partof;
	}

	public String getContactpoint() {
		return contactpoint;
	}

	public void setContactpoint(String contactpoint) {
		this.contactpoint = contactpoint;
	}

	public String getOwner() {
		return owner;
	}

	public void setOwner(String owner) {
		this.owner = owner;
	}

	public TimePeriod getTimeperiod() {
		return timeperiod;
	}

	public void setTimeperiod(TimePeriod timeperiod) {
		this.timeperiod = timeperiod;
	}

	public String getOrientation() {
		return orientation;
	}

	public void setOrientation(String orientation) {
		this.orientation = orientation;
	}

	public ValueAndUnit getDynamicRange() {
		return dynamicRange;
	}

	public void setDynamicRange(ValueAndUnit dynamicRange) {
		this.dynamicRange = dynamicRange;
	}

	public Double getResolution() {
		return resolution;
	}

	public void setResolution(Double resolution) {
		this.resolution = resolution;
	}

	public ValueAndUnit getSamplePeriod() {
		return samplePeriod;
	}

	public void setSamplePeriod(ValueAndUnit samplePeriod) {
		this.samplePeriod = samplePeriod;
	}

	public String getFilter() {
		return filter;
	}

	public void setFilter(String filter) {
		this.filter = filter;
	}

	public Location getLocation() {
		return location;
	}

	public void setLocation(Location location) {
		this.location = location;
	}

}

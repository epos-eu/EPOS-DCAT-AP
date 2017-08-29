package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class ServiceParameter {

	@XmlPath("http:paramName/text()")
	private String name;

	@XmlPath("rdf:label/text()")
	private String label;	
	
	@XmlPath("dct:type/text()")
	private String type;

	@XmlPath("http:paramValue/text()")
	private List<String> value;

	@XmlPath("schema:minValue/text()")
	private String minValue;
	
	@XmlPath("schema:maxValue/text()")
	private String maxValue;
	
	@XmlPath("owl:versionInfo/text()")
	private String version;
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<String> getValue() {
		return value;
	}

	public void setValue(List<String> value) {
		this.value = value;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getVersion() {
		return version;
	}

	public void setVersion(String version) {
		this.version = version;
	}

	public String getLabel() {
		return label;
	}

	public void setLabel(String label) {
		this.label = label;
	}

	public String getMinValue() {
		return minValue;
	}

	public void setMinValue(String minValue) {
		this.minValue = minValue;
	}

	public String getMaxValue() {
		return maxValue;
	}

	public void setMaxValue(String maxValue) {
		this.maxValue = maxValue;
	}

}

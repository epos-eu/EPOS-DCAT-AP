package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Catalog {

	@XmlPath("dct:title/text()")
	private String title;

	@XmlPath("dct:description/text()")
	private String description;

	@XmlPath("dct:publisher/foaf:name/text()")
	private String publisher;

	@XmlPath("eposap:Dataset")
	private List<Dataset> dataset;

	@XmlPath("eposap:CatalogRecord")
	private CatalogRecord catalogrecord;

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getPublisher() {
		return publisher;
	}

	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}

	public List<Dataset> getDatasets() {
		return dataset;
	}

	public void setDatasets(List<Dataset> dataset) {
		this.dataset = dataset;
	}

	public CatalogRecord getCatalogrecord() {
		return catalogrecord;
	}

	public void setCatalogrecord(CatalogRecord catalogrecord) {
		this.catalogrecord = catalogrecord;
	}

}

package org.epos_ip.elements;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.datatype.XMLGregorianCalendar;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class Publication {

	@XmlPath("dct:identifier/text()")
	private String identifier;

	@XmlPath("dct:title/text()")
	private List<String> title;

	@XmlPath("eposap:authors/text()")
	private List<String> authors;

	// dct?
	@XmlPath("eposap:publisher/text()")
	private String publisher;

	// dct:description
	@XmlPath("dct:abstract/text()")
	private List<String> description;

	@XmlPath("dct:issued/text()")
	private XMLGregorianCalendar issued;

	@XmlPath("schema:issn/text()")
	private String issn;

	@XmlPath("schema:issueNumber/text()")
	private String issueNumber;

	@XmlPath("schema:volumeNumber/text()")
	private String volumeNumber;

	@XmlPath("schema:numberOfPages/text()")
	private String numberOfPages;

	@XmlPath("schema:keywords/text()")
	private String keywords;

	@XmlPath("eposap:contributors/text()")
	private List<String> contributors;

	@XmlPath("dct:accessRights/dct:RightsStatement/text()")
	private List<String> accesslimit;

	@XmlPath("dct:format/dct:MediaTypeOrExtent/text()")
	private List<String> format;

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

	public List<String> getAuthors() {
		return authors;
	}

	public void setAuthors(List<String> authors) {
		this.authors = authors;
	}

	public String getPublisher() {
		return publisher;
	}

	public void setPublisher(String publisher) {
		this.publisher = publisher;
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

	public String getIssn() {
		return issn;
	}

	public void setIssn(String issn) {
		this.issn = issn;
	}

	public String getIssueNumber() {
		return issueNumber;
	}

	public void setIssueNumber(String issueNumber) {
		this.issueNumber = issueNumber;
	}

	public String getVolumeNumber() {
		return volumeNumber;
	}

	public void setVolumeNumber(String volumeNumber) {
		this.volumeNumber = volumeNumber;
	}

	public String getNumberOfPages() {
		return numberOfPages;
	}

	public void setNumberOfPages(String numberOfPages) {
		this.numberOfPages = numberOfPages;
	}

	public String getKeywords() {
		return keywords;
	}

	public void setKeywords(String keywords) {
		this.keywords = keywords;
	}

	public List<String> getContributors() {
		return contributors;
	}

	public void setContributors(List<String> contributors) {
		this.contributors = contributors;
	}

	public List<String> getAccesslimit() {
		return accesslimit;
	}

	public void setAccesslimit(List<String> accesslimit) {
		this.accesslimit = accesslimit;
	}

	public List<String> getFormat() {
		return format;
	}

	public void setFormat(List<String> format) {
		this.format = format;
	}

}

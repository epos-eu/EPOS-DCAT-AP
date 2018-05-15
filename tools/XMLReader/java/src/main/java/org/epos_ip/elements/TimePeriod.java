package org.epos_ip.elements;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.datatype.XMLGregorianCalendar;

import org.eclipse.persistence.oxm.annotations.XmlPath;

@XmlAccessorType(XmlAccessType.FIELD)
public class TimePeriod {

	@XmlPath("dct:PeriodOfTime/schema:startDate/text()")
	private XMLGregorianCalendar start;

	@XmlPath("dct:PeriodOfTime/schema:endDate/text()")
	private XMLGregorianCalendar end;

	public XMLGregorianCalendar getStart() {
		return start;
	}

	public void setStart(XMLGregorianCalendar start) {
		this.start = start;
	}

	public XMLGregorianCalendar getEnd() {
		return end;
	}

	public void setEnd(XMLGregorianCalendar end) {
		this.end = end;
	}

}

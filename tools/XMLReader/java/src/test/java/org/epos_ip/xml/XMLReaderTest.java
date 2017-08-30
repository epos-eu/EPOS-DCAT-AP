package org.epos_ip.xml;

import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.ArrayList;
import java.util.List;

import junit.framework.Assert;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for XMLReader {@link org.epos_ip.xml.XMLReader}.
 */
public class XMLReaderTest extends TestCase {
	private static String LINEBREAK = String.format("%n");
	/**
	 * Create the test case
	 *
	 * @param testName
	 *            name of the test case
	 */
	public XMLReaderTest(String testName) {
		super(testName);
	}

	/**
	 * @return the suite of tests being tested
	 */
	public static Test suite() {
		return new TestSuite(XMLReaderTest.class);
	}

	/**
	 * Rigourous Test :-)
	 */
	public void testXMLReader() {
		final XMLReader reader = new XMLReader();
		final List<String> errorFiles = new ArrayList<String>();
		try {
			Files.walkFileTree(Paths.get("examples"), new SimpleFileVisitor<Path>() {
				@Override
				public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
					if (file.getFileName().toString().endsWith("xml")) {
						try {
							reader.readXML(file.toAbsolutePath().toString());
						} catch (Exception e) {
							errorFiles.add(file.toAbsolutePath().toString());
						}
					}
					return FileVisitResult.CONTINUE;
				}
			});

		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println(String.join(LINEBREAK, errorFiles));
		Assert.assertTrue(errorFiles.isEmpty());
	}
}

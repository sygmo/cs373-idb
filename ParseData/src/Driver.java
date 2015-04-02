import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Driver extends WriteToJson {

    public static void main(String[] args) {
        //extractConstellationsUsingJsoup("http://en.wikipedia.org/wiki/88_modern_constellations","wikitable");
        //extractStarsUsingJsoup("http://en.wikipedia.org/wiki/List_of_exoplanetary_host_stars");
    	extractPlanetsUsingJsoup("http://en.wikipedia.org/wiki/Planet");
    }
    
    // USE THIS INSTEAD: http://en.wikipedia.org/wiki/List_of_gravitationally_rounded_objects_of_the_Solar_System
    public static void extractPlanetsUsingJsoup(String url)
    {
    	Document doc;
    	try {
            // need http protocol
            doc = Jsoup.connect(url).get();
            
            // most planets -> eq(0)
            Elements nextTurns = doc.select("table[class=wikitable sortable] td:eq(0) a");
            ListIterator<Element> iter = nextTurns.listIterator();
            List<String> urls = new ArrayList<String>();
            while(iter.hasNext()) 
    	    {
        		Element e = (Element) iter.next();
        		String s = e.attr("abs:href");
        		if(e.hasAttr("title")) {
        			urls.add(s);
        		}
    	    }
            // Mercury and Uranus -> eq(1)
            nextTurns = doc.select("table[class=wikitable sortable] td:eq(1) a");
            iter = nextTurns.listIterator();
            while(iter.hasNext()) 
    	    {
        		Element e = (Element) iter.next();
        		String s = e.attr("abs:href");
        		if(e.hasAttr("title")) {
        			urls.add(s);
        		}
    	    }
            // Jupiter -> eq(2)
            nextTurns = doc.select("table[class=wikitable sortable] td:eq(2) a");
            iter = nextTurns.listIterator();
            while(iter.hasNext()) 
    	    {
        		Element e = (Element) iter.next();
        		String s = e.attr("abs:href");
        		if(e.hasAttr("title")) {
        			urls.add(s);
        		}
    	    }
            for(String planet : urls)
            {
            	System.out.print("db.session.add(planet(");
            	doc = Jsoup.connect(planet).get();
            	Elements n = doc.select("table.infobox caption");
            	for(Element e : n)
            	{
            		System.out.print("name = \"" + e.text() + "\"");
            	}
            	n = doc.select("table.infobox tr");
            	int has_mass = 0;
            	for(Element e : n)
            	{
            		if(e.text().contains("Mass"))
            		{
            			String[] number = e.text().split("Mass ");
            			System.out.print(", mass = " + number[number.length-1]);
            		}
            		// distance from the sun (perihelion is closest to the sun)
            		if(e.text().contains("Perihelion"))
            		{
            			String[] number = e.text().split("Perihelion ");
            			System.out.print(", distance_from_sun = " + number[number.length-1]);
            		}
            		if(e.text().contains("Orbital period"))
            		{
            			String[] number = e.text().split("Orbital period ");
            			System.out.print(", orbital_period = " + number[number.length-1]);
            		}
            		// length of day = rotation period
            		if(e.text().contains("Sidereal"))
            		{
            			String[] number = e.text().split("Sidereal rotation period ");
            			System.out.print(", length_of_day = " + number[number.length-1]);
            		}
            		// surface temperature
            		if(e.text().contains("Surface temp"))
            		{
            			String[] number = e.text().split("Surface temp. min mean max ");
            			System.out.print(", surface_temperature = " + number[number.length-1]);
            		}
            		// volume
            		if(e.text().contains("Volume"))
            		{
            			String[] number = e.text().split("Volume ");
            			System.out.print(", volume = " + number[number.length-1]);
            		}
            		// radius 
            		if(e.text().contains("Mean radius"))
            		{
            			String[] number = e.text().split("Mean radius ");
            			System.out.print(", radius = " + number[number.length-1]);
            		}
            		// density
            		if(e.text().contains("Mean density"))
            		{
            			String[] number = e.text().split("Mean density ");
            			System.out.print(", density = " + number[number.length-1]);
            		}
            		// surface area
            		if(e.text().contains("Surface area"))
            		{
            			String[] number = e.text().split("Surface area ");
            			System.out.print(", surface_area = " + number[number.length-1]);
            		}
            		// semi major axis
            		if(e.text().contains("Semi-major axis"))
            		{
            			String[] number = e.text().split("Semi-major axis ");
            			System.out.print(", semi_major_axis = " + number[number.length-1]);
            		}
            		// gravity
            		if(e.text().contains("Surface gravity"))
            		{
            			String[] number = e.text().split("Surface gravity ");
            			System.out.print(", gravity = " + number[number.length-1]);
            		}
            		// composition
            		if(e.text().contains("Composition by volume"))
            		{
            			String[] number = e.text().split("Composition by volume ");
            			System.out.print(", composition = " + number[number.length-1]);
            		}
            		// number of moons
            		if(e.text().contains("Known satellites"))
            		{
            			String[] number = e.text().split("Known satellites ");
            			System.out.print(", moons = " + number[number.length-1]);
            		}
            	}
            	System.out.print(", history = " + "None");
            	System.out.print(", photo_link = " + "None");
            	System.out.print(", photo = " + "None");
            	System.out.println(", fk_star_planet = " + "Sun");
            	System.out.println("))");
            }
    	} catch (IOException e) {
                e.printStackTrace();
                }
    }
    
    
    public static void extractStarsUsingJsoup(String url)
    {
    	try {
    		Document doc = Jsoup.connect(url).get();
            
            Elements nextTurns = doc.select("table.toccolours td:eq(0) a");
            ListIterator<Element> iter = nextTurns.listIterator();
            List<String> urls = new ArrayList<String>();
            while(iter.hasNext()) 
    	    {
        		Element e = (Element) iter.next();
        		String s = e.attr("abs:href");
        		if(!s.contains("redlink"))
        		{
        			urls.add(s);
        		}
    	    }
    		for(String star : urls)
    		{
        		StringBuilder py_stars = new StringBuilder();
    			// name
    			py_stars.append("db.session.add(star(");
            	doc = Jsoup.connect(star).get();
            	Elements n = doc.select("table.infobox caption");
            	boolean save_star = true;
            	for(Element e : n)
            	{
            		py_stars.append("name = \"" + e.text() + "\"");
            	}
    	    	// mass
            	n = doc.select("table.infobox tr");
            	int has_mass = 0;
            	for(Element e : n)
            	{
            		if(e.text().contains("Mass"))
            		{
            			String[] number = e.text().split("Mass ");
            			if(number[number.length-1].contains("±"))
            			{
            				number[number.length-1] = number[number.length-1].substring(0, number[number.length-1].indexOf("±")-1);
            			}
            			py_stars.append(", mass = " + number[number.length-1]);
            			has_mass++;
            		}
            	}
            	if(has_mass == 1)
            	{
            		// TODO: mass is not on star page; check main table
            		save_star = false;
            	}
    	    	// radius
    	    	// spectral_type
    	    	// temperature
    	    	// luminosity
    	    	// stellar_distance
    	    	// planentary_systems
    	    	// fk_constellation_star
    	    	// history
    	    	// photo_link
    	    	// photo
            	if(save_star)
            	{
            		System.out.println(py_stars.toString());
            	}
    		}
    	}
    	catch (IOException e) {
    		 
    	}
    }

    public static void extractConstellationsUsingJsoup(String url, String tableId){
        Document doc;
        try {
            // need http protocol
            doc = Jsoup.connect(url).get();
            
            Elements nextTurns = doc.select("table.wikitable td:eq(0) a");
            ListIterator<Element> iter = nextTurns.listIterator();
            List<String> urls = new ArrayList<String>();
            while(iter.hasNext()) 
    	    {
        		Element e = (Element) iter.next();
        		String s = e.attr("abs:href");
        		if(!s.contains("#"))
        		{
        			urls.add(s);
        		}
    	    }
            for(String constellation : urls)
            {
            	System.out.print("db.session.add(constellation(");
            	doc = Jsoup.connect(constellation).get();
            	Elements n = doc.select("table.infobox caption");
            	for(Element e : n)
            	{
            		System.out.print("name = \"" + e.text() + "\"");
            	}
            	n = doc.select("table.infobox tr");
            	for(Element e : n)
            	{
            		if(e.text().contains("Stars with planets"))
            		{
            			String[] number = e.text().split("Stars with planets ");
            			System.out.print(", stars_with_planets = " + number[number.length-1]);
            		}
            	}
            	for(Element e : n)
            	{
            		if(e.text().contains("Symbolism"))
            		{
            			String[] number = e.text().split("Symbolism ");
            			if(number[number.length-1].contains("["))
            			{
            				number[number.length-1] = number[number.length-1].substring(0, number[number.length-1].indexOf("["));
            			}
            			System.out.print(", meaning = \"" + number[number.length-1] + "\"");
            		}
            	}
            	System.out.print(", history = " + "None");
            	System.out.print(", photo_link = " + "None");
            	System.out.print(", photo = " + "None");
            	for(Element e : n)
            	{
            		if(e.text().contains("Family"))
            		{
            			String[] number = e.text().split("Family ");
            			System.out.print(", fk_constellation_family = " + "None\"\"\"" + number[number.length-1] + "\"\"\"");
            		}
            	}
            	System.out.println("))");
            }
            /*//getFamilies(nextTurns);
            for (Element nextTurn : nextTurns) {
                System.out.println(nextTurn.text());
            }
            //Set id of any table from any website and the below code will print the contents of the table.
            //Set the extracted data in appropriate data structures and use them for further processing
            /*Elements table = doc.getElementsByClass(tableId);
            for (Element t : table) {
                Element item = t;
                String cadena = "";
                for (Element row : t.select("tr")) {
                    for (Element column : row.select("td")) {
                        // Elements tds = row.select("td");
                        // cadena += tds.get(0).text() + "->" +
                        // tds.get(1).text()
                        // + " \n";
                    	String temp = column.text();
                    	if(temp.contains("/"))
                    	{
                    		temp = temp.substring(0,temp.indexOf('/'));
                    	}
                        cadena += temp + ",";
                    }
                    cadena += "\n";
                }
                System.out.println(cadena);
            }
            System.out.println("finished");*/

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

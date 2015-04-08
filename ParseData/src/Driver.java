import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;
import java.util.regex.Matcher;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Driver extends WriteToJson {
	static Map<String, Integer> constellation_keys = new HashMap<String, Integer>();
	static Map<String, Integer> star_keys = new HashMap<String, Integer>();

    public static void main(String[] args) {
        extractConstellationsUsingJsoup("http://en.wikipedia.org/wiki/88_modern_constellations","wikitable");
        Map<String, String> exoPlanetLinks = extractStarsUsingJsoup("http://en.wikipedia.org/wiki/List_of_exoplanetary_host_stars");
        extractExoplanetsUsingJsoup(exoPlanetLinks);
    	Map<String, String> moons = extractPlanetsUsingJsoup("http://en.wikipedia.org/wiki/Planet");
    	extractMoonsUsingJsoup(moons);
    }
    
    public static void extractMoonsUsingJsoup(Map<String, String> moons)
    {
    	/*
    	 * name = db.Column(Text, nullable = False)
	radius = db.Column(Float)
	volume = db.Column(Float)
	mass = db.Column(Float)
	distance_from_planet = db.Column(Float)
	orbital_period = db.Column(Float)
	surface_gravity = db.Column(Float)
	history = db.Column(Text)
	photo_link = db.Column(Text)
	photo = db.Column(LargeBinary)
	fk_planet_moon = db.Column(Integer, ForeignKey("planet.id"))
    	 */
    	
    }
    
    // USE THIS INSTEAD: http://en.wikipedia.org/wiki/List_of_gravitationally_rounded_objects_of_the_Solar_System
    public static Map<String, String> extractPlanetsUsingJsoup(String url)
    {
    	Document doc;
        Map<String,String> moonPlanet = new HashMap<String,String>();
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
            	StringBuilder py_planets = new StringBuilder();
            	py_planets.append("db.session.add(planet(");
            	doc = Jsoup.connect(planet).get();
            	Elements n = doc.select("table.infobox caption");
            	String name = "";
            	for(Element e : n)
            	{
            		name = e.text();
            		py_planets.append("name = \"" + name + "\"");
            	}
            	n = doc.select("table.infobox tr");
            	doc.select("span[style*=display:none]").remove();
            	int has_mass = 0;
            	int moons = 0;
            	for(Element e : n)
            	{
            		//in AU
            		if(e.text().contains("Mass"))
            		{
            			if(!name.equals("Earth"))
            			{
            				String[] spl = e.text().split("kg");
            				String earths = spl[spl.length-1];
            				if(earths.charAt(0) == '[')
            				{
            					earths = earths.substring(3);
            				}
            				if(earths.charAt(0) == ' ')
            				{
            					earths = earths.substring(1);
            				}
            				int index = earths.length();
            				for(int i = 0; i < earths.length(); i++)
            				{
            					if(!(earths.charAt(i)+"").matches("[\\d\\.]"))
            					{
            						index = i;
            						i = earths.length();
            					}
            				}
            				earths = earths.substring(0, index);
            				py_planets.append(", mass = " + earths);
            			}
            			else
            			{
            				py_planets.append(", mass = " + 1);
            			}
            		}
            		// distance from the sun (perihelion is closest to the sun) in AU
            		if(e.text().contains("Perihelion"))
            		{
            			String changer = e.text();
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					if(!name.equals("Earth"))
            					{
            						py_planets.append(", distance_from_sun = " + number[i]);
            					}
            					else
            					{
            						py_planets.append(", distance_from_sun = " + 0.98329);
            					}
            					i = number.length;
            				}
            			}
            		}
            		// in Earth Years
            		if(e.text().contains("Orbital period"))
            		{
            			String changer = e.text();
            			String diff = changer.replaceAll("[^0-9\\.,]","_");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("_");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					if(name.equals("Mercury") || name.equals("Venus") || name.equals("Earth"))
            					{
            						double days = Double.parseDouble(number[i]);
            						number[i] = (days / (365.256363004)) + "";
            					}
            					py_planets.append(", orbital_period = " + number[i]);
            					i = number.length;
            				}
            			}
            		}
            		// length of day = rotation period
            		if(e.text().contains("Sidereal"))
            		{
            			String changer = e.text();
            			String[] check_neg = changer.split("Sidereal rotation period ");
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					if(check_neg[1].charAt(0) == 8722)
            					{
            						number[i] = "-" + number[i];
            					}
            					py_planets.append(", length_of_day = " + number[i]);
            					i = number.length;
            				}
            			}
            		}
            		// surface temperature (in K)
            		if(e.text().contains("Surface temp. min mean max "))
            		{
            			String temp = "";
            			if(name.equals("Mercury")) 
            			{
            				temp = "340";
            			}
            			if(name.equals("Venus")) 
            			{
            				temp = "737";
            			}
            			if(name.equals("Earth")) 
            			{
            				temp = "288";
            			}
            			if(name.equals("Mars")) 
            			{
            				temp = "210";
            			}
            			if(name.equals("Jupiter")) 
            			{
            				temp = "165";
            			}
            			if(name.equals("Saturn")) 
            			{
            				temp = "134";
            			}
            			if(name.equals("Uranus")) 
            			{
            				temp = "76";
            			}
            			if(name.equals("Neptune")) 
            			{
            				temp = "72";
            			}
            			py_planets.append(", surface_temperature = " + temp);
            		}
            		// volume (in AU)
            		if(e.text().contains("Volume"))
            		{
            			if(!name.equals("Earth"))
            			{
            				String[] spl = e.text().split("km3");
            				String earths = spl[spl.length-1];
            				while(earths.charAt(0) == '[')
            				{
            					earths = earths.substring(3);
            				}
            				if(earths.charAt(0) == ' ')
            				{
            					earths = earths.substring(1);
            				}
            				int index = earths.length();
            				for(int i = 0; i < earths.length(); i++)
            				{
            					if(!(earths.charAt(i)+"").matches("[\\d\\.]"))
            					{
            						index = i;
            						i = earths.length();
            					}
            				}
            				earths = earths.substring(0, index);
            				py_planets.append(", volume = " + earths);
            			}
            			else
            			{
            				py_planets.append(", volume = " + 1);
            			}
            		}
            		// radius in km
            		if(e.text().contains("Mean radius"))
            		{
            			String changer = e.text();
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_planets.append(", radius = " + number[i]);
            					i = number.length;
            				}
            			}
            		}
            		// density in g/cm^3
            		if(e.text().contains("Mean density"))
            		{
            			String changer = e.text();
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_planets.append(", density = " + number[i]);
            					i = number.length;
            				}
            			}
            		}
            		// surface area
            		if(e.text().contains("Surface area"))
            		{
            			if(!name.equals("Earth"))
            			{
            				String[] spl = e.text().split("km2");
            				String earths = spl[spl.length-1];
            				while(earths.charAt(0) == '[')
            				{
            					earths = earths.substring(3);
            				}
            				if(earths.charAt(0) == ' ')
            				{
            					earths = earths.substring(1);
            				}
            				int index = earths.length();
            				for(int i = 0; i < earths.length(); i++)
            				{
            					if(!(earths.charAt(i)+"").matches("[\\d\\.]"))
            					{
            						index = i;
            						i = earths.length();
            					}
            				}
            				earths = earths.substring(0, index);
            				py_planets.append(", surface_area = " + earths);
            			}
            			else
            			{
            				py_planets.append(", surface_area = " + 1);
            			}
            		}
            		// semi major axis in AU
            		if(e.text().contains("Semi-major axis"))
            		{
            			if(!name.equals("Earth"))
            			{
	            			String changer = e.text();
	            			String diff = changer.replaceAll("[^0-9\\.,]","A");
	            			diff = diff.replaceAll("[,]","");
	            			String[] number = diff.split("A");
	            			for(int i = 0; i < number.length; i++)
	            			{
	            				if(number[i].length() > 0)
	            				{
	            					py_planets.append(", semi_major_axis = " + number[i]);	            					i = number.length;
	            				}
	            			}
            			}
            			else
            			{
        					py_planets.append(", semi_major_axis = " + 1);
            			}
            		}
            		// gravity in m/s^2
            		if(e.text().contains("Surface gravity"))
            		{
            			String changer = e.text();
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_planets.append(", gravity = " + number[i]);
            					i = number.length;
            				}
            			}
            		}
            		// number of moons
            		if(e.text().contains("Known satellites"))
            		{
            			String[] number = e.text().split("Known satellites ");
            			if(number[number.length-1].contains(" "))
            			{
            				number[number.length-1] = number[number.length-1].substring(0, number[number.length-1].indexOf(' '));
            			}
            			py_planets.append(", moons = " + number[number.length-1]);
            			moons++;
            			moonPlanet.put("http://en.wikipedia.org/wiki/Moons_of_"+name, name);
            		}
            	}

        		if(moons == 0)
        		{
        			if(name.equals("Earth"))
        			{
        				moonPlanet.put("http://en.wikipedia.org/wiki/Moon", "Earth");
        				py_planets.append(", moons = " + 1);
        			}
        			else
        			{
        				py_planets.append(", moons = " + 0);
        			}
        		}
            	py_planets.append(", history = " + "None");
            	py_planets.append(", photo_link = " + "None");
            	py_planets.append(", photo = " + "None");
            	py_planets.append(", fk_star_planet = " + 1);
            	py_planets.append("))");
            	System.out.println(py_planets.toString());
            }
    	} catch (IOException e) {
                e.printStackTrace();
                }
    	return moonPlanet;
    }
    
    public static void extractExoplanetsUsingJsoup(Map<String,String> exoPlanetStar)
    {
    	Iterator it = exoPlanetStar.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            //System.out.println(pair.getKey() + " = " + pair.getValue());
            try {
				Document doc = Jsoup.connect((String)pair.getKey()).get();
				StringBuilder py_exoplanets = new StringBuilder();
    			// name
    			py_exoplanets.append("db.session.add(exoplanet(");
            	Elements n = doc.select("table.infobox caption");
            	String exoplanets_name = "";
            	boolean save_exoplanet = true;
            	if(n.size() == 0)
            	{
            		save_exoplanet = false;
            	}
            	for(Element e : n)
            	{
            		String[] name = e.text().split("\\[");
            		exoplanets_name = name[0];
            		if(exoplanets_name.endsWith(" ")) 
            		{
            			exoplanets_name = exoplanets_name.substring(0, exoplanets_name.length() - 1);
            		}
            		py_exoplanets.append("name = \"" + exoplanets_name + "\"");
            	}
            	//discovered
            	n = doc.select("table.infobox tr");
            	doc.select("span[style*=display:none]").remove();
            	for(Element e : n)
            	{
            		if(e.text().contains("Discovery date"))
            		{
            			String[] discovery = e.text().split(" "); 
            			if(discovery[discovery.length-1].contains("["))
            			{
            				discovery[discovery.length-1] = discovery[discovery.length-1].substring(0, discovery[discovery.length-1].indexOf('['));
            			}
            			if(discovery[discovery.length-1].contains("-"))
            			{
            				discovery[discovery.length-1] = discovery[discovery.length-1].substring(0, discovery[discovery.length-1].indexOf('-'));
            			}
            			discovery[discovery.length-1] = discovery[discovery.length-1].replaceAll("[^0-9]", "");
            			py_exoplanets.append(", discovered = \"" + discovery[discovery.length-1] + "\"");
            		}
            	}
            	//orbital_period
            	n = doc.select("table.infobox tr");
            	doc.select("span[style*=display:none]").remove();
            	int has_orbit = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Orbital period"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_exoplanets.append(", orbital_period = " + number[i]);
            					i = number.length;
            				}
            			}
            			has_orbit++;
            		}
            	}
            	if(has_orbit > 1 || has_orbit == 0)
            	{
            		save_exoplanet = false;
            	}
            	//semi_major_axis
            	n = doc.select("table.infobox tr");
            	doc.select("span[style*=display:none]").remove();
            	int has_axis = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Semimajor axis"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			String[] check_neg = changer.split("Semimajor axis ");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					if(check_neg[1].charAt(0) == 8722)
            					{
            						number[i] = "-" + number[i];
            					}
            					py_exoplanets.append(", semi_major_axis = " + number[i]);
            					i = number.length;
            				}
            			}
            			has_axis++;
            		}
            	}
            	if(has_axis > 1 || has_axis == 0)
            	{
            		save_exoplanet = false;
            	}
            	//discovery_method
            	for(Element e : n)
            	{
            		if(e.text().contains("Discovery method"))
            		{ 
            			String method = e.text();
            			if(method.contains("["))
            			{
            				method = method.substring("Discovery method ".length(), method.indexOf('['));
            			}
            			py_exoplanets.append(", discovery_method = \"" + method + "\"");
            		}
            	}
            	// fk_star_planet
            	int key = -1;
            	if(star_keys.containsKey(pair.getValue()))
            	{
            		key = star_keys.get(pair.getValue());
            	}
            	else
            	{
            		System.out.println("FIND THE KEY FOR " + pair.getValue());
            	}
            	py_exoplanets.append(", fk_star_planet = " + key);
            	// history
            	py_exoplanets.append(", history = " + "None");
    	    	// photo_link
            	py_exoplanets.append(", photo_link = " + "None");
    	    	// photo
            	py_exoplanets.append(", photo = " + "None))");
            	if(save_exoplanet)
            	{
            		System.out.println(py_exoplanets.toString());
            	}
			} catch (IOException e) {
				
			}
            it.remove(); // avoids a ConcurrentModificationException
        }
    }
    
    public static Map<String,String> extractStarsUsingJsoup(String url)
    {
    	Map<String,String> exoPlanetStar = new HashMap<String,String>();
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

        	int key = 2;
    		for(String star : urls)
    		{
        		StringBuilder py_stars = new StringBuilder();
    			// name
    			py_stars.append("db.session.add(star(");
            	doc = Jsoup.connect(star).get();
            	Elements n = doc.select("table.infobox caption");
            	String star_name = "";
            	boolean save_star = true;
            	for(Element e : n)
            	{
            		star_name = e.text();
            		py_stars.append("name = \"" + star_name + "\"");
            		star_keys.put(star_name, key);
            	}
    	    	// mass
            	n = doc.select("table.infobox tr");
            	doc.select("span[style*=display:none]").remove();
            	int has_mass = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Mass"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_stars.append(", mass = " + number[i]);
            					i = number.length;
            				}
            			}
            			
            			has_mass++;
            		}
            	}
            	if(has_mass > 1 || has_mass == 0)
            	{
            		save_star = false;
            	}
    	    	// radius
            	int has_radius = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Radius"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_stars.append(", radius = " + number[i]);
            					i = number.length;
            				}
            			}
            			
            			has_radius++;
            		}
            	}
            	if(has_radius > 1 || has_radius == 0)
            	{
            		save_star = false;
            	}
    	    	// spectral_type
            	int has_spect = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Spectral type"))
            		{
            			String diff = changer.replaceAll("[^0-9\\s\\w]","_");
            			diff = diff.replaceAll("Spectral type ", "_");
            			String[] number = diff.split("_");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_stars.append(", spectral_type = " + "\"" + number[i] + "\"");
            					i = number.length;
            				}
            			}
            			
            			has_spect++;
            		}
            	}
            	if(has_spect > 1 || has_spect == 0)
            	{
            		save_star = false;
            	}
    	    	// temperature
            	int has_temperature = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Temperature"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_stars.append(", temperature = " + number[i]);
            					i = number.length;
            				}
            			}
            			
            			has_temperature++;
            		}
            	}

            	if(has_temperature > 1 || has_temperature == 0)
            	{
            		save_star = false;
            	}
    	    	// luminosity
            	int has_luminosity = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Luminosity"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_stars.append(", luminosity = " + number[i]);
            					i = number.length;
            				}
            			}
            			
            			has_luminosity++;
            		}
            	}
            	if(has_luminosity > 1 || has_luminosity == 0)
            	{
            		save_star = false;
            	}
    	    	// stellar_distance
            	int has_dist = 0;
            	for(Element e : n)
            	{
            		String changer = e.text();
            		if(e.text().contains("Distance"))
            		{
            			String diff = changer.replaceAll("[^0-9\\.,]","A");
            			diff = diff.replaceAll("[,]","");
            			String[] number = diff.split("A");
            			for(int i = 0; i < number.length; i++)
            			{
            				if(number[i].length() > 0)
            				{
            					py_stars.append(", stellar_distance = " + number[i]);
            					i = number.length;
            				}
            			}
            			
            			has_dist++;
            		}
            	}
            	if(has_dist > 1 || has_dist == 0)
            	{
            		save_star = false;
            	}
    	    	// planetary_systems
            	Map<String, String> temp = new HashMap<String, String>();
            	int count_planet = 0;
            	Elements planets = doc.select("table.wikitable td:eq(0)");
            	iter = planets.listIterator();
                while(iter.hasNext()) 
        	    {
            		Element e = (Element) iter.next();
            		count_planet++;
        	    }
                planets = doc.select("table.wikitable td:eq(0) a");
            	iter = planets.listIterator();
                while(iter.hasNext()) 
        	    {
                	Element e = (Element) iter.next();
            		String s = e.attr("abs:href");
                	if(!s.contains("redlink"))
            		{
	            		temp.put(s, star_name);
            		}
        	    }
                py_stars.append(", planetary_systems = " + count_planet);
    	    	// fk_constellation_star
                for(Element e : n)
            	{
            		if(e.text().contains("Constellation"))
            		{
            			String[] number = e.text().split("Constellation ");
            			int constellation_key = -1;
            			if(number[number.length - 1].contains("["))
            			{
            				number[number.length - 1] = number[number.length - 1].substring(0, number[number.length - 1].indexOf('['));
            			}
            			if(constellation_keys.containsKey(number[number.length - 1]))
            			{
            				constellation_key = constellation_keys.get(number[number.length - 1]);
            				py_stars.append(", fk_constellation_star = " + constellation_key);
            			}
            			else
            			{
            				py_stars.append(", fk_constellation_star = " + constellation_key);
            				System.out.println("FIND THE KEY FOR" + number[number.length -1]);
            			}
            		}
            	}
    	    	// history
            	py_stars.append(", history = " + "None");
    	    	// photo_link
            	py_stars.append(", photo_link = " + "None");
    	    	// photo
            	py_stars.append(", photo = " + "None))");
            	if(save_star)
            	{
            		exoPlanetStar.putAll(temp);
            		key++;
            		System.out.println(py_stars.toString());
            	}
    		}
    	}
    	catch (IOException e) {
    		 
    	}
    	return exoPlanetStar;
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

        	int count = 2;
            for(String constellation : urls)
            {
            	System.out.print("db.session.add(constellation(");
            	doc = Jsoup.connect(constellation).get();
            	Elements n = doc.select("table.infobox caption");
            	for(Element e : n)
            	{
            		System.out.print("name = \"" + e.text() + "\"");
            		constellation_keys.put(e.text(), count);
            		count++;
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
            			String[] arr = {"NOT GOING TO MATCH","Ursa Major", "Zodiac", "Perseus", "Hercules", "Orion", "Heavenly Waters", "Bayer", "La Caille"};
            			int index = -1;
            			for(int i = 1; i < arr.length; i++)
            			{
            				if(number[number.length-1].contains(arr[i]))
            				{
            					index = i;
            				}
            			}
            			System.out.print(", fk_constellation_family = " + index);
            		}
            	}
            	System.out.println("))");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
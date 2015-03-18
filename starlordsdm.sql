DROP TABLE "constellation";
DROP TABLE "planet";
DROP TABLE "star";
DROP TABLE "moon";
DROP TABLE "family";

CREATE TABLE "constellation" (
"id" INTEGER NOT NULL,
"name" TEXT NOT NULL,
"history" TEXT,
"photo_link" TEXT,
"area" TEXT,
"stars_with_planets" INTEGER,
"brightest_star" TEXT,
"nearest_star" TEXT,
"fk_constellation_family" TEXT,
PRIMARY KEY ("id") ,
CONSTRAINT "fk_constellation_family" FOREIGN KEY ("fk_constellation_family") REFERENCES "family" ("name")
);

CREATE TABLE "planet" (
"id" INTEGER NOT NULL,
"name" TEXT NOT NULL,
"radius" REAL,
"rings" INTEGER,
"distance_from_sun" REAL,
"composition" TEXT,
"type" TEXT,
"is_dwarf" INTEGER,
"days_of_revolution" TEXT,
"volume" REAL,
"mass" REAL,
"density" REAL,
"surface_area" REAL,
"gravity" REAL,
"length_of_day" REAL,
"length_of_year" REAL,
"surface_temperature" REAL,
"atmosphere" TEXT,
"number_of_moons" INTEGER,
"history" TEXT,
"photo_link" TEXT,
"fk_star_planet" INTEGER,
PRIMARY KEY ("id") ,
CONSTRAINT "fk_star_planet" FOREIGN KEY ("fk_star_planet") REFERENCES "star" ("id")
);

CREATE TABLE "star" (
"id" INTEGER NOT NULL,
"name" TEXT,
"mass" REAL,
"radius" REAL,
"age" REAL,
"temperature" REAL,
"stellar_distance" REAL,
"stellar_classification" TEXT,
"henry_draper_catalogue" INTEGER,
"hipparcos_catalogue" INTEGER,
"right_ascension" TEXT,
"declination" TEXT,
"apparent_magnitued" REAL,
"absolute_magnitude" REAL,
"luminosity" TEXT,
"photo_link" TEXT,
"history" TEXT,
"fk_constellation_star" INTEGER,
PRIMARY KEY ("id") ,
CONSTRAINT "fk_constellation_star" FOREIGN KEY ("fk_constellation_star") REFERENCES "constellation" ("id")
);

CREATE TABLE "moon" (
"id" INTEGER NOT NULL,
"name" TEXT,
"radius" REAL,
"volume" REAL,
"mass" REAL,
"distance_from_planet" REAL,
"orbital_period" REAL,
"surface_gravity" REAL,
"history" TEXT,
"photo_link" TEXT,
"fk_planet_moon" INTEGER,
PRIMARY KEY ("id") ,
CONSTRAINT "fk_planet_moon" FOREIGN KEY ("fk_planet_moon") REFERENCES "planet" ("id")
);

CREATE TABLE "family" (
"name" TEXT NOT NULL,
PRIMARY KEY ("name") 
);


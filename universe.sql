ALTER TABLE "star" DROP CONSTRAINT "fk_constellation_star";
ALTER TABLE "planet" DROP CONSTRAINT "fk_star_planet";
ALTER TABLE "moon" DROP CONSTRAINT "fk_planet_moon";
ALTER TABLE "constellation" DROP CONSTRAINT "fk_constellation_family";

DROP TABLE "constellation";
DROP TABLE "planet";
DROP TABLE "star";
DROP TABLE "moon";
DROP TABLE "family";

CREATE TABLE "constellation" (
"id" int NOT NULL,
"name" TEXT NOT NULL,
"area" float8,
"stars_with_planets" int,
"brightest_star" TEXT,
"nearest_star" TEXT,
"fk_constellation_family" TEXT,
"history" TEXT,
"photo_link" TEXT,
"photo" bytea,
PRIMARY KEY ("id") 
);

CREATE TABLE "planet" (
"id" int NOT NULL,
"name" TEXT NOT NULL,
"radius" float8,
"rings" int,
"distance_from_sun" float8,
"composition" TEXT,
"is_dwarf" bool,
"orbital_period" float8,
"volume" float8,
"mass" float8,
"density" float8,
"surface_area" float8,
"gravity" float8,
"length_of_day" float8,
"length_of_year" float8,
"surface_temperature" float8,
"atmosphere" TEXT,
"number_of_moons" int,
"history" TEXT,
"photo_link" TEXT,
"fk_star_planet" int,
"photo" bytea,
PRIMARY KEY ("id") 
);

CREATE TABLE "star" (
"id" int NOT NULL,
"name" TEXT,
"mass" float8,
"radius" float8,
"temperature" float8,
"luminosity" float8,
"surface gravity" float8,
"stellar_distance" float8,
"stellar_classification" TEXT,
"henry_draper_catalogue" int,
"hipparcos_catalogue" int,
"apparent_magnitude" float8,
"absolute_magnitude" float8,
"photo_link" TEXT,
"history" TEXT,
"fk_constellation_star" int,
"parallax" float8,
"photo" bytea,
PRIMARY KEY ("id") 
);

CREATE TABLE "moon" (
"id" int NOT NULL,
"name" TEXT,
"radius" float8,
"volume" float8,
"mass" float8,
"distance_from_planet" float8,
"orbital_period" float8,
"surface_gravity" float8,
"history" TEXT,
"photo_link" TEXT,
"fk_planet_moon" int,
"photo" bytea,
PRIMARY KEY ("id") 
);

CREATE TABLE "family" (
"name" TEXT NOT NULL,
PRIMARY KEY ("name") 
);


ALTER TABLE "star" ADD CONSTRAINT "fk_constellation_star" FOREIGN KEY ("fk_constellation_star") REFERENCES "constellation" ("id");
ALTER TABLE "planet" ADD CONSTRAINT "fk_star_planet" FOREIGN KEY ("fk_star_planet") REFERENCES "star" ("id");
ALTER TABLE "moon" ADD CONSTRAINT "fk_planet_moon" FOREIGN KEY ("fk_planet_moon") REFERENCES "planet" ("id");
ALTER TABLE "constellation" ADD CONSTRAINT "fk_constellation_family" FOREIGN KEY ("fk_constellation_family") REFERENCES "family" ("name");


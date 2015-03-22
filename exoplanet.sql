ALTER TABLE "star" DROP CONSTRAINT "fk_constellation_star";
ALTER TABLE "Planet" DROP CONSTRAINT "fk_star_planet";
ALTER TABLE "moon" DROP CONSTRAINT "fk_planet_moon";
ALTER TABLE "constellation" DROP CONSTRAINT "fk_constellation_family";
ALTER TABLE "ExoPlanet" DROP CONSTRAINT "fk_ExoPlanet";

DROP TABLE "constellation";
DROP TABLE "Planet";
DROP TABLE "star";
DROP TABLE "moon";
DROP TABLE "family";
DROP TABLE "ExoPlanet";

CREATE TABLE "constellation" (
"id" int NOT NULL,
"name" TEXT NOT NULL,
"stars_with_planets" int,
"meaning" TEXT,
"fk_constellation_family" int,
"history" TEXT,
"photo_link" TEXT,
"photo" bytea,
PRIMARY KEY ("id") 
);

CREATE TABLE "Planet" (
"id" int NOT NULL,
"name" TEXT NOT NULL,
"distance_from_sun" float8,
"composition" TEXT,
"orbital_period" float8,
"volume" float8,
"mass" float8,
"density" float8,
"surface_area" float8,
"semi_major_axis" float8,
"rings" int,
"gravity" float8,
"length_of_day" float8,
"length_of_year" float8,
"surface_temperature" float8,
"atmosphere" TEXT,
"number_of_moons" int,
"history" TEXT,
"fk_star_planet" int,
"photo_link" TEXT,
"photo" bytea,
PRIMARY KEY ("id") 
);

CREATE TABLE "star" (
"id" int NOT NULL,
"name" TEXT,
"mass" float8,
"radius" float8,
"spectral_type" TEXT,
"temperature" float8,
"luminosity" float8,
"stellar_distance" float8,
"parallax" float8,
"planetary systems" int,
"fk_constellation_star" int,
"history" TEXT,
"photo_link" TEXT,
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
"photo" bytea,
"fk_planet_moon" int,
PRIMARY KEY ("id") 
);

CREATE TABLE "family" (
"id" int NOT NULL,
"name" TEXT,
PRIMARY KEY ("id") 
);

CREATE TABLE "ExoPlanet" (
"id" int NOT NULL,
"name" TEXT NOT NULL,
"discovered" TEXT,
"orbital_period" float8,
"semi_major_axis" float8,
"discovery_method" text,
"history" TEXT,
"fk_star_planet" int,
"photo_link" TEXT,
"photo" bytea,
PRIMARY KEY ("id") 
);


ALTER TABLE "star" ADD CONSTRAINT "fk_constellation_star" FOREIGN KEY ("fk_constellation_star") REFERENCES "constellation" ("id");
ALTER TABLE "Planet" ADD CONSTRAINT "fk_star_planet" FOREIGN KEY ("fk_star_planet") REFERENCES "star" ("id");
ALTER TABLE "moon" ADD CONSTRAINT "fk_planet_moon" FOREIGN KEY ("fk_planet_moon") REFERENCES "Planet" ("id");
ALTER TABLE "constellation" ADD CONSTRAINT "fk_constellation_family" FOREIGN KEY ("fk_constellation_family") REFERENCES "family" ("id");
ALTER TABLE "ExoPlanet" ADD CONSTRAINT "fk_ExoPlanet" FOREIGN KEY ("fk_star_planet") REFERENCES "star" ("id");


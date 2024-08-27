"# Movie-Duration-Match" 
Movie Duration Match


As a data scientist at Amazon Prime Video, you are tasked with enhancing the in-flight entertainment experience for Amazon’s airline partners. Your challenge is to develop a feature that suggests individual movies from Amazon's content database that fit within a given flight's duration. For flight 101, find movies whose runtime is less than or equal to the flight's duration.


The output should list suggested movies for the flight, including 'flight_id', 'movie_id', and 'movie_duration'."

Tables: entertainment_catalog, flight_schedule

entertainment_catalog

movie_id:
int
title:
varchar
duration:
int

flight_schedule

flight_id:
int
flight_duration:
int
flight_date:
datetime

link "https://platform.stratascratch.com/coding/10360-movie-duration-match?code_type=3"

data analysis project i used fake data to solve it by excel,python,sql
#Exercise 1 - Show all tables.
USE sakila;
show tables;

#Exercise 2 - Retrieve all the data from the tables actor, film and customer.
SELECT * FROM actor,film,customer;
#another way
select * from actor;
select * from film;
select * from customer;

# Exercise 3 - Retrieve the following columns from their respective tables:
# 3.1 - Titles of all films from the film table 
SELECT title from film;

# 3.2. List of languages used in films, with the column aliased as language from the language table
SELECT name as language from language;

# 3.3 List of first names of all employees from the staff table
select first_name from staff;

# Exercise 4 - Retrieve unique release years
select DISTINCT(release_year) from film;

# Exercise 5 - ounting records for database insights
# 5.1 Determine the number of stores that the company has.
select count(store_id) from inventory;

# 5.2 Determine the number of employees that the company has.
select count(staff_id) from staff;

# 5.3 Determine how many films are available for rent and how many have been rented.
select count(rental_id) as 'films rented' from rental;
select count(film_id) as 'films available for rent' from film;

# 5.4 Determine the number of distinct last names of the actors in the database.
select count(distinct(last_name)) from actor;

#Exercise 6 - Retrieve the 10 longest films
select length as duration from film order by length desc limit 10;

# Exercise 7- Use filtering techniques in order to:
# 7.1 Retrieve all actors with the first name "SCARLETT".
SELECT first_name from actor where first_name like "SCARLETT";

#7.2 Retrieve all movies that have ARMAGEDDON in their title and have a duration longer than 100 minutes.
#Hint: use LIKE operator. More information here.
SELECT title,length as duration from film where title LIKE '%ARMAGEDDON%' and length>100;

#7.3 Determine the number of films that include Behind the Scenes content
select count(special_features) as BTS_count from film where special_features like '%Behind the Scenes%';




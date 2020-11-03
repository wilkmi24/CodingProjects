/* Assignment #1 */
SELECT * FROM tbl_habitat;

/* Assignment #2*/
SELECT * FROM tbl_species
    WHERE species_order = 3

/* Assignment #3 */    
SELECT * FROM tbl_nutrition 
    WHERE nutrition_cost <= 600;

/*Assignment #4 */
SELECT * FROM tbl_species 
    WHERE species_nutrition BETWEEN 2202 AND 2206;

/* Assignment #5 */
SELECT tbl_species.species_name AS 'Species Name', 
tbl_nutrition.nutrition_id AS 'Nutrition Type' FROM tbl_species
JOIN tbl_nutrition ON tbl_species.species_nutrition = tbl_nutrition.nutrition_id;

/* Assignment #6 */
SELECT tbl_specialist.specialist_fname, tbl_specialist.specialist_lname, tbl_specialist.specialist_contact 
FROM tbl_specialist
INNER JOIN tbl_care ON care_specialist = specialist_id
INNER JOIN tbl_species ON species_care = care_id
WHERE tbl_species.species_name ='penguin';


-- List all records in `second_table` with initialised name values
-- The output includes name and score, and is sorted in descending order of score
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;

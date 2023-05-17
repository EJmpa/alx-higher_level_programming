-- Displays the max temperature of each state (ordered by State name).
-- Query to perform operation
SELECT state, MAX(value) AS max_temp
       FROM temperatures
       GROUP BY state
       ORDER BY state ASC;

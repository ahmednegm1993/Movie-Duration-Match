WITH target_duration AS (
    SELECT flight_id, flight_duration
    FROM [dbo].[flight_schedule] 
    WHERE flight_id = 101
)
SELECT ec.movie_id, ec.duration AS movie_duration, td.flight_id
FROM [dbo].[entertainment_catalog] ec
JOIN target_duration td ON ec.duration <= td.flight_duration;

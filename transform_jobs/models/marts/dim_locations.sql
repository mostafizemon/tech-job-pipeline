{{ config(materialized='table') }}

SELECT DISTINCT
    md5(location_name) AS location_id,
    location_name
FROM {{ ref('stg_jobs') }}
WHERE location_name IS NOT NULL
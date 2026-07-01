{{ config(materialized='table') }}

SELECT DISTINCT
    md5(job_category) AS category_id,
    job_category
FROM {{ ref('stg_jobs') }}
WHERE job_category IS NOT NULL
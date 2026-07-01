{{ config(materialized='table') }}

SELECT 
    job_id,
    job_title,
    md5(company_name) AS company_id,
    md5(location_name) AS location_id,
    md5(job_category) AS category_id,
    
    
    contract_type,
    contract_time,
    salary_min,
    salary_max,
    created_at
    
FROM {{ ref('stg_jobs') }}
WHERE job_id IS NOT NULL
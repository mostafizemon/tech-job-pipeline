{{ config(materialized='table') }}

SELECT DISTINCT
    md5(company_name) AS company_id,
    company_name
FROM {{ ref('stg_jobs') }}
WHERE company_name IS NOT NULL
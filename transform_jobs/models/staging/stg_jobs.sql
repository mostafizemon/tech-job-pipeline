WITH raw_data AS (
    SELECT * FROM {{ source('job_market', 'bronze_jobs') }}
),

cleaned_data AS (
    SELECT DISTINCT
        id::VARCHAR AS job_id,
        title::VARCHAR AS job_title,
        company.display_name::VARCHAR AS company_name,
        location.display_name::VARCHAR AS location_name,
        category.label::VARCHAR AS job_category,
        contract_type::VARCHAR AS contract_type,
        contract_time::VARCHAR AS contract_time,
        salary_min::FLOAT AS salary_min,
        salary_max::FLOAT AS salary_max,
        created::TIMESTAMP AS created_at
    FROM raw_data
)

SELECT * FROM cleaned_data
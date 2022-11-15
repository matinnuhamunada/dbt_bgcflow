SELECT *
FROM {{ source('external_location', 'regions') }}
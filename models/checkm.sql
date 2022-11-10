WITH src_checkm AS (
    SELECT * FROM {{ ref('df_checkm_stats') }}
),

stg_checkm AS (
    SELECT
        genome_id,
        Completeness AS completeness,
        Contamination AS contamination,
        "# ambiguous bases" AS num_ambiguous_bases,
        "Coding density" AS coding_density,
        "# predicted genes" AS num_predicted_genes       
    FROM src_checkm
)

SELECT * FROM stg_checkm
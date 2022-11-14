WITH src_taxa AS (
    SELECT * FROM {{ ref('gtdb_meta') }}
),

src_genomes AS (
    SELECT * FROM {{ ref('antismash_6.1.1_summary') }}
),

stg_taxa AS (
    SELECT
        md5(Domain || Phylum || Class || src_taxa.Order || Family || Genus || Organism) AS tax_id,
        genome_id,
    FROM src_taxa
),

stg_genomes AS(
    SELECT 
        src_genomes.genome_id, 
        stg_taxa.tax_id,
        src_genomes.source,
        src_genomes.strain,
        src_genomes.bgcs_count,
        src_genomes.bgcs_on_contig_edge,
    FROM src_genomes, stg_taxa
    WHERE
        src_genomes.genome_id = stg_taxa.genome_id
)

SELECT * FROM stg_genomes

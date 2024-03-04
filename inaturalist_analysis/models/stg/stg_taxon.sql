select taxon from {{ source("airflow", "cq_inaturalist_observations") }} group by taxon

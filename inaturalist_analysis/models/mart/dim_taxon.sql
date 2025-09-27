with source as (select * from {{ ref("stg_taxon") }}) select * from source

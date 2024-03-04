with
    source as (select * from {{ ref("stg_observations") }}),
    taxon as (select * from {{ ref("dim_taxon") }}),
    final as (
        select
            source.observation_id,
            source.uuid,
            source.uri,
            source.taxon_id,
            source.latitude,
            source.longitude,
            source.quality_grade,
            taxon.name as scientific_name,
            taxon.preferred_common_name as common_name,
            taxon.complete_rank,
            taxon.wikipedia_url,
            taxon.ancestry
        from source
        left join taxon on source.taxon_id = taxon.taxon_id
    )

select *
from final

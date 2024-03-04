with
    observations as (select * from {{ ref("stg_observations") }}),
    taxon as (select * from {{ ref("dim_taxon") }}),

    final as (
        select taxon.preferred_common_name as common_name, count(*)
        from observations
        left join taxon on observations.taxon_id = taxon.taxon_id
        group by common_name
        order by count(*) desc
    )

select *
from final

with
    observations as (select * from {{ ref("stg_observations") }}),

    final as (
        select quality_grade, count(*)
        from observations
        group by quality_grade
        order by count(*) desc
    )

select *
from final

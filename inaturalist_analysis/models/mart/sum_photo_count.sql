with
    photos as (select * from fct_photos),
    observations as (select * from fct_observations),
    final as (
        select observations.common_name, count(photos.observation_id) as photo_count
        from observations
        left join photos on photos.observation_id = observations.observation_id
        group by observations.common_name
        order by photo_count desc
    )

select *
from final

with
    source as (
        select
            observation_id,
            (data -> 'id')::integer as photo_id,
            (data -> 'url')::text as url,
            (data -> 'attribution')::text as attribution,
            (data -> 'license_code')::text as license_code,
            (data -> 'original_dimensions' -> 'width')::integer as photo_width,
            (data -> 'original_dimensions' -> 'height')::integer as photo_height
        from {{ ref("stg_photos") }}, lateral jsonb_array_elements(photos) as data
    ),

    final as (
        select
            observation_id,
            photo_id,
            url,
            attribution,
            license_code,
            photo_width,
            photo_height,
            photo_width * photo_height as total_pixels
        from source
    )

select *
from final

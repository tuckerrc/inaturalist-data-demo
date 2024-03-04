select
    observation_id,
    (data ->> 'id')::integer as photo_id,
    (data ->> 'url')::text as url,
    (data ->> 'attribution')::text as attribution,
    (data ->> 'license_code')::text as license_code
from {{ ref("stg_photos") }}, lateral jsonb_array_elements(photos) as data

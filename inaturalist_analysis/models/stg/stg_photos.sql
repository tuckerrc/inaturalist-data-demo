select id as observation_id, photos
from {{ source("airflow", "cq_inaturalist_observations") }}

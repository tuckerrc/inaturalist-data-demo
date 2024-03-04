with
    source as (select * from {{ source("airflow", "cq_inaturalist_observations") }}),
    renamed as (
        select
            source.id as observation_id,
            quality_grade as quality_grade,
            uuid as uuid,
            time_observed_at as time_observed_at,
            species_guess as species_guess,
            uri as uri,
            location as location,
            cast(split_part(location, ',', 1) as float) as latitude,
            cast(split_part(location, ',', 2) as float) as longitude,
            identifications_some_agree as identifications_some_agree,
            num_identification_agreements as num_identification_agreements,
            num_identification_disagreements as num_identification_disagreements,
            place_guess as place_guess,
            identifications as identifications,
            taxon_data.id as taxon_id
        from source, jsonb_to_record(taxon) as taxon_data(id int)
    )

select *
from renamed

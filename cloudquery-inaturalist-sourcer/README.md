# Python iNaturalist Sourcer

Simple sourcer for iNaturalist Observations inside a bounding box from the
iNaturalist API ([api.inaturalist.org](https://api.inaturalist.org/v1/docs/)).

Created from the clouquery [python-plugin-template](https://github.com/cloudquery/python-plugin-template) repo 

## Config Spec

Configurable attributes: `base_url`, `family_id`,and `bbox`.

```yaml
spec:
  [...sources_attributes]
  spec:
    base_url: https://api.inaturalist.org
    family_id: 7823 # Corvidae
    bbox: # Wake County, NC
      swlat: 35.530836
      swlng: -79.071087
      nelat: 36.117908
      nelng: -78.247617
```

 - `base_url` - api url
 - `family_id` - taxon id for the observations you want to source
 - `bbox` - bounding box limit (southwest to northeast corners)

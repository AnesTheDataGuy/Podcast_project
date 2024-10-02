import json
from listennotes import podcast_api
from pprint import pprint

client = podcast_api.Client(api_key='c3817fba0b204e06a612a50019bb8ebe')
response = client.fetch_best_podcasts(
  q='star wars',
  sort_by_date=0,
  type='episode',
  offset=0,
  len_min=10,
  len_max=30,
  genre_ids='68,82',
  published_before=1580172454000,
  published_after=0,
  only_in='title,description',
  language='English',
  safe_mode=0,
  unique_podcasts=0,
  interviews_only=0,
  sponsored_only=0,
  page_size=10,
)
pprint(type(json.dumps(response.json())))


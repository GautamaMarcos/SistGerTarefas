import requests
from django.conf import settings

SUPABASE_URL = settings.SUPABASE_URL
SUPABASE_SERVICE_ROLE_KEY = settings.SUPABASE_SERVICE_ROLE_KEY

headers = {
    "apikey": SUPABASE_SERVICE_ROLE_KEY,
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}"
}

def fetch_from_supabase(endpoint):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    response = requests.get(url, headers=headers)
    return response.json()

def insert_to_supabase(endpoint, data):
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    response = requests.post(url, json=data, headers=headers)
    return response.json()


# from supabase import create_client, Client
# import os

# url: str = os.getenv("SUPABASE_URL")
# key: str = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(url, key)






# import requests
# from django.conf import settings

# SUPABASE_URL = settings.SUPABASE_URL
# SUPABASE_KEY = settings.SUPABASE_KEY

# headers = {
#     "apikey": SUPABASE_KEY,
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {SUPABASE_KEY}"
# }

# def fetch_from_supabase(endpoint):
#     url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
#     response = requests.get(url, headers=headers)
#     return response.json()

# def insert_to_supabase(endpoint, data):
#     url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
#     response = requests.post(url, json=data, headers=headers)
#     return response.json()

import requests, json
from pathlib import Path

TOKEN = "cfoat_zJKn9NbwmPszp4aRViHMOeKxuVuNUR8dlE41Capr8eg.GO9w799RqagtQI3JLV6ThBCY3QehfPPccswfJJY4Jb4"
ACCOUNT_ID = "0a68341689fffbae0284be2321350415"
PROJECT = "porsche-digest"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# First: get upload token (returns JWT for signing artifacts upload)
resp = requests.post(
    f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/upload-token",
    headers=headers
)
upload_jwt = resp.json()["result"]["jwt"]
print("Upload JWT:", upload_jwt[:30], "...")

# Second: upload artifacts via R2 signed POST (not API)
# The upload JWT is used as Authorization for the upload endpoint
upload_url = f"https://upload-assets.github.io/{PROJECT}-v7-deploy.zip"  # This is wrong; need proper endpoint

# Let's check the correct upload endpoint by listing available ones
print("Response from upload-token:", resp.json())

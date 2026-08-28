"""
Update CNAME record using browser-use CLI in headless mode.
The browser-use CLI handles auth automatically via the existing Chrome session.
"""
import subprocess
import json
import time
import sys
import os
import tempfile
import textwrap

task_description = textwrap.dedent("""
You are already logged into the Cloudflare dashboard. 

Navigate to: https://dash.cloudflare.com/0a68341689fffbae0284be2321350415/costafamily.ai/dns/records

Find the DNS record with name "digest" and type "CNAME". It currently shows:
- Name: digest.costafamily.ai  
- Type: CNAME
- Content: porsche-digest.pages.dev
- Proxy status: Proxied

Your task:
1. Click the row to expand it (if collapsed)
2. Find and click the "Edit" button for the digest record ONLY
3. Wait for the edit form to appear with a "Target" textarea
4. The textarea should contain "porsche-digest.pages.dev"
5. Clear it and type "porsche-digest-v7.pages.dev" 
6. Click "Save"
7. Wait 5 seconds for the page to process
8. Confirm the change was successful by checking the record shows the new target

IMPORTANT: Make sure you're editing the DIGEST record, not the DOCS record. 
The record name should be "digest.costafamily.ai".
After editing, verify the content shows "porsche-digest-v7.pages.dev".
""").strip()

# Write task to file
with open("/c/Users/SERVER/Hermes-Workspace/porsche-digest/task.txt", "w") as f:
    f.write(task_description)

# Use browser-use CLI to run the task
cmd = [
    sys.executable, "-m", "browser_use.cli", "run",
    "/c/Users/SERVER/Hermes-Workspace/porsche-digest/task.txt"
]

# Set environment for browser-use
env = os.environ.copy()
env["BROWSER_USE_HEADLESS"] = "false"
env["CHROME_PATH"] = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

print("Running browser-use CLI task...")
print(f"Task description written to: /c/Users/SERVER/Hermes-Workspace/porsche-digest/task.txt")
print(f"Chrome path: {env.get('CHROME_PATH')}")
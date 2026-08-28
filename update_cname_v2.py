"""
Update CNAME record for digest.costafamily.ai via Cloudflare Dashboard UI.
Uses Chrome DevTools Protocol directly to interact with the page.
"""
import subprocess
import json
import time
import os

# Check if Chrome is running with remote debugging
def check_chrome():
    result = subprocess.run(
        ["curl", "-s", "http://127.0.0.1:9222/json"],
        capture_output=True, text=True
    )
    if result.returncode == 0 and result.stdout:
        tabs = json.loads(result.stdout)
        for tab in tabs:
            if "dash.cloudflare.com" in tab.get("url", ""):
                return tab
    return None

def exec_cdp(tab_id, cmd, params=None):
    """Execute a CDP command on a specific tab"""
    if params is None:
        params = {}
    payload = {
        "id": 1,
        "method": cmd,
        "params": params
    }
    result = subprocess.run(
        ["curl", "-s", "-X", "POST", "-H", "Content-Type: application/json",
         "-d", json.dumps(payload),
         f"http://127.0.0.1:9222/json/execute/6c6b5a07-5b3a-4b3a-8b3a-000000000000"],  # placeholder
        capture_output=True, text=True
    )
    return result.stdout

# Let's use a simpler approach - create a script that will be run by the browser
script = """
(async () => {
    // Go to DNS records page
    window.location.href = 'https://dash.cloudflare.com/0a68341689fffbae0284be2321350415/costafamily.ai/dns/records';
    
    // Wait a bit and then find the edit button
    setTimeout(() => {
        const editButtons = document.querySelectorAll('button[aria-label*="Edit" i]');
        for (const btn of editButtons) {
            if (btn.textContent.includes('digest')) {
                btn.click();
                console.log('Clicked edit for digest');
                break;
            }
        }
    }, 5000);
})();
"""

# Save the script to a file that can be injected
with open("/c/Users/SERVER/Hermes-Workspace/porsche-digest/inject_update.js", "w") as f:
    f.write(script)
    
print("Script written. Will need manual injection or different approach.")
print("Checking Chrome debug status...")

result = check_chrome()
if result:
    print(f"Found Cloudflare tab: {result.get('title', 'unknown')}")
    print(f"URL: {result.get('url', 'unknown')}")
    print(f"Target: {result.get('webSocketDebuggerUrl', 'not found')}")
else:
    print("No Chrome tab with Cloudflare found. Is Chrome running with --remote-debugging-port=9222?")
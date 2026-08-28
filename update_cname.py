"""
Update CNAME record for digest.costafamily.ai via Cloudflare Dashboard UI.
Uses browser automation with the existing Chrome session.
"""
from browser_use import Agent
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.environ.get("OPENAI_API_KEY", "")
)

agent = Agent(
    task="""
    You are already logged into the Cloudflare dashboard via Chrome.
    Navigate to https://dash.cloudflare.com/0a68341689fffbae0284be2321350415/costafamily.ai/dns/records
    
    In the DNS records table, find the record:
    - Name: digest.costafamily.ai
    - Type: CNAME
    - Current Content: porsche-digest.pages.dev
    
    Steps to update:
    1. Click on the "Expand digest record" button to expand that row
    2. Click the "Edit" button that appears in that row
    3. A form should appear. Find the "Target" textarea field.
    4. Clear the existing value (porsche-digest.pages.dev) and type "porsche-digest-v7.pages.dev"
    5. Click the "Save" button.
    6. Wait for any success notification or page refresh.
    7. Verify that the digest CNAME now shows porsche-digest-v7.pages.dev
    
    Be very careful to interact with the CORRECT record (digest, not docs or protonmail).
    If you make a mistake, click "Cancel" and try again.
    """,
    llm=llm,
    max_actions_per_step=10,
    use_vision=True
)

result = agent.run()
print(str(result))
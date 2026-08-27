import asyncio, json, os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command='npx',
    args=['-y', '@cloudflare/mcp-server-cloudflare']
)

async def ***REMOVED***_cloudflare_mcp():
    try:
        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                tools = await session.list_tools()
                print('Available Cloudflare MCP tools:')
                for t in tools.tools:
                    desc = t.description[:80] if t.description else ""
                    print(f'  - {t.name}: {desc}...')
    except Exception as e:
        print(f'Error: {str(e)[:200]}')

asyncio.run(***REMOVED***_cloudflare_mcp())

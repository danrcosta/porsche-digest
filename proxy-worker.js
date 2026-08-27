export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const targetUrl = `https://porsche-digest.pages.dev${url.pathname}${url.search}`;
    
    const response = await fetch(targetUrl, {
      method: request.method,
      headers: {
        ...request.headers,
        'host': 'porsche-digest.pages.dev',
      },
    });
    
    return new Response(response.body, {
      status: response.status,
      headers: response.headers,
    });
  }
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const subdomain = 'porsche-digest.pages.dev';
    const targetUrl = `https://${subdomain}${url.pathname}`;
    
    // Proxy all requests to the Pages domain to bypass WAF
    const response = await fetch(targetUrl, {
      method: request.method,
      headers: { ...request.headers },
    });
    
    return new Response(response.body, {
      status: response.status,
      headers: response.headers,
    });
  }
}

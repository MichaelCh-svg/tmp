from mitmproxy import http, ctx

def load(loader):
    ctx.options.ssl_insecure = True  # Disable certificate validation for upstream servers

def request(flow: http.HTTPFlow) -> None:
    if flow.client_conn.address[0] == "YOUR_PROXY_IP":
        return
    if flow.request.pretty_host == "url1.website.com":
        flow.request.host = "url2.com"
        flow.request.scheme = "https"  # Change to "http" if needed
        flow.request.port = 443  # Change to 80 if using HTTP

def configure(updated):
    if "certs" in ctx.options:
        ctx.log.info(f"Using custom certificates from {ctx.options.certs}")

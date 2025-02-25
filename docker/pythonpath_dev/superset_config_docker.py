from superset.config import TALISMAN_CONFIG

GUEST_ROLE_NAME = 'EmbeddedViewer'
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    # "DASHBOARD_NATIVE_FILTERS_SET": True,
}
OVERRIDE_HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
TALISMAN_CONFIG = {
    "content_security_policy": None,
    "force_https": False,
    "strict_transport_security": False
}
WTF_CSRF_ENABLED = False
WTF_CSRF_EXEMPT_LIST = ["superset.views.core.guest_token"]

# TALISMAN_CONFIG = {
#     "content_security_policy": {
#         "base-uri": ["'self'"],
#         "default-src": ["'self'"],
#         "img-src": [
#             "'self'",
#             "blob:",
#             "data:",
#             "https://apachesuperset.gateway.scarf.sh",
#             "https://static.scarf.sh/",
#         ],
#         "worker-src": ["'self'", "blob:"],
#         "connect-src": [
#             "'self'",
#             "https://api.mapbox.com",
#             "https://events.mapbox.com",
#         ],
#         "object-src": "'none'",
#         "style-src": [
#             "'self'",
#             "'unsafe-inline'",
#         ],
#         "script-src": ["'self'", "'strict-dynamic'"],
#         "frame-ancestors": ["http://localhost:8080"]
#     },
#     "content_security_policy_nonce_in": ["script-src"],
#     "force_https": False,
#     "session_cookie_secure": False,
# }

import urllib.request
import sys

def check_health():
    try:
        # Pings the SentryNode API locally
        urllib.request.urlopen("http://localhost:8001/health", timeout=2)
        sys.exit(0)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    check_health()
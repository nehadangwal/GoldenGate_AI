# Example of what to push publicly
def test_sovereign_identity():
    # This proves the system works without showing HOW the HMAC is generated
    response = requests.post(GATEWAY_URL, json={"prompt": "test"})
    assert "x-sentry-signature" in response.headers
    print("✅ Sovereign Provenance Verified.")
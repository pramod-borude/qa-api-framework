def assert_status_code(resp, expected_code):
    assert resp.status_code == expected_code, f"Expected {expected_code}, got {resp.status_code}. Response: {resp.text}"

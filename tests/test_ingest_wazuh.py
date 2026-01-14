from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_ingest_wazuh():
    payload = {
        "rule_id": "5710",
        "agent": "agent-01"
    }

    res = client.post("/ingest/wazuh", json=payload)
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_ingest_wazuh_with_different_rule():
    payload = {
        "rule_id": "5719",
        "agent": "agent-02"
    }

    res = client.post("/ingest/wazuh", json=payload)
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_ingest_wazuh_missing_rule_id():
    payload = {
        "agent": "agent-01"
    }

    res = client.post("/ingest/wazuh", json=payload)
    assert res.status_code == 422  # Validation error


def test_ingest_wazuh_missing_agent():
    payload = {
        "rule_id": "5710"
    }

    res = client.post("/ingest/wazuh", json=payload)
    assert res.status_code == 422  # Validation error


def test_ingest_wazuh_empty_payload():
    payload = {}

    res = client.post("/ingest/wazuh", json=payload)
    assert res.status_code == 422  # Validation error
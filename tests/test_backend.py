from backend.app import app


def test_home():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert "Production Agentic Pipeline" in response.get_data(as_text=True)


def test_health():
    response = app.test_client().get("/health")

    assert response.status_code in [200, 503]


def test_chat_requires_message():
    response = app.test_client().post(
        "/api/chat",
        json={}
    )

    assert response.status_code == 400

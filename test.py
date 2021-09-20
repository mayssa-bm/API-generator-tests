from app import app


def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200



def test2():
    response = app.test_client().get("/")
    assert b"API Generator" in response.data
    assert b"API name" in response.data
    assert b"Generate API" in response.data
    assert b"Random API Generator" in response.data

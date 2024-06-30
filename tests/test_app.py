from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert (afirmar)


def test_read_root_html_deve_retornar_ok_e_ola_mundo_html():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/html')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.text == '<html><body><h1>Olá Mundo!</h1></body></html>'

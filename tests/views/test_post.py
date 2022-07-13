import pytest
from django.urls import reverse


@pytest.mark.django_db # para acessar o banco de dados
def test_post_view(client):
    url = reverse('home')
    reposnse = client.get(url)
    assert reposnse.status_code == 200
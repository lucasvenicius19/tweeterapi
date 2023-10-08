from src.services import _get_trends
from unitest import mock

def test_get_trends_with_success():
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = []
    _get_trends(woe_id=1000, api=mock_api)
    
    assert 1 == 1
    
# Implementando testes basicos
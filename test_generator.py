from generator import mock_llm_response

def test_mock_llm_response():
    story = 'Como usuário quero logar'
    response = mock_llm_response(story)
    assert 'Feature' in response
    assert story in response

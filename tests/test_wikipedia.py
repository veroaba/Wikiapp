from _pytest.config import argparsing
from wikiapp import wikipedia

def test_random_page_uses_given_language(mock_requests_get):
  wikipedia.random_page(language ="d")
  args, _ = mock_requests_get.call_args
  assert 'es.wikipedia.org' in args [0]

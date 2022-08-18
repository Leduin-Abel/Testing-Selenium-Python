
import pytest
from pages.result import searchEngineResultPage
from pages.search import searchEngineSearchPage

# This adds multiple searchs


@pytest.mark.parametrize('PHRASE', ['pizza', 'hamburger', 'chicken'])
def test_basic_searchEngineTest(browser, PHRASE):

    searchPage = searchEngineSearchPage(browser)
    resultPage = searchEngineResultPage(browser)

    # Given the page has loaded
    searchPage.load()

    # When the user searches <PHRASE>
    searchPage.search(PHRASE)

    # Then the search result title is <PHRASE>
    assert PHRASE in resultPage.title()

    # And the search result query is <PHRASE>
    assert PHRASE == resultPage.search_input_value()

    # And the search result links are related to <PHRASE>
    titles = resultPage.result_link_titles()
    for x in range(len(titles)):
        if (PHRASE in (str(titles[x]))):
            linksContainPhrase = True

    assert linksContainPhrase == True

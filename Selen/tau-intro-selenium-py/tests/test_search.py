

from pages.result import searchEngineResultPage
from pages.search import searchEngineSearchPage


def test_basic_searchEngineTest(browser):

    searchPage = searchEngineSearchPage(browser)
    resultPage = searchEngineResultPage(browser)

    PHRASE = "pizza"

    # Given the page has loaded
    searchPage.load()

    # When the user searches "pizza"
    searchPage.search(PHRASE)


    # Then the search result title is "pizza"
    assert PHRASE in resultPage.title()

    # And the search result query is "pizza"
    assert PHRASE == resultPage.search_input_value()

    # And the search result links are related to "pizza"
    for title in resultPage.result_link_titles():
        assert PHRASE.lower() in title.lower()

    raise Exception("Incompleto")

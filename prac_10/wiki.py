import wikipedia

search_phrase = input("Search phrase: ")
while search_phrase != '':
    try:
        searched_page = wikipedia.page(search_phrase)
        print(f"Title: {searched_page.title}\nSummary: {wikipedia.summary(search_phrase)}URL: {searched_page.url}\n")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Search phrase: ")
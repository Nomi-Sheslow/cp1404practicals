import wikipedia

search_phrase = str(input("Search: "))
while search_phrase != "":
    try:
        print(wikipedia.search(search_phrase))
        print(wikipedia.page(search_phrase))
        print(wikipedia.summary(search_phrase))
        print(wikipedia.page(search_phrase).url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = str(input("Search: "))

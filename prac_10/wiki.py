import wikipedia


def main():
    search_query = input("Enter page title: ")

    while search_query:
        try:
            # Get the Wikipedia page
            page = wikipedia.page(search_query, autosuggest=False)

            # Print the page details
            print(f"\n{page.title}")
            print(f"{page.summary}")
            print(f"{page.url}\n")

        except wikipedia.DisambiguationError as e:
            # Handle disambiguation error
            print(f"\nWe need a more specific title. Try one of the following, or a new search:\n{e.options}\n")

        except wikipedia.PageError:
            # Handle page error
            print(f"\nPage id \"{search_query}\" does not match any pages. Try another id!\n")

        except Exception as e:
            # Handle any other exceptions
            print(f"\nAn error occurred: {e}\n")

        # Prompt for another page title or search phrase
        search_query = input("Enter page title: ")


main()

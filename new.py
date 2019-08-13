from googlesearch import search

query = input()

for url in search(query, stop=20):
    print(url)

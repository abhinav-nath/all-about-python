import requests

def fetch_top_headlines(api_key, country_code='in'):
    news_api_url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}"

    response = requests.get(news_api_url)
    response = response.json()

    if response['status'] == 'ok':
        for article in response['articles']:
            title = article['title']
            description = article["description"]

            if title is not None:
                print("\n" + title + "\n")

            if description is not None:
                print(description + "\n")

            print("-" * 100)
    else:
        print("Failed to fetch top headlines. Please check your API key and try again.")

api_key = "<YOUR API KEY>"

fetch_top_headlines(api_key)

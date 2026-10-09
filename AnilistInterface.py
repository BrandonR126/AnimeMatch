import requests

# AniList GraphQL API endpoint
url = "https://graphql.anilist.co"

def GetTop10(genre=None, tag=None):
    # Define Variables for the Query
    variables = {
        "genre": genre,
        "tag": tag,
        "page": 1,
        "perPage": 10              # Get top 10 most popular
    }

    query = """
    query ($genre: String, $tag: String, $page: Int, $perPage: Int) {
        Page(page: $page, perPage: $perPage) {
            media(genre: $genre, tag: $tag, sort: POPULARITY_DESC) {
                title {
                    romaji
                    english
                }
                popularity
                averageScore
                genres
                tags {
                    name
                }
            }
        }
    }
    """

    # Make the HTTP POST Request
    response = requests.post(url, json={"query": query, "variables": variables})

    # Output the Results
    if response.status_code == 200:
        data = response.json()["data"]["Page"]["media"]
        print(f"Top Popular Anime with '{tag}' Tag:\n")
        for i, anime in enumerate(data, 1):
            title = anime["title"]["english"] or anime["title"]["romaji"] # return english title if available, otherwise romaji (could become a setting?)
            print(f"{i}. {title}")
            print(f"   Popularity: {anime['popularity']:,} members | Score: {anime['averageScore']}/100")
            print(f"   Genres: {', '.join(anime['genres'])}")
            print(f"   Tags: {', '.join([tag['name'] for tag in anime['tags']])}\n")
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")

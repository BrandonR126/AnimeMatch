import requests

# AniList GraphQL API endpoint
url = "https://graphql.anilist.co"

def GetTopAnime(genreIn=None, tagIn=None, genreNotIn=None, tagNotIn=None, results=10):
    # Define Variables for the Query
    variables = {
        "genreIn": genreIn,
        "tagIn": tagIn,
        "genreNotIn": genreNotIn,
        "tagNotIn": tagNotIn,
        "page": 1,
        "perPage": results              # Get top 10 most popular
    }

    query = """
    query ($genreIn: [String], $tagIn: [String], $genreNotIn: [String], $tagNotIn: [String], $page: Int, $perPage: Int) {
        Page(page: $page, perPage: $perPage) {
            media(genre_in: $genreIn, tag_in: $tagIn, genre_not_in: $genreNotIn, tag_not_in: $tagNotIn, sort: POPULARITY_DESC) {
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
        for i, anime in enumerate(data, 1):
            title = anime["title"]["english"] or anime["title"]["romaji"] # return english title if available, otherwise romaji (could become a setting?)
            print(f"{i}. {title}")
            print(f"   Popularity: {anime['popularity']:,} members | Score: {anime['averageScore']}/100")
            print(f"   Genres: {', '.join(anime['genres'])}")
            print(f"   Tags: {', '.join([tag['name'] for tag in anime['tags']])}\n")
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")

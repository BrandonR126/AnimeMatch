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
    query ( $tagIn: [String], $genreNotIn: [String], $tagNotIn: [String], $page: Int, $perPage: Int) {
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
            # NOTE: This is a temporary solution to output results. should be moved into dedicated function for UI in the future.
            title = anime["title"]["english"] or anime["title"]["romaji"] # return english title if available, otherwise romaji (could become a setting?)
            print(f"{i}. {title}")
            print(f"   Popularity: {anime['popularity']:,} members | Score: {anime['averageScore']}/100")
            print(f"   Genres: {', '.join(anime['genres'])}")
            print(f"   Tags: {', '.join([tag['name'] for tag in anime['tags']])}\n")

            return anime
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")


def GetAnimeFromTitle(title):
    # Define Variables for the Query
    variables = {
        "title": title
    }

    query = """
    query ($title: String) {
        Media(search: $title, type: ANIME) {
            title {
                romaji
                english
            }
            popularity
            averageScore
            genres
            tags {
                name
                rank
            }
        }
    }
    """

    # Make the HTTP POST Request
    response = requests.post(url, json={"query": query, "variables": variables})

    # Output the Results
    if response.status_code == 200:
        anime = response.json()["data"]["Media"]

        # NOTE: This is a temporary solution to output results. should be moved into dedicated function for UI in the future.
        title = anime["title"]["english"] or anime["title"]["romaji"]
        print(f"Title: {title}")
        print(f"Popularity: {anime['popularity']:,} members | Score: {anime['averageScore']}/100")
        print(f"Genres: {', '.join(anime['genres'])}")
        print(f"Tags: {', '.join([tag['name'] for tag in anime['tags']])}\n")

        return anime
    
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")
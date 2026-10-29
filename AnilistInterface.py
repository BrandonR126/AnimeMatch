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
        "perPage": results,
    }

    query = """
    query ( $genreIn: [String],$tagIn: [String], $genreNotIn: [String], $tagNotIn: [String], $page: Int, $perPage: Int) {
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
                    rank
                }
            }
        }
    }
    """

    # Make the HTTP POST Request
    response = requests.post(url, json={"query": query, "variables": variables})

    # Output the Results
    if response.status_code == 200:
        return response.json()["data"]["Page"]["media"]
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")



def GetAnimeFromTitle(title):
    # Define Variables for the Query
    variables = {
        "title": title,
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
        return response.json()["data"]["Media"]
    else:
        print(f"Failed with status code {response.status_code}: {response.text}")

def FormatAnime(anime): 
    if anime is None:
        return "No anime found."

    title = anime["title"]["english"] or anime["title"]["romaji"]
    score = anime["averageScore"]
    popularity = anime["popularity"]
    genres = ", ".join(anime["genres"])
    tags = ", ".join([tag["name"] for tag in anime["tags"]])

    text = title + "\n"
    text += "   Score: " + str(score) + "/100 | Popularity: " + str(popularity) + "\n"
    text += "   Genres: " + genres + "\n"
    text += "   Tags: " + tags + "\n"
    return text
import requests

url = "https://graphql.anilist.co"


def GetTopAnime(genreIn=None, tagIn=None, results=10):
    # Make sure genre and tag are lists
    if type(genreIn) == str:
        genreIn = [genreIn]
    if type(tagIn) == str:
        tagIn = [tagIn]

    variables = {
        "genreIn": genreIn,
        "tagIn": tagIn,
        "page": 1,
        "perPage": results
    }

    query = """
    query ($genreIn: [String], $tagIn: [String], $page: Int, $perPage: Int) {
        Page(page: $page, perPage: $perPage) {
            media(genre_in: $genreIn, tag_in: $tagIn, sort: POPULARITY_DESC, type: ANIME) {
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

    response = requests.post(url, json={"query": query, "variables": variables})

    if response.status_code == 200:
        data = response.json()["data"]["Page"]["media"]
        return data
    else:
        print("API Error")
        return []


def GetAnimeFromTitle(title):
    variables = {"title": title}

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
            }
        }
    }
    """

    response = requests.post(url, json={"query": query, "variables": variables})

    if response.status_code == 200:
        anime = response.json()["data"]["Media"]
        return anime
    else:
        print("API Error")
        return None


def format_anime(anime):
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
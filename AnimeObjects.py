class Anime:
    def __init__(self, title, score, popularity, genres, tags):
        self.title = title
        self.score = score
        self.popularity = popularity
        self.genres = genres          # list of strings
        self.tags = tags              # list of strings

    def __str__(self):
        # This is what prints when you do print(anime)
        text = self.title + "\n"
        text += "   Score: " + str(self.score) + "/100 | Popularity: " + str(self.popularity) + "\n"
        text += "   Genres: " + ", ".join(self.genres) + "\n"
        text += "   Tags: " + ", ".join(self.tags) + "\n"
        return text


def makeAnimeFromDict(data):
    """
    Takes the dictionary that comes from the API
    and turns it into an Anime object.
    """
    if data is None:
        return None

    # Get the title (English if available, otherwise romaji)
    title = data["title"].get("english") or data["title"].get("romaji") or "Unknown"

    score = data.get("averageScore") or 0
    popularity = data.get("popularity") or 0
    genres = data.get("genres") or []

    # Tags come as a list of dictionaries, so we only keep the name
    tags = []
    for tag in data.get("tags") or []:
        tags.append(tag["name"])

    return Anime(title, score, popularity, genres, tags)
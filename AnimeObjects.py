class Anime:
    def __init__(self, title, score, popularity, genres, tags):
        self.title = title
        self.score = score
        self.popularity = popularity
        self.genres = genres          # list of strings
        self.tags = tags              # list of strings

    def __str__(self):
        """
        This is what appears when we print the anime.
        It shows ALL the information (not just the title).
        """
        text = self.title + "\n"
        text += "   Score: " + str(self.score) + "/100 | Popularity: " + str(self.popularity) + "\n"
        text += "   Genres: " + ", ".join(self.genres) + "\n"
        text += "   Tags: " + ", ".join(self.tags) + "\n"
        return text

    def to_dict(self):
        """
        Returns a normal dictionary if someone prefers dictionaries
        instead of the object.
        """
        return {
            "title": self.title,
            "score": self.score,
            "popularity": self.popularity,
            "genres": self.genres,
            "tags": self.tags
        }


def make_anime(data):
    """
    Takes the dictionary that comes from the AniList API
    and turns it into an Anime object.
    """
    if data is None:
        return None

    # Prefer English title, otherwise use the Japanese (romaji) title
    title = data["title"].get("english") or data["title"].get("romaji") or "Unknown"

    score = data.get("averageScore")
    if score is None:
        score = "N/A"

    popularity = data.get("popularity") or 0
    genres = data.get("genres") or []

    tags = {}
    for tag in data.get("tags") or []:
        name = tag.get("name")
        rank = tag.get("rank", 0)
        if name:
            tags[name] = rank

    return Anime(title, score, popularity, genres, tags)
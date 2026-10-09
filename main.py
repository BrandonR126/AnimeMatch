import AnilistInterface

def main():
    # Example
    tags = "Afterlife"
    genres = "Mystery", "Psychological", "Thriller"
    AnilistInterface.GetTopAnime(tagIn=tags, results=20)


main()
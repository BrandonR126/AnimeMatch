import AnilistInterface

def main():
    # Example of GetTopAnime function usage
    # tags = "Afterlife"
    # genres = "Mystery", "Psychological", "Thriller"
    # AnilistInterface.GetTopAnime(tagIn=tags, results=20)




    # Example of GetAnimeFromTitle function usage
    title = "Oshi no Ko"

    result = AnilistInterface.GetAnimeFromTitle(title)
    tags = result["tags"]
    # example of filtering tags based on rank (ranked out of 100 based on user voting)
    for tag in tags:
        if(tag["rank"] < 65):
            result["tags"].remove(tag)
        else:
            print(f"{tag['name']} - {tag['rank']}")

main()
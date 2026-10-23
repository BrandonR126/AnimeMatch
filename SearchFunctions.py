import AnilistInterface as anilist
import AnimeManager as manager
import AnimeObjects as aniObjects

def ByGenre(genre=None):
    animeList = anilist.GetTopAnime(genreIn=genre, results=5)
    formatedAnime = []
    for anime in animeList:
        formatedAnime.append(aniObjects.make_anime(anime))
    return formatedAnime


def BySimilarFromTitle(title=None):
    anime = anilist.GetAnimeFromTitle(title)

    # convert anime into obj and get tags
    anime_obj = aniObjects.make_anime(anime)
    anime_obj.tags = manager.SortTagsByRank(anime_obj.tags)
    tagRank = anime_obj.tags[0]["rank"]
    anime_obj.tags = manager.FilterTagsByRank(anime_obj.tags, tagRank - 5)  # Filter tags to only include those within 10 ranks of the highest rank

    tagNames = [tag["name"] for tag in anime_obj.tags]
    genreNames = anime_obj.genres
    # find similar anime, convert into objects, and exclude the searched anime from the results
    similarAnime = anilist.GetTopAnime(genreIn = genreNames, results=10) # not using tags for now since the tags seem to really limit what is returned. could be a setting in the future to use tags or not.
    similarAnimeObj = []
    for anime in similarAnime:
        anime = aniObjects.make_anime(anime)
        anime.tags = manager.FilterTagsByRank(anime.tags, 75)
        similarAnimeObj.append(anime)
    similarAnimeObj = manager.ExcludeSearchedAnime(similarAnimeObj, anime_obj)

    similarAnimeObj = manager.RankAnimeByStats(similarAnimeObj)

    return similarAnimeObj[:5]  # Return top 5 results



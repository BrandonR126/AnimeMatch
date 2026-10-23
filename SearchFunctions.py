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
    anime_obj.tags = manager.FilterTagsByRank(anime_obj.tags, 70)
    anime_obj.tags = manager.SortTagsByRank(anime_obj.tags)

    # find similar anime, convert into objects, and exclude the searched anime from the results
    similarAnime = anilist.GetTopAnime(tagIn=anime_obj.tags[0], genreIn=anime_obj.genres[0], results=10)
    similarAnimeObj = []
    for anime in similarAnime:
        anime = aniObjects.make_anime(anime)
        anime.tags = manager.FilterTagsByRank(anime.tags, 75)
        similarAnimeObj.append(anime)
    similarAnimeObj = manager.ExcludeSearchedAnime(similarAnimeObj, anime_obj)

    similarAnimeObj = manager.RankAnimeByStats(similarAnimeObj)

    return similarAnimeObj[:5]  # Return top 5 results



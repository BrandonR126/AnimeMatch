import re
import time

import AnilistInterface as anilist
import AnimeManager as manager
import AnimeObjects as aniObjects
import animeCache as animeCache

def ByGenre(genre=None):
    animeList = anilist.GetTopAnime(genreIn=genre, results=5)
    formatedAnime = []
    for anime in animeList:
        formatedAnime.append(aniObjects.make_anime(anime))
    return formatedAnime

def ByFilter(genres=None, tags=None, genresNotIn=None, tagsNotIn=None):
    animeList = anilist.GetTopAnime(genreIn=genres, tagIn=tags, genreNotIn=genresNotIn, tagNotIn=tagsNotIn)
    formatedAnime = []
    for anime in animeList:
        formatedAnime.append(aniObjects.make_anime(anime))
    return formatedAnime


def BySimilarFromTitle(title=None):
    anime = anilist.GetAnimeFromTitle(title)
    if anime is None:
        return None

    # convert anime into obj and get tags
    anime_obj = aniObjects.make_anime(anime)
    anime_obj.tags = manager.SortTagsByRank(anime_obj.tags)
    tagRank = anime_obj.tags[0]["rank"]
    anime_obj.tags = manager.FilterTagsByRank(anime_obj.tags, tagRank - 10)

    genreNames = anime_obj.genres
    # find similar anime, convert into objects, and exclude the searched anime from the results
    similarAnime = anilist.GetTopAnime(genreIn = genreNames, results=10)
    similarAnimeObj = []
    for anime in similarAnime:
        anime = aniObjects.make_anime(anime)
        anime.tags = manager.FilterTagsByRank(anime.tags, 75)
        similarAnimeObj.append(anime)
    similarAnimeObj = manager.ExcludeSearchedAnime(similarAnimeObj, anime_obj)

    similarAnimeObj = manager.RankAnimeByStats(similarAnimeObj, anime_obj)

    return similarAnimeObj

def SearchByTitle(title):
    cache = animeCache.load_cache()
    if title in cache:
        anime = cache[title]
    else:
        anime = anilist.GetAnimeFromTitle(title)
        if anime is None:
            return None
        cache[title] = anime
        animeCache.save_cache(cache) # update cache with the newly fetched anime data

    return aniObjects.make_anime(anime)

def GetListFromTextEntry(entry): 
    string = entry.get().strip()
    if(string == ""):
        return None

    items = [item.strip() for item in re.split(r'[,;]+', string) if item.strip()]
    
    return items if items else None
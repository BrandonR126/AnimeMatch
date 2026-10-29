import re
import time

import AnilistInterface as anilist
import AnimeManager as manager
import AnimeObjects as aniObjects

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

    time.sleep(0.5) # avoid 429 too many requests errors

    # convert anime into obj and get tags
    anime_obj = aniObjects.make_anime(anime)
    anime_obj.tags = manager.SortTagsByRank(anime_obj.tags)
    tagRank = anime_obj.tags[0]["rank"]
    anime_obj.tags = manager.FilterTagsByRank(anime_obj.tags, tagRank - 10)

    tagNames = [tag["name"] for tag in anime_obj.tags]
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


def GetListFromTextEntry(entry): 
    string = entry.get().strip()
    if(string == ""):
        return None

    items = [item.strip() for item in re.split(r'[,;]+', string) if item.strip()]
    
    return items if items else None
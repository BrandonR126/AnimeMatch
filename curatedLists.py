import animeCache
import AnilistInterface as anilist
import AnimeObjects as aniObjects

# Lists + anime names here:
sabrinaList = [
    "Jojo's Bizarre Adventure",
    "A Silent Voice",
    "Erased",
    "Fullmetal Alchemist: Brotherhood",
    "Chainsaw Man",
]
brandonList = [
    "Grave of the Fireflies",
    "Sousou no Frieren",
    "Attack on Titan",
    "[Oshi No Ko]",
    "Chainsaw Man",
]
alexcsanderList = [
    "Mushishi",
    "Ping Pong the Animation",
    "Kaiba",
    "Odd Taxi",
    "The Tatami Galaxy",
]

beginnerList = [
    "Spy x Family",
    "Fullmetal Alchemist: Brotherhood",
    "Death Note",
    "Spirited Away",
    "My Hero Academia",
]

allLists = {
    "Sabrina's List": sabrinaList,
    "Brandon's List": brandonList,
    "Alexcsander's List": alexcsanderList,
    "Beginner's List": beginnerList,
}

# NOTE: useCache and useAPI are primarily for testing purposes. In production, both should be set to True. Other functions using cache
# do NOT need to have these parameters. We only need one for testing purposes.
# Should prob make a function just for testing cache, but this works for now.
def GetList(animeList, useCache=True, useAPI = True): # set useCache to False to ignore cache and fetch fresh data, set useAPI to False to only use cache
    if not animeList:
        return []

    cache = animeCache.load_cache()
    anime_objects = []
    cache_updated = False

    for anime_name in animeList:
        if useCache and anime_name in cache:
            anime_objects.append(aniObjects.make_anime(cache[anime_name]))
        elif useAPI:
            anime_data = anilist.GetAnimeFromTitle(anime_name)
            if anime_data:
                anime_obj = aniObjects.make_anime(anime_data)
                anime_objects.append(anime_obj)

                if(useCache):
                    cache[anime_name] = anime_data # save cache in memory
                    cache_updated = True

    if cache_updated:
        animeCache.save_cache(cache) # save cache to file

    return anime_objects



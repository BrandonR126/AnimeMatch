def FilterTagsByRank(tagList, minRank):
    return [tag for tag in tagList if tag.get("rank", 0) >= minRank]

def SortTagsByRank(tagList, descending=True):
    return sorted(tagList, key=lambda x: x.get("rank", 0), reverse=descending)

def FilterByAttribute(items, attribute_name, minScore):
    return [item for item in items if getattr(item, attribute_name, 0) >= minScore]

def SortByAttribute(animeList, attribute_name, descending=True):
    return sorted(animeList, key=lambda x: getattr(x, attribute_name, 0), reverse=descending)

def ExcludeSearchedAnime(anime_list, searched_anime):
    """
    Exclude the searched anime from the list of similar anime.
    """
    if(anime_list is None or searched_anime is None):
        return anime_list

    return [anime for anime in anime_list if anime.title != searched_anime.title]

def RankAnimeByStats(anime_list, searched_anime):
    """
    Rank the anime list based on a combination of score and popularity.
    This is a simple ranking algorithm that gives equal weight to both attributes.
    """
    if anime_list is None:
        return []

    # Calculate a combined score for each anime
    for anime in anime_list:
        tagScore = 0
        for searchedTag in searched_anime.tags:
            for animeTag in anime.tags:
                if searchedTag["name"] == animeTag["name"]:
                    tagScore += 10

        score = getattr(anime, 'score', 0) or 0
        popularity = getattr(anime, 'popularity', 0) or 0
        # Normalize score and popularity to a scale of 0-100
        normalized_score = (score / 100) * 50  # Score contributes up to 50 points
        normalized_popularity = (popularity / max(1, max(getattr(a, 'popularity', 0) for a in anime_list))) * 50  # Popularity contributes up to 50 points
        anime.combined_score = normalized_score + normalized_popularity + tagScore

    # Sort the list based on the combined score in descending order
    return sorted(anime_list, key=lambda x: getattr(x, 'combined_score', 0), reverse=True)

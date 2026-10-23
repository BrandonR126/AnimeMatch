def FilterTagsByRank(tagList, minRank):
    return [tag for tag in tagList if tag.get("rank", 0) >= minRank]

def SortTagsByRank(tagList, descending=True):
    return sorted(tagList, key=lambda x: x.get("rank", 0), reverse=descending)

def FilterByAttribute(items, attribute_name, minScore):
    return [item for item in items if getattr(item, attribute_name, 0) >= minScore]

def SortByAttribute(animeList, attribute_name, descending=True):
    return sorted(animeList, key=lambda x: getattr(x, attribute_name, 0), reverse=descending)
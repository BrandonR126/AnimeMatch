def FilterTagsByRank(tags, minRank):
    filteredTags = [tag for tag in tags if tag["rank"] >= minRank]
    return filteredTags
import AnilistInterface as anilist

print("AnimeMatch Console Demo")

print("Top Action anime:")
results = anilist.GetTopAnime(genreIn="Action", results=3)

for i, anime in enumerate(results, 1):
    print(str(i) + ". " + anilist.format_anime(anime))

print("-" * 40)

print("Search for 'Oshi no Ko':")
anime = anilist.GetAnimeFromTitle("Oshi no Ko")
print(anilist.format_anime(anime))
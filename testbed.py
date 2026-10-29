import AnilistInterface as anilist
import AnimeManager as manager
import AnimeObjects as anime


pass_count = 0
fail_count = 0
error_count = 0

# test classes
genres1 = [
        {"name": "Action", "rank": 86},
        {"name": "Comedy", "rank": 76},
        {"name": "Drama", "rank": 75},
        {"name": "Fantasy", "rank": 28}
]
tags1 = [
        {"name": "Afterlife", "rank": 85},
        {"name": "Supernatural", "rank": 80},
        {"name": "Psychological", "rank": 60},
        {"name": "Detective", "rank": 50},
]
genres2 = [
        {"name": "Action", "rank": 90},
        {"name": "Mystery", "rank": 70},
        {"name": "Thriller", "rank": 60}
]
tags2 = [
        {"name": "Detective", "rank": 90},
        {"name": "Psychological", "rank": 80}
]
genres3 = [
        {"name": "Action", "rank": 70},
        {"name": "Adventure", "rank": 60},
        {"name": "Sci-Fi", "rank": 50}
]
tags3 = [
        {"name": "Space", "rank": 70},
        {"name": "Mecha", "rank": 60}
]
TestAnime1 = anime.Anime("Death Note", 80, 80, genres1, tags1)
TestAnime2 = anime.Anime("Attack on Titan", 90, 90, genres2, tags2)
TestAnime3 = anime.Anime("Cowboy Bebop", 70, 70, genres3, tags3)
anime_list = [TestAnime1, TestAnime2, TestAnime3]


def run_test(name, test_func):
    global pass_count, fail_count, error_count
    print("\n" + "=" * 40)
    print("TEST: " + name)
    print("-" * 40)
    try:
        result = test_func()
        if result:
            print("→ PASS")
            pass_count +=1
        else:
            print("→ FAIL")
            fail_count += 1
    except Exception as e:
        print("→ ERROR: " + str(e))
        error_count += 1
    print("=" * 40)


def test_genre():
    data = anilist.GetTopAnime(genreIn="Action", results=3)
    print("Got " + str(len(data)) + " anime")
    if len(data) > 0:
        print(anilist.FormatAnime(data[0]))
    return len(data) > 0


def test_tag():
    data = anilist.GetTopAnime(tagIn="Afterlife", results=3)
    print("Got " + str(len(data)) + " anime")
    if len(data) > 0:
        print(anilist.FormatAnime(data[0]))
    return len(data) > 0


def test_title():
    anime = anilist.GetAnimeFromTitle("Death Note")
    if anime is not None:
        print(anilist.FormatAnime(anime))
        return True
    return False


def test_no_filters():
    data = anilist.GetTopAnime(results=3)
    print("Got " + str(len(data)) + " anime")
    if len(data) > 0:
        print(anilist.FormatAnime(data[0]))
    return len(data) > 0

def test_filter_tags_by_rank():
    min_rank = 60
    filtered_tags = manager.FilterTagsByRank(TestAnime1.tags, min_rank)
    print("Filtered Tags:", filtered_tags)
    if len(filtered_tags) == 3:
        return True
    else: return False

def test_sort_tags_by_rank():
    sorted_tags = manager.SortTagsByRank(TestAnime1.tags)
    print("Sorted Tags:", sorted_tags)
    if sorted_tags[0]["rank"] == 85 and sorted_tags[3]["rank"] == 50:
        return True
    else: return False

def test_filter_by_attribute():
    min_score = 80
    filtered_items = manager.FilterByAttribute(anime_list, "score", min_score)
    print("Filtered Items:", filtered_items)
    if len(filtered_items) == 2:
        return True
    else: return False

def test_sort_by_attribute():
    sorted_anime = manager.SortByAttribute(anime_list, "score")
    print("Sorted Anime:", sorted_anime)
    if sorted_anime[0].score == 90 and sorted_anime[2].score == 70:
        return True
    else: return False

def test_exclude_searched_anime():
    searched_anime = TestAnime1
    filtered_list = manager.ExcludeSearchedAnime(anime_list, searched_anime)
    print("Filtered List:", filtered_list)
    if searched_anime not in filtered_list and len(filtered_list) == 2:
        return True
    else: return False

print("AnimeMatch API Testbed")
print("Running tests...")

run_test("1. Search by Genre", test_genre)
run_test("2. Search by Tag", test_tag)
run_test("3. Search by Title", test_title)
run_test("4. No filters", test_no_filters)
run_test("5. Filter Tags by Rank", test_filter_tags_by_rank)
run_test("6. Sort Tags by Rank", test_sort_tags_by_rank)
run_test("7. Filter by Attribute", test_filter_by_attribute)
run_test("8. Sort by Attribute", test_sort_by_attribute)
run_test("9. Exclude Searched Anime", test_exclude_searched_anime)

print("\nAll tests finished.")
print("Passed: " + str(pass_count))
print("Failed: " + str(fail_count))
print("Errors: " + str(error_count))
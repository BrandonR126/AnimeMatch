import AnilistInterface as anilist
import AnimeManager as manager

def run_test(name, test_func):
    print("\n" + "=" * 40)
    print("TEST: " + name)
    print("-" * 40)
    try:
        result = test_func()
        if result:
            print("→ PASS")
        else:
            print("→ FAIL")
    except Exception as e:
        print("→ ERROR: " + str(e))
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
    tags = [
        {"name": "Action", "rank": 86},
        {"name": "Comedy", "rank": 76},
        {"name": "Drama", "rank": 75},
        {"name": "Fantasy", "rank": 28}
    ]
    min_rank = 60
    filtered_tags = manager.FilterTagsByRank(tags, min_rank)
    print("Filtered Tags:", filtered_tags)
    if len(filtered_tags) == 3:
        return True
    else: return False

print("AnimeMatch API Testbed")
print("Running tests...")

run_test("1. Search by Genre", test_genre)
run_test("2. Search by Tag", test_tag)
run_test("3. Search by Title", test_title)
run_test("4. No filters", test_no_filters)
run_test("5. Filter Tags by Rank", test_filter_tags_by_rank)

print("\nAll tests finished.")
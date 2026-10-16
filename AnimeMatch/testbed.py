import AnilistInterface as anilist


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
        print(anilist.format_anime(data[0]))
    return len(data) > 0


def test_tag():
    data = anilist.GetTopAnime(tagIn="Afterlife", results=3)
    print("Got " + str(len(data)) + " anime")
    if len(data) > 0:
        print(anilist.format_anime(data[0]))
    return len(data) > 0


def test_title():
    anime = anilist.GetAnimeFromTitle("Death Note")
    if anime is not None:
        print(anilist.format_anime(anime))
        return True
    return False


def test_no_filters():
    data = anilist.GetTopAnime(results=3)
    print("Got " + str(len(data)) + " anime")
    if len(data) > 0:
        print(anilist.format_anime(data[0]))
    return len(data) > 0


print("AnimeMatch API Testbed")
print("Running tests...")

run_test("1. Search by Genre", test_genre)
run_test("2. Search by Tag", test_tag)
run_test("3. Search by Title", test_title)
run_test("4. No filters", test_no_filters)

print("\nAll tests finished.")
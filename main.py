import AnilistInterface

def main():
    # Example usage of the get_top_anime_by_tag function
    tag = "Desert"
    genre = "Action"  # You can change this to any tag you want to search for
    AnilistInterface.GetTop10(tag=tag, genre=genre)


main()
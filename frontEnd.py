import tkinter as tk
from tkinter import messagebox
import AnimeObjects as aniObjects
import SearchFunctions as search


# Widgets are created in build_window() and used by the search buttons.
root = None
genre_entry = None
tag_entry = None
exclude_genre_entry = None
exclude_tag_entry = None
title_entry = None
results_box = None
search_buttons = []


def SetBusy(is_busy):
    """
    Turn the search buttons off while AniList is working.
    A second click during that pause would start another search on top of the first one.
    """
    if is_busy:
        state = tk.DISABLED
    else:
        state = tk.NORMAL

    for button in search_buttons:
        button.config(state=state)




def ShowSearching(message):
    """Let the user see that a search is running. The window pauses until AniList answers."""
    SetBusy(True)
    WriteResults(message + "\n")
    root.update()

def WriteResults(text):
    """Put text in the results box and scroll back to the first line."""
    results_box.insert(tk.END, text + "\n")


def ShowResults(anime_list, note="", empty_message="No matching anime found."):
    """Replace the results box with the recommendation text."""
    try:
        for anime in anime_list:
            WriteResults(str(anime))
    except:
        WriteResults(note)
    
    finally:
        SetBusy(False)

def SearchByFilter():
    genres = search.GetListFromTextEntry(genre_entry)
    tags = search.GetListFromTextEntry(tag_entry)
    genres_not_in = search.GetListFromTextEntry(exclude_genre_entry)
    tags_not_in = search.GetListFromTextEntry(exclude_tag_entry)

    ShowSearching("Searching for anime...")
    try:
        anime_list = search.ByFilter(
            genres=genres,
            tags=tags,
            genresNotIn=genres_not_in,
            tagsNotIn=tags_not_in,
        )

    except Exception as error:
        print("Search failed: " + str(error))
        ShowResults(None, note="Something went wrong: " + str(error))
        return

    ShowResults(anime_list)


def SearchBySimilarFromTitle():
    title = title_entry.get().strip()

    if title == "":
        messagebox.showwarning("Missing input", "Please type an anime title")
        return

    ShowSearching("Searching for anime similar to: " + title + "...")

    try:
        similar_anime = search.BySimilarFromTitle(title=title)
    except Exception as error:
        print("Search failed: " + str(error))
        ShowResults(None, note="Something went wrong: " + str(error))
        return

    note = 'Similar to "' + title + '".'

    ShowResults(similar_anime, note=note, empty_message="No similar anime found.")


def build_window():
    """Create the AnimeMatch window and its widgets. Does not start the event loop."""
    global root
    global genre_entry, tag_entry, exclude_genre_entry, exclude_tag_entry, title_entry, results_box, search_buttons

    if root is not None:
        try:
            if root.winfo_exists():
                root.destroy()
        except tk.TclError:
            pass

    root = tk.Tk()
    root.title("AnimeMatch")
    root.geometry("680x720")
    root.minsize(640, 560)

    # Title
    tk.Label(root, text="AnimeMatch", font=("Arial", 18, "bold")).pack(pady=10)

    # genre
    genre_frame = tk.Frame(root)
    genre_frame.pack(pady=5)

    tk.Label(genre_frame, text="Genre:").pack(side=tk.LEFT)
    genre_entry = tk.Entry(genre_frame, width=25)
    genre_entry.pack(side=tk.LEFT, padx=5)

    # tag
    tag_frame = tk.Frame(root)
    tag_frame.pack(pady=5)

    tk.Label(tag_frame, text="Tag:").pack(side=tk.LEFT)
    tag_entry = tk.Entry(tag_frame, width=25)
    tag_entry.pack(side=tk.LEFT, padx=5)

    # exclude genre
    exclude_genre_frame = tk.Frame(root)
    exclude_genre_frame.pack(pady=5)

    tk.Label(exclude_genre_frame, text="Exclude Genre:").pack(side=tk.LEFT)
    exclude_genre_entry = tk.Entry(exclude_genre_frame, width=25)
    exclude_genre_entry.pack(side=tk.RIGHT, padx=5)

    # exclude tag
    exclude_tag_frame = tk.Frame(root)
    exclude_tag_frame.pack(pady=5)

    tk.Label(exclude_tag_frame, text="Exclude Tag:").pack(side=tk.LEFT)
    exclude_tag_entry = tk.Entry(exclude_tag_frame, width=25)
    exclude_tag_entry.pack(side=tk.RIGHT, padx=5)

    # search button
    filtered_search_frame = tk.Frame(root)
    filtered_search_frame.pack(pady=5)
    filter_button = tk.Button(filtered_search_frame, text="Search with Filters", command=SearchByFilter)
    filter_button.pack(side=tk.LEFT)

    # Title search
    title_frame = tk.Frame(root)
    title_frame.pack(pady=15)

    tk.Label(title_frame, text="Search by Similar to Title: ").pack(side=tk.LEFT)
    title_entry = tk.Entry(title_frame, width=25)
    title_entry.pack(side=tk.LEFT, padx=5)
    title_entry.insert(0, "Oshi no Ko")

    title_button = tk.Button(title_frame, text="Search by Similar to Title", command=SearchBySimilarFromTitle)
    title_button.pack(side=tk.LEFT)
    search_buttons = [filter_button, title_button]

    # Results area (simple Text + Scrollbar)
    tk.Label(root, text="Results:", font=("Arial", 12)).pack(pady=(15, 0))

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    results_box = tk.Text(frame, width=70, height=16, wrap=tk.WORD, font=("Arial", 10), yscrollcommand=scrollbar.set)
    results_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=results_box.yview)

    return root


def start_app():
    """Open the window and wait for button clicks. main.py calls this."""
    build_window()
    root.mainloop()


start_app()
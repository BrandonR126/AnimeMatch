import tkinter as tk
from tkinter import messagebox
import SearchFunctions as search

def SearchByFilter():
    genres = search.GetListFromTextEntry(genre_entry)
    tags = search.GetListFromTextEntry(tag_entry)
    genres_not_in = search.GetListFromTextEntry(exclude_genre_entry)
    tags_not_in = search.GetListFromTextEntry(exclude_tag_entry)

    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, "Searching for anime...\n\n")
    root.update()

    anime_list = search.ByFilter(genres=genres, tags=tags, genresNotIn=genres_not_in, tagsNotIn=tags_not_in)

    if not anime_list:
        results_box.insert(tk.END, "No results found.\n")
        return

    for anime in anime_list:
        results_box.insert(tk.END, str(anime) + "\n")


def SearchBySimilarFromTitle():
    title = title_entry.get().strip()

    if title == "":
        messagebox.showwarning("Missing input", "Please type an anime title")
        return

    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, "Searching for similar animes to: " + title + "...\n\n")
    root.update()

    similarAnimeObj = search.BySimilarFromTitle(title=title)

    if not similarAnimeObj:
        results_box.insert(tk.END, "No similar animes found.\n")
        return

    for anime in similarAnimeObj:
        results_box.insert(tk.END, str(anime) + "\n")

# Create the window
root = tk.Tk()
root.title("AnimeMatch")
root.geometry("600x500")

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
tk.Button(filtered_search_frame, text="Search with Filters", command=SearchByFilter).pack(side=tk.LEFT)

# Title search
title_frame = tk.Frame(root)
title_frame.pack(pady=25)

tk.Label(title_frame, text="Search by Similar to Title: ").pack(side=tk.LEFT)
title_entry = tk.Entry(title_frame, width=25)
title_entry.pack(side=tk.LEFT, padx=5)
title_entry.insert(0, "Oshi no Ko")

tk.Button(title_frame, text="Search by Similar to Title", command=SearchBySimilarFromTitle).pack(side=tk.LEFT)

# Results area (simple Text + Scrollbar)
tk.Label(root, text="Results:", font=("Arial", 12)).pack(pady=(15, 0))

frame = tk.Frame(root)
frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_box = tk.Text(frame, width=70, height=18, yscrollcommand=scrollbar.set)
results_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=results_box.yview)

root.mainloop()
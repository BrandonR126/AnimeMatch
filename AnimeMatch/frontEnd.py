import tkinter as tk
from tkinter import messagebox
import AnilistInterface as anilist


def search_by_genre():
    genre = genre_entry.get().strip()

    if genre == "":
        messagebox.showwarning("Missing input", "Please type a genre")
        return

    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, "Searching for genre: " + genre + "...\n\n")
    root.update()

    anime_list = anilist.GetTopAnime(genreIn=genre, results=5)

    if len(anime_list) == 0:
        results_box.insert(tk.END, "No results found.\n")
        return

    for i, anime in enumerate(anime_list, 1):
        results_box.insert(tk.END, str(i) + ". " + anilist.format_anime(anime) + "\n")


def search_by_title():
    title = title_entry.get().strip()

    if title == "":
        messagebox.showwarning("Missing input", "Please type an anime title")
        return

    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, "Searching for title: " + title + "...\n\n")
    root.update()

    anime = anilist.GetAnimeFromTitle(title)

    if anime is None:
        results_box.insert(tk.END, "No anime found.\n")
        return

    results_box.insert(tk.END, anilist.format_anime(anime))


# Create the window
root = tk.Tk()
root.title("AnimeMatch")
root.geometry("600x500")

# Title
tk.Label(root, text="AnimeMatch", font=("Arial", 18, "bold")).pack(pady=10)

# Genre search
genre_frame = tk.Frame(root)
genre_frame.pack(pady=5)

tk.Label(genre_frame, text="Genre:").pack(side=tk.LEFT)
genre_entry = tk.Entry(genre_frame, width=25)
genre_entry.pack(side=tk.LEFT, padx=5)
genre_entry.insert(0, "Action")

tk.Button(genre_frame, text="Search by Genre", command=search_by_genre).pack(side=tk.LEFT)

# Title search
title_frame = tk.Frame(root)
title_frame.pack(pady=5)

tk.Label(title_frame, text="Title: ").pack(side=tk.LEFT)
title_entry = tk.Entry(title_frame, width=25)
title_entry.pack(side=tk.LEFT, padx=5)
title_entry.insert(0, "Oshi no Ko")

tk.Button(title_frame, text="Search by Title", command=search_by_title).pack(side=tk.LEFT)

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
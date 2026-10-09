import tkinter as tk
import AnilistInterface as anilist

#functions
def search_anime():
    anilist.GetTopAnime (genreIn = "Action")

root = tk.Tk ()

root.title ("Anime Match")
root.geometry("500x300")

#varibles
search_button = tk.Button (root, text="Search", command=search_anime)

search_button.pack()
root.mainloop()
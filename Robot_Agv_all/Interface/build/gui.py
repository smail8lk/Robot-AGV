
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Dell\Documents\Réseaux Industriels\ROBOT_AGV\ROBOT_AGV\Interface\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("710x499")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 499,
    width = 710,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=287.0,
    y=415.0,
    width=137.0,
    height=38.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    290.0,
    121.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#CAD4DD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=188.0,
    y=100.0,
    width=204.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    563.0,
    357.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=461.0,
    y=336.0,
    width=204.0,
    height=41.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    563.0,
    284.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=461.0,
    y=263.0,
    width=204.0,
    height=41.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    290.0,
    191.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=188.0,
    y=170.0,
    width=204.0,
    height=41.0
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=460.0,
    y=200.0,
    width=204.0,
    height=41.0
)


canvas.create_rectangle(
    0.0,
    1.0,
    710.0,
    74.0,
    fill="#1A3257",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    606.0,
    36.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    57.0,
    36.0,
    image=image_image_2
)

canvas.create_text(
    34.0,
    108.0,
    anchor="nw",
    text="Entrer le port",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    35.0,
    169.0,
    anchor="nw",
    text="Entree addressee IP",
    fill="#000000",
    font=("Inter", 12 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    123.0,
    202.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    123.0,
    139.0,
    image=image_image_4
)



canvas.create_text(
    271.0,
    273.0,
    anchor="nw",
    text="Entrer le numero de station ",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    271.0,
    346.0,
    anchor="nw",
    text="Enter la misson ",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    271.0,
    230.0,
    anchor="nw",
    text="Enter le nombre de mission ",
    fill="#000000",
    font=("Inter", 12 * -1)
)

window.resizable(False, False)
window.mainloop()

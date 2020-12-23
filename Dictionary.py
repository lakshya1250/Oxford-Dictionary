# ----- Imports -----
from tkinter import *
import tkinter as tk
import requests
import json

# ----- Global Variables -----
height = 500
width = 800
background_color = "#FFFF00"

# Get Your API Key From developer.oxforddictionaries.com
# od-api.oxforddictionaries.com/api/v2/entries/{language}/{word}

# ----- Functions -----
def get_define(word):    
    """Gets The Definition From The Input"""
    app_id = 'app_id'
    app_key = 'api_key'
    language = 'en-us'
    toshow = ""
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'+language+"/"+word
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    if r.status_code == 200:        
        text = r.json()
        define = text["results"][0]['lexicalEntries'][0]['entries'][0]["senses"][0]["definitions"][0]
        words = define.split(" ")
        for word in words:
            toshow += word.capitalize() + " "           
        if toshow[len(toshow)//2] != " ":
            label1["text"] = f"{toshow[0:len(toshow)//2]}\n{toshow[len(toshow)//2:-1]+toshow[-1]}"
        else:
            label1["text"] = f"{toshow[0:len(toshow)//2]}\n{toshow[(len(toshow)//2)+1:-1]+toshow[-1]}"
    else:
        label1["text"] = "There Was A Problem\nRetrieving That Information"
    
# ----- Main Code -----

# Initializing The Main Tkinter Window
root = tk.Tk()
root.title("Oxford Dictionary")
root.geometry(f"{width}x{height}")

# Initializing And Setting The Images
logo_image = tk.PhotoImage(file = "Logo.png")
background_image = tk.PhotoImage(file = 'Background.png')
root.iconphoto(False, logo_image)
root.iconbitmap("Icon.ico")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# Creating The Main Window
frame1 = tk.Frame(root, bg = background_color, relief = RIDGE, bd = 5)
frame1.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry1 = tk.Entry(frame1, font = ("Times New Roman", 20), relief = RIDGE)
entry1.place(relx = 0.02, rely = 0.1, relwidth = 0.6, relheight = 0.8)

button1 = tk.Button(frame1, text = "Get Definiton", font = ("Times New Roman", 20), relief = RIDGE, command = lambda:get_define(entry.get()), cursor = "hand2")
button1.place(relx = 0.68, rely = 0.1, relwidth = 0.3, relheight = 0.8)

frame2 = tk.Frame(root, bg = background_color, relief = RIDGE, bd = 10)
frame2.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label1 = tk.Label(frame2, font = ("Courier", 20), relief = RIDGE)
label1.place(relwidth = 1, relheight = 1)

# ----- Driver Code -----
if __name__ =  = "__main__":
	root.mainloop()

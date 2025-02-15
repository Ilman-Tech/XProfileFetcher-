import tkinter as tk
from tkinter import *
import requests
import os
from dotenv import load_dotenv
from PIL import Image, ImageTk
from io import BytesIO

# Load environment variables from the .env file
load_dotenv()

# Get the Bearer Token from the .env file
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')


def get_image_profile():
    # Get the username input from the user and remove any extra spaces
    username = entry.get().strip()

    # If no username is entered, display a message
    if not username:
        profile_label.config(text="Please enter a username.")
        return

    # Build the URL to request user profile data from the Twitter API
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)

    # If the API request is successful
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        profile_image_url = data['data']['profile_image_url']

        # Replace the "_normal" in the URL to get the high-resolution image
        high_res_image_url = profile_image_url.replace("_normal", "_400x400")

        # Make a request to fetch the high-resolution image
        image = requests.get(high_res_image_url)

        # If the image is fetched successfully
        if image.status_code == 200:
            image_data = Image.open(BytesIO(image.content))
            image_data = image_data.resize((200, 200))  # Resize the image to 200x200

            # Convert the image to a format that can be displayed in Tkinter
            photo = ImageTk.PhotoImage(image_data)

            # Update the label with the profile image
            profile_label.config(image=photo)
            profile_label.image = photo
        else:
            # If there was an error fetching the image
            profile_label.config(text="Image not found. Please try again later.")
    else:
        # If the API request fails
        profile_label.config(text="Request failed. Please try again later.")


# Setup the main window
root = tk.Tk()
root.title('X Profile Downloader')  # Window title
root.geometry('400x500')  # Window size
root.resizable(False, False)  # Prevent resizing the window

# Label for the username input field
label = Label(root, text='Enter Twitter username', font=('Arial', 16))
label.pack(pady=10)

# Input field for the username
entry = Entry(root, font=('Arial', 16), justify='center', borderwidth=5, bd=5, width=25)
entry.pack(pady=10)

# Button to trigger the profile image fetch
button = Button(root, text="Get Profile", borderwidth=5, bd=5)
button.config(command=get_image_profile)  # Bind the button to the function
button.pack(pady=10)

# Label to display the profile image
profile_label = Label(root)
profile_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

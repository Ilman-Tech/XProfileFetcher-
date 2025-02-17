# XProfileFetcher

## Introduction  
In version 2 of this project, we have added a completely new graphical user interface (GUI) that allows users to easily view the profile picture of a Twitter user directly within the application, without the need to manually extract the image link. This project is designed as an exercise for learning how to work with APIs and send HTTP requests.

## Technologies Used
- **Tkinter**: A Python library for building graphical user interfaces (GUIs).
- **PIL (Pillow)**: A Python library for image processing and manipulation.
- **Requests**: A simple Python library for sending HTTP requests to the Twitter API.
- **dotenv**: A Python library for managing environment variables, such as the Twitter Bearer token.
- **io**: A Python module for managing byte data, especially when working with image content.

## Libraries Required
To install the necessary libraries, run the following commands:
```bash
pip install Pillow
pip install requests
pip install python-dotenv
```

## How the Program Works
1. **User Input**: The user enters the Twitter username in the input field.
2. **Sending Request to API**: Upon clicking the "Get Profile" button, the application sends a request to the Twitter API using the Bearer token.
3. **Receiving Profile Image**: The program retrieves the user's profile picture in high quality (400x400) from the API.
4. **Displaying Image**: The profile image is displayed within the Tkinter graphical interface, allowing the user to view it without needing to open a browser.

## Setting Up the Program

For the program to work correctly, you first need to visit the [Twitter Developer website](https://developer.twitter.com/en/apps) and obtain your API key. After getting your API key, you will need to add the raw URL of the website.

Then, create a file named `.env` and store your API key inside a variable. This file should be placed in the root directory of your project so the program can access it.

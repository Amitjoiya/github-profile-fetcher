# GitHub Profile Fetcher

## Overview
This Python command-line tool uses the GitHub REST API to fetch and display a GitHub user's profile information along with their top 5 most recently updated repositories. The tool retrieves user data and saves the fetched information in a structured JSON file.

## Features
- Accepts GitHub username as input
- Fetches user profile details including name, bio, location, follower counts, and account creation date
- Retrieves top 5 repositories sorted by the most recent update with details like name, description, programming language, stars, and last updated time
- Saves the fetched data into a JSON file named with the username and timestamp

## Requirements
- Python 3.x
- `requests` library (Install using: `pip install requests`)

## How to Run
1. Open the terminal or command prompt in the project folder
2. Run the command: `python main.py`
3. Enter the GitHub username when prompted
4. The user profile and repository details will be displayed on the console
5. A JSON file containing the fetched data will be saved in the project folder

## Sample Output


User Name: Amit Joiya
Bio: BSc CS & Data Analytics @ IIT Patna | Learning Python & Data Science
Location: India
Public Repos: 5
Followers: 0
Following: 0

Top 5 Repositories:
Name: todo-fullstack
Description: None
Language: JavaScript
Stars: 0
Last Updated: 2025-08-21T05:51:36Z
...



## Notes
- If an invalid username is entered, the program will display a "User not found" message.
- The JSON output file is uniquely named using the username and timestamp to avoid overwriting.
- Basic error handling for network issues and invalid inputs is included.

---

Feel free to customize this README as needed. This should give your interviewer a clear understanding of your project and its functionality.

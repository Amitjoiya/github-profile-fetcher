import requests
import json
from datetime import datetime

def fetch_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("User not found or error occurred.")
        return None

def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        sorted_repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)[:5]
        return sorted_repos
    else:
        print("Repositories data fetch karne me error.")
        return None

def main():
    username = input("Enter GitHub username: ")
    profile = fetch_github_profile(username)
    repos = fetch_repositories(username)

    if profile and repos:
        data_to_save = {
            "user_profile": {
                "login": profile.get("login"),
                "name": profile.get("name"),
                "bio": profile.get("bio"),
                "location": profile.get("location"),
                "public_repos": profile.get("public_repos"),
                "followers": profile.get("followers"),
                "following": profile.get("following"),
                "created_at": profile.get("created_at")
            },
            "repositories": [
                {
                    "name": repo.get("name"),
                    "description": repo.get("description"),
                    "language": repo.get("language"),
                    "stargazers_count": repo.get("stargazers_count"),
                    "updated_at": repo.get("updated_at")
                }
                for repo in repos
            ]
        }

        file_name = f"{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(file_name, "w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

        print(f"\nData saved successfully in {file_name}")

        print("User Name:", profile.get("name"))
        print("Bio:", profile.get("bio"))
        print("Location:", profile.get("location"))
        print("Public Repos:", profile.get("public_repos"))
        print("Followers:", profile.get("followers"))
        print("Following:", profile.get("following"))

        print("\nTop 5 Repositories:")
        for repo in repos:
            print("Name:", repo.get("name"))
            print("Description:", repo.get("description"))
            print("Language:", repo.get("language"))
            print("Stars:", repo.get("stargazers_count"))
            print("Last Updated:", repo.get("updated_at"))
            print("------")

if __name__ == "__main__":
    main()

import requests
from datetime import datetime

token = ''######Enter your token here

headers = {
    'Authorization': f'token {token}'
}

def fetch_user_info(user):
    response = requests.get(f'https://api.github.com/users/{user}', headers=headers)
    data = response.json()
    return data

def fetch_repos(user):
    response = requests.get(f'https://api.github.com/users/{user}/repos', headers=headers)
    data = response.json()
    return data

def fetch_followers(user):
    followers = []
    url = f'https://api.github.com/users/{user}/followers'
    while url:
        response = requests.get(url, headers=headers)
        followers.extend(response.json())
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return followers

def fetch_following(user):
    following = []
    url = f'https://api.github.com/users/{user}/following'
    while url:
        response = requests.get(url, headers=headers)
        following.extend(response.json())
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None
    return following

def calculate_average_stars(repos):
    total_stars = sum([repo['stargazers_count'] for repo in repos])
    average_stars = total_stars / len(repos)
    return average_stars

def calculate_total_forks(repos):
    total_forks = sum([repo['forks_count'] for repo in repos])
    return total_forks

def calculate_total_watchers(repos):
    total_watchers = sum([repo['watchers_count'] for repo in repos])
    return total_watchers


def display_user_info(user_info):
    print(f"\nUser info for {user_info['login']}:")
    print(f"Login: {user_info['login']}")
    print(f"ID: {user_info['id']}")
    print(f"Name: {user_info.get('name', 'N/A')}")
    print(f"Company: {user_info.get('company', 'N/A')}")
    print(f"Blog: {user_info.get('blog', 'N/A')}")
    print(f"Location: {user_info.get('location', 'N/A')}")
    print(f"Email: {user_info.get('email', 'N/A')}")
    print(f"Bio: {user_info.get('bio', 'N/A')}")
    print(f"Followers: {user_info['followers']}")
    print(f"Following: {user_info['following']}")
    created_at = datetime.fromisoformat(user_info['created_at'].replace('Z', '+00:00'))
    updated_at = datetime.fromisoformat(user_info['updated_at'].replace('Z', '+00:00'))
    print(f"Created At: {created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Updated At: {updated_at.strftime('%Y-%m-%d %H:%M:%S')}")


def display_repos_info(user, repos):
    average_stars = calculate_average_stars(repos)
    print(f"\nThe average number of stars for {user}'s repositories is {round(average_stars, 1)}")

    total_forks = calculate_total_forks(repos)
    print(f"The total number of forks for {user}'s repositories is {round(total_forks, 1)}")

    total_watchers = calculate_total_watchers(repos)
    print(f"The total number of watchers for {user}'s repositories is {round(total_watchers, 1)}")


def display_followers(user, followers, n=None):
    print(f"\nFollowers of {user}:")
    total_followers = len(followers)
    if n is None:
        n = total_followers
        print(f"Displaying all {n} followers.")
    else:
        print(f"Displaying top {n} of {total_followers} followers.")
    for follower in followers[:n]:
        follower_info = fetch_user_info(follower['login'])
        print(f"{follower['login']} ({follower_info.get('name', 'N/A')})")

def display_following(user, following, n=None):
    print(f"\nFollowing of {user}:")
    total_following = len(following)
    if n is None:
        n = total_following
        print(f"Displaying all {n} following.")
    else:
        print(f"Displaying top {n} of {total_following} following.")
    for user in following[:n]:
        user_info = fetch_user_info(user['login'])
        print(f"{user['login']} ({user_info.get('name', 'N/A')})")

def main_menu():
    predefined_users = ['mojombo', 'galvez', 'broccolini', 'github']
    
    while True:
        print("\nMenu:")
        print("1. Display user information")
        print("2. Display user repository information")
        print("3. Display user followers")
        print("4. Display user following")
        print("0. Exit")

        choice = input("Enter your choice: ")
        
        if choice in ['1', '2', '3', '4']:
            print("\nSelect a GitHub username:")
            print("1. Enter a GitHub username")
            for i, user in enumerate(predefined_users, start=2):
                print(f"{i}. {user}")
            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                user = input("Enter a GitHub username: ")
            elif 2 <= int(user_choice) <= len(predefined_users) + 1:
                user = predefined_users[int(user_choice) - 2]
            else:
                print("Invalid choice. Please enter a valid option.")
                continue

            if choice == '1':
                user_info = fetch_user_info(user)
                if 'login' in user_info:
                    display_user_info(user_info)
                else:
                    print(f"Could not fetch user info for {user}")
            elif choice == '2':
                repos = fetch_repos(user)
                display_repos_info(user, repos)
            elif choice == '3':
                followers = fetch_followers(user)
                total_followers = len(followers)
                n = input(f"Enter the number of followers to display or 'all' to display ({total_followers}) followers: ")
                n = None if n.lower() == 'all' else int(n)
                followers = fetch_followers(user)
                display_followers(user, followers, n)
            elif choice == '4':
                following = fetch_following(user)
                total_following = len(following)
                n = input(f"Enter the number of following to display or 'all' to display ({total_following}) following: ")
                n = None if n.lower() == 'all' else int(n)
                following = fetch_following(user)
                display_following(user, following, n)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()

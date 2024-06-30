import argparse
import json
import os
from zipfile import ZipFile


INSTAGRAM = "instagram"
SOURCE_DIR = "connections/followers_and_following"


def parser():
    parser = argparse.ArgumentParser(
        description="Instafollow is a tool to analyze Instagram followers and following."
    )

    parser.add_argument(
        "-i",
        "--import",
        dest="import_file",
        metavar="FILE",
        help="Import the downloaded Instagram data. Specify the zip file.",
    )
    parser.add_argument(
        "-l",
        "--list",
        type=str,
        choices=["followers", "following", "not_following_back", "not_followed_back"],
        metavar="ITEM",
        help="List the followers, following, not_following_back, or not_followed_back.",
    )

    args = parser.parse_args()

    if args.import_file:
        extract_zip_file(args.import_file)
    elif args.list:
        if args.list == "followers":
            print("Followers")
            for i, user in enumerate(get_followers()):
                print(f"{i+1}. {user}")
        elif args.list == "following":
            print("Following")
            for i, user in enumerate(get_following()):
                print(f"{i+1}. {user}")
        elif args.list == "not_following_back":
            print("Not following back")
            followers = get_followers()
            following = get_following()
            not_following_back = [user for user in following if user not in followers]
            for i, user in enumerate(not_following_back):
                print(f"{i+1}. {user}")
        elif args.list == "not_followed_back":
            print("Not followed back")
            followers = get_followers()
            following = get_following()
            not_followed_back = [user for user in followers if user not in following]
            for i, user in enumerate(not_followed_back):
                print(f"{i+1}. {user}")
    else:
        parser.print_help()

def extract_zip_file(zip_file):
    with ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall()
    print("Files extracted successfully.")


def get_followers():
    # read json object from followers_*.json
    followers = []
    for file in os.listdir(SOURCE_DIR):
        if "followers" in file:
            with open(f"{SOURCE_DIR}/{file}") as f:
                data = f.read()
                f.close()
                users = json.loads(data)
                followers.extend(
                    [user["string_list_data"][0]["value"] for user in users]
                )
    return followers


def get_following():
    # read json object from following_*.json
    following = []
    for file in os.listdir(SOURCE_DIR):
        if "following" in file:
            with open(f"{SOURCE_DIR}/{file}") as f:
                data = f.read()
                users = json.loads(data)
                following.extend(
                    [
                        user["string_list_data"][0]["value"]
                        for user in users["relationships_following"]
                    ]
                )
    return following


if __name__ == "__main__":
    parser()

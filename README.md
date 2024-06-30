# Instafollow
Instafollow is a simple script that allows you to see followers, following, not following back and not followed back on Instagram.

## Instructions
1. Login to your Instagram account on your browser
2. Go [here](https://accountscenter.instagram.com/info_and_permissions/dyi/) and click on "Download or transfer informations"
3. Select instgram account > Some of my data > Followers and Following
4. Download to device
5. Select the date range
6. Select json format
7. Create file

## Usage
```bash
$ python3 instafollow.py

usage: instafollow.py [-h] [-i FILE] [-l ITEM]

Instafollow is a tool to analyze Instagram followers and following.

options:
  -h, --help            show this help message and exit
  -i FILE, --import FILE
                        Import the downloaded Instagram data. Specify the zip file.
  -l ITEM, --list ITEM  List the followers, following, not_following_back, or not_followed_back.


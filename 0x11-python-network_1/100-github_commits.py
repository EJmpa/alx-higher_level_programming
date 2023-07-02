#!/usr/bin/python3
"""
Uses the GitHub API to list 10 most recent commits of a repository by an owner.
Usage: ./100-github_commits.py <repository> <owner>
"""

import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit["sha"]
            author = commit["commit"]["author"]["name"]
            print(f"{sha}: {author}")
    except IndexError:
        pass

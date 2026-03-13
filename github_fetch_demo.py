import os
from github import Github, GithubException
from datetime import datetime, timedelta, UTC
from config_reader import load_repositories


def fetch_recent_commits(repo_full_name):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)
    try:
        repo = g.get_repo(repo_full_name)
    except GithubException as e:
        msg = getattr(e, 'data', None)
        if isinstance(msg, dict) and 'message' in msg:
            err = msg['message']
        else:
            err = str(e)
        print(f"\nRepository: {repo_full_name} - ERROR fetching repo: {err}")
        return

    since_time = datetime.now(UTC) - timedelta(hours=24)

    try:
        commits = repo.get_commits(since=since_time)
    except GithubException as e:
        print(f"\nRepository: {repo_full_name} - ERROR fetching commits: {e}")
        return

    print(f"\nRepository: {repo_full_name}")

    count = 0
    for commit in commits:
        # defensive access: commit metadata can be partially missing
        message = getattr(commit.commit, 'message', '<no message>')
        author_name = None
        author_date = None

        if getattr(commit, 'author', None) and getattr(commit.author, 'login', None):
            author_name = commit.author.login
        elif getattr(commit.commit, 'author', None) and getattr(commit.commit.author, 'name', None):
            author_name = commit.commit.author.name
        else:
            author_name = 'Unknown'

        if getattr(commit.commit, 'author', None) and getattr(commit.commit.author, 'date', None):
            author_date = commit.commit.author.date
        else:
            author_date = 'Unknown'

        print("Commit message:", message)
        print("Author:", author_name)
        print("Date:", author_date)
        print("-" * 30)

        count += 1
        if count >= 5:
            break


if __name__ == "__main__":
    repos = load_repositories()

    for repo in repos:
        full_name = f"{repo['owner']}/{repo['name']}"
        fetch_recent_commits(full_name)
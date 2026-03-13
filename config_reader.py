import yaml


def load_repositories(config_file="repos.yaml"):
    with open(config_file, "r") as file:
        data = yaml.safe_load(file)

    return data["repos"]


def print_repositories(repos):
    print("Repositories loaded from config:\n")

    for repo in repos:
        print(f"Name: {repo['name']}")
        print(f"Owner: {repo['owner']}")
        print(f"URL: {repo['url']}")
        print(f"Type: {repo['type']}")
        print("-" * 40)


if __name__ == "__main__":
    repositories = load_repositories()
    print_repositories(repositories)
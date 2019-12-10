from github import Github

# remove the minus sign from the key
g = Github("8c0e5202752a9f00b139b7d0f36bd79f75741975")

for repo in g.get_user().get_repos():
    print(repo.name)
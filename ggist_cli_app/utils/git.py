import subprocess
import os

def clone(repo, local):
    p = subprocess.Popen(['git', 'clone', repo, local], stdout=subprocess.PIPE)
    print(p.communicate())

def get_repo_name(remote_url):
    return os.path.splitext(os.path.basename(remote_url))[0]

# def commit():
#     commit_message = input('\nType in your commit message: ')
#     run('commit', '-am', commit_message)
#     run('push', '-u', 'origin', 'master')


# def branch():
#     branch = input('\nType in the name of the branch you want to make: ')
#     run('checkout', '-b', branch)

#     choice = input('\nDo you want to push the branch right now to GitHub? (y/n): ').lower()

#     if choice == 'y':
#         run('push', '-u', 'origin', branch)
#     else:
#         print('\nOkay, goodbye!\n')


# def pull():
#     print('\nPulls changes from the current folder if *.git is initialized.')
#     choice = input('\nDo you want to pull the changes from GitHub? (y/n): ').lower()

#     if choice == 'y':
#         run('pull')
#     else:
#         print('\nOkay, goodbye!\n')


# def fetch():
#     print('\nFetches changes from the current folder.')
#     run('fetch')


# def merge():
#     branch = input('\nType in the name of your branch: ')
#     run('merge', branch)


# def reset():
#     filename = input('\nType in the name of your file: ')
#     run('reset', filename)


# def blame():
#     file = input('\nType in the name of the file: ')
#     run('blame', file)


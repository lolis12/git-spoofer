import git
from datetime import date, datetime, time, timedelta
from os import environ, getcwd, system
from os.path import join
from random import randint
def create(days, file_name, code, commit_message, final_message, empty_repo_url):
    repo, file_path = git.Repo.init(getcwd()), join(getcwd(), file_name)
    for commit_date in [datetime.combine(d, time(hour=randint(0, 23), minute=randint(0, 59), second=randint(0, 59), microsecond=randint(0, 999999))) for d in dates(days)]:
        open(file_path, "w").write(str(__import__('uuid').uuid1()))
        repo.index.add([file_path])
        environ["GIT_AUTHOR_DATE"] = environ["GIT_COMMITTER_DATE"] = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        repo.index.commit(commit_message)
    open(file_path, "w").write(code)
    environ["GIT_AUTHOR_DATE"] = environ["GIT_COMMITTER_DATE"] = ""
    repo.index.add([file_path])
    repo.index.commit(final_message)
    repo.create_remote("origin", empty_repo_url)
    system("git push origin master") # repo.remotes.origin.push() Isn't working
def dates(days):
    for day_delta in range(days):
        for i in range(randint(1, 10)): yield date.today() - timedelta(days=day_delta)
year = 2021
wanted_year = 2008
year = round((year - wanted_year) * 365.24)
create(year, "commit.py", open(__file__).read(), "Commit", "DONE", "https://github.com/lolis12/pop4.git")

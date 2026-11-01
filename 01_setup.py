import shutil 
import subprocess
import re
import github.Github as gh

def check_ifInstalled(pkg_name: str) -> bool: 
    """
    Args:
        pgk_name (str): package name to be checked if it's installed. Use with .exe extension

    Return:
        bool
    """

    # TODO: check if pkg_name is a string
    pkg_path = shutil.which(pkg_name)

    if pkg_path:
        return True
    else:
        print(f"{pkg_name} is not in PATH")
        return False

def check_ifInstalledPipx(pkg_name: str) -> bool: 
    """
    Args:
        pgk_name (str): package name to be checked if it's installed. Use with .exe extension

    Return:
        bool
    """

    pipx_dump = subprocess.run(["pipx", "list"], capture_output=True, text=True, check=True).stdout

    lines = pipx_dump.splitlines()

    installed = False

    for line in lines:
        if re.search(pkg_name, line):
            installed = True

    if not installed:
        print(f"{pkg_name} is not in PATH")

    return installed

if not check_ifInstalled("git.exe"):
    subprocess.run("winget install Git.Git --scope user")

if not check_ifInstalled("gh.exe"):
    subprocess.run("winget install GitHub.cli --scope user")

if not check_ifInstalled("dc.exe"):
    token = None # Put your GitHub API token here if you want to access a private repo.
    repo_path = "doublecmd/doublecmd"
    g = gh(token)
    repo = g.get_repo(repo_path)
    latest = repo.get_latest_release()
    print(latest.title)

# TODO: put every pkg name to list so it will be less package managers calls???
# before that check for pipx

if not check_ifInstalledPipx("uv.exe"):
    subprocess.run("pipx install uv.exe")

# NOTE: Doesn't work - can't install msvc build tools
# if not check_ifInstalledPipx("vimiv.exe"):
#     subprocess.run("pipx install vimiv")
#     subprocess.run("pipx inject vimiv PyQt6")

# TODO:
# add keepassxc
# add neovim
# add neovim's dots
# add syncthing
# add latex

# TODO:
# check later: 
# gh release download --repo owner/repo --pattern "*.zip"

# add try catches

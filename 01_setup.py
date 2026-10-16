import shutil 
import subprocess
import re

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

# TODO: put every pkg name to list so it will be less package managers calls???

if not check_ifInstalledPipx("uv.exe"):
    subprocess.run("pipx install uv.exe")


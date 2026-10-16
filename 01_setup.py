import shutil 
import subprocess

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


if not check_ifInstalled("git.exe"):
    subprocess.run("winget install Git.Git --scope user")

if not check_ifInstalled("gh.exe"):
    subprocess.run("winget install GitHub.cli --scope user")


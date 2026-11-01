
# Source - https://stackoverflow.com/a/77784164
# Posted by Gabriel Gomes
# Retrieved 2026-11-01, License - CC BY-SA 4.0

# TODO: merge with setup

import requests
response = requests.get("https://github.com/doublecmd/doublecmd/releases/latest")
latest_tag = response.url.split('/').pop()
actual_version = response.url
numbers_version = latest_tag.replace("v", "")
# https://github.com/doublecmd/doublecmd/releases/download/v1.2.10/doublecmd-1.2.10.x86_64-win64.zip
download_url = "https://github.com/doublecmd/doublecmd/releases/download/" + latest_tag + "/" + "doublecmd-" + numbers_version + ".x86_64-win64.zip"

req = requests.get(download_url)
filename = download_url.split('/')[-1]
 
# Writing the file to the local file system
with open(filename,'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')

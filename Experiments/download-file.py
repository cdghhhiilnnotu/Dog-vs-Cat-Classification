# import bs4
# import requests

# url = "https://drive.google.com/drive/u/0/folders/1y7EP2-Rkz8w98_ANynOtlzqiOF_LOkIc"
# r = requests.get(url)
# data = bs4.BeautifulSoup(r.text, "html.parser")
# for l in data.find_all("a"):
#     r = requests.get(url + l["href"])
#     print(r.status_code)

# import requests
# URL = "https://drive.google.com/file/d/1Sew3xRbnWTT1xeH_p-JlDpyH7_-VRLr5/view?usp=drive_link"
# response = requests.get(URL)
# open("instagram.png", "wb").write(response.content)

import requests

url = "https://drive.google.com/file/d/1Sew3xRbnWTT1xeH_p-JlDpyH7_-VRLr5/view?usp=drive_link"
response = requests.get(url)

if response.status_code == 200:
    with open("file.png", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file.")




 
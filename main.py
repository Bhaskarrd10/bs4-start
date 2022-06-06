
from bs4 import BeautifulSoup
#import lxml


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title.string)
#print(soup.prettify())
#print(soup.a)
#print(soup.p)

all_anchour_tags = soup.find_all(name="a")
#print(all_anchour_tags)

for tag in all_anchour_tags:
    print(tag.getText())
import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/jobs/jobs-in-berkeley-ca?trk=homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
links = soup.find_all('a', {'class': 'base-card__full-link'})


#print(links)


url_job = "https://www.linkedin.com/jobs/view/brand-finance-analyst-at-clif-bar-company-2813781657?refId=vwaUiua%2F9e66C%2FvcDuVkig%3D%3D&trackingId=qIbva%2F6X6LM2Mai2jc4YoA%3D%3D&trk=public_jobs_topcard-title"

txt2 = requests.get(url_job).text
s2 = BeautifulSoup(txt2, 'html.parser')
result2 = s2

print(result2)
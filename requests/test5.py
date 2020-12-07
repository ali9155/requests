import requests
from bs4 import BeautifulSoup
url = 'https://www.worldometers.info/coronavirus/?_hsenc=p2ANqtz--rZXdvpxgMsH2oK-1Gnu8BHPWc7J_QFtZPsrVwAQqpHNrXQyllzVBZ-CG04OGICUPv9WB0pw6m8Xj09Ixp0oS-m2EepfHxZxugXc-OjvBoFnnxDpI&_hsmi=84525637'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

strings = soup.find_all(string=re.compile('china'))

for txt in strings:
    print(' '.join(txt.split()))
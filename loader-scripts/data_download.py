

# Start with the following to reproduce
# wget --recursive --no-parent --accept zip "http://www2.census.gov/acs2010_5yr/summaryfile/2006-2010_ACSSF_By_State_All_Tables/"

import urllib.request as ur
import bs4

url_root = "http://www2.census.gov/acs2010_5yr/summaryfile/2006-2010_ACSSF_By_State_All_Tables/"

contents = ur.urlopen(url_root)

data = contents.read()

soup = bs4.BeautifulSoup(data, 'html.parser')

# simple recognizer for zip file 
import re
zip_re = re.compile('\.zip$')

# recognize and pull out one zip files
link_list = [link['href'] for link in soup.find_all(href=zip_re)]
zip_to_retrieve = url_root + link_list[0]
res = ur.urlretrieve(zip_to_retrieve, link_list[0])






# Start with the following to reproduce
# wget --recursive --no-parent --accept zip "http://www2.census.gov/acs2010_5yr/summaryfile/2006-2010_ACSSF_By_State_All_Tables/"

import re
import urllib.parse as up
import urllib.request as ur
import requests as rq
import bs4

# url_root = "http://www2.census.gov/acs2010_5yr/summaryfile/2006-2010_ACSSF_By_State_All_Tables/"

census_domain_data = 'http://www2.census.gov/'
census_survey = 'acs'
census_release = '2010_5yr'
census_data_granularity = 'summaryfile'
census_data_directory = '2006-2010_ACSSF_By_State_All_Tables'

local_data_directory = 'c:\\users\\swint\\git\\metralytics\\census_raw_data'

data_url = up.urljoin(census_domain_data, '/'.join([census_survey+census_release, census_data_granularity, census_data_directory]))

def get_list_zip_files(data_url):
    webpage = rq.get(data_url)

    soup = bs4.BeautifulSoup(webpage.text, 'html.parser')

    # simple recognizer for zip file 
    zip_re = re.compile('\.zip$')

    # recognize and pull out one zip files
    zipfile_list = [link['href'] for link in soup.find_all(href=zip_re)]

    return zipfile_list

zipfile_list = get_list_zip_files(data_url)

file_name = zipfile_list[1]

def download_file(file_name, data_url, target_directory='.'):
    from os import path

    print('file_name:', file_name)

    zip_to_retrieve = data_url + '/' + file_name
    print('zip_to_retrieve:', zip_to_retrieve)

    file_target = path.join(target_directory, file_name)
    print('file_target:', file_target)

    res = ur.urlretrieve(zip_to_retrieve, file_target)
    return res

download_file(file_name, data_url, local_data_directory)




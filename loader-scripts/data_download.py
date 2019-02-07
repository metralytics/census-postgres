

# Start with the following to reproduce
# wget --recursive --no-parent --accept zip "http://www2.census.gov/acs2010_5yr/summaryfile/2006-2010_ACSSF_By_State_All_Tables/"

import re
import urllib.parse as up
import urllib.request as ur
import requests as rq
import bs4

# url_root = "http://www2.census.gov/acs2016_5yr/summaryfile/2012-2016_ACSSF_By_State_All_Tables/"
# url_root = 'https://www2.census.gov/programs-surveys/acs/summary_file/'

# format 
# parent  'https://www2.census.gov/programs-surveys/acs/summary_file/'
# year 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}'
# data directory 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data'
# file: 1-year templates 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data/{year}_1yr_Summary_FileTemplates.zip'
# file: 5-year templates 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data/{year}_1yr_Summary_FileTemplates.zip'
# data file: 1-year data 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data/1_year_entire_sf/All_Geographies.zip'
# geography files: 5-year data # data file: 5-year data group 2 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data/5_year_entire_sf/{year}_ACS_Geography_Files.zip'
# data file: 5-year data group 2 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data/5_year_entire_sf/Tracts_Block_Groups_Only.tar.gz'
# data file: 5-year data group 1 'https://www2.census.gov/programs-surveys/acs/summary_file/{year}/data/5_year_entire_sf/All_Georgraphies_Not_Tracts_Blocks_Groups.tar.gz'

census_domain_data = 'http://www2.census.gov/'
census_survey = 'acs'
census_release = '2016_5yr'
census_data_granularity = 'summaryfile'
census_data_directory = '2012-2016_ACSSF_By_State_All_Tables'

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

for file_name in zipfile_list:
    download_file(file_name, data_url, local_data_directory)





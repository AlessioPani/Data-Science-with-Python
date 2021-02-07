# Script that implements the following command:
# wget -O /resources/data/Example1.txt 'url'

import os, requests

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

def retrieveContent(url):
    '''
    Check if the provided url does actually have a content. 
    '''
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error {response.status_code}')
        return None
    else:
        print(f'Ok!')
        return response.content


def writeContent(path, content):
    '''
    Write on a file the content provided by retrieveContent.

    This function is called only if retrieveContent doesn't return an
    error code. 
    '''
    with open(path, 'wb') as file:
        file.write(content)

    
if __name__ == '__main__':
    response = retrieveContent(URL)

    if response is not None:
        path = os.path.join(os.getcwd(), 'example.txt')
        writeContent(path, response)

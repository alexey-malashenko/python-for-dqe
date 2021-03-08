import xml.etree.ElementTree as ET
import os

path_name = os.path.dirname(__file__)
path_name = os.path.join(path_name, 'Publikation\\'
                                                      'Publication.xml')
xml_file = ET.parse(path_name)

print(f'xml_file: {xml_file}')

root = xml_file.getroot()

print(f'root: {root}')

print('-----------------------')

for publication in root.findall('publication'):
    print(publication)
    for text in publication.findall('text'):
        print(text.text)
    for other_param in publication.findall('other_param'):
        print(other_param.text)

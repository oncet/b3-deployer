import boto3
import json
import os

with open('config.json') as json_file:
    config = json.load(json_file)

all_files = []

for folder, folders, files in os.walk(config['folder']):
    for file in files:
        all_files.append(folder + '/' + file)

print('Uploading {0} file(s) from the "{1}" folder to the "{2}" bucket.'.format(
    len(all_files), config['folder'], config['bucket']))

s3 = boto3.resource('s3')

for file in all_files:
    print('Uploading {0}.'.format(file))
    file_content = open(file, 'rb')
    s3.Bucket(config['bucket']).put_object(Key=file, Body=file_content)
    file_content.close()

print('Finished uploading files!')
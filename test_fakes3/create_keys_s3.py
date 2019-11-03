import boto3 
import os
import botocore
import random 
import uuid

from tqdm import tqdm
from io import StringIO

COMMAND_FAKE_S3 = 'fakes3 -r fakes3/fake_s3_root -p 4567  --license xxx'

def create_files_and_upload(no_of_files, bucket_name, s3_client):
    random_text = 'Manor we shall merit by chief wound no or would Oh towards between subject passage sending mention it'

    list_words = random_text.split(' ')
    for _ in tqdm(range(no_of_files)):
        file_name = uuid.uuid4().hex[:6].upper()
        random.shuffle(list_words)
        with StringIO() as out:
            out.write(' '.join(list_words))
            s3_client.upload_fileobj(out, bucket_name, f'{file_name}.txt')

def main():
    fakes3_session = boto3.Session(
        aws_access_key_id='123',
        aws_secret_access_key='abc'
    )
    s3_client = fakes3_session.client('s3', endpoint_url='http://localhost:4567')
    create_files_and_upload(1000, 'mybucket', s3_client)

if __name__ == '__main__':
    main()
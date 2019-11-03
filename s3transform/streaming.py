import os
import multiprocessing 
import boto3
import pprint


def main():
    session = boto3.Session(
        aws_access_key_id='123',
        aws_secret_access_key='abc'
    )

    pp = pprint.PrettyPrinter(indent=4)
    s3_client = session.client('s3', endpoint_url='http://localhost:4567/')

    bucket = 'mybucket'
    key = 'small.txt'
    objects = s3_client.list_objects_v2(Bucket=bucket)
    list_obj = [data['Key'] for data in objects['Contents']]
    pp.pprint(list_obj)

    s3_client.put_object(Body=s3_client.get_object(Bucket=bucket, Key=key)['Body'].read(), Bucket='my_bucket2', Key=key)

    i = 0
    for line in s3_client.get_object(Bucket='my_bucket2', Key=key)['Body'].iter_lines():
        i += 1

    print(i)    

if __name__ == '__main__':
    main()
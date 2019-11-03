import os
import boto3
import botocore
import tqdm
import pandarallel
import logging
import dask.dataframe as dd

import multiprocessing 

logger = logging.getLogger(__name__)

class s3transform():
    def __init__(self, src_params, dest_params):
        self._src_bucket = src_params['src_bucket']
        self._src_bucket = src_params['dest_bucket']
        self._src_client = src_params['src_session']
        self._src_bucket = src_params['session']

    def get_keys(self, loc=None):
        if loc is None:
            logger.error(f'Please provide a valid location to fetch keys')


def main():
    session_src = boto3.Session(
        aws_access_key_id='123',
        aws_secret_access_key='abc'
    )

    session_dest = boto3.Session(
        aws_access_key_id='123',
        aws_secret_access_key='abc'
    )


    src_params = {
        'session': session_src,
        'bucket': 'my_bucket'
    }

    dest_params = {
        'session': session_dest,
        'bucket': 'my_bucket2'
    }


if __name__ == '__main__':
    main()

    
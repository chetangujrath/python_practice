import boto3

from aws_wrapper import show_s3_buckets,upload_file,list_file,create_bucket

s3_obj = boto3.resource('s3')
file_path = 'test_file.txt'
show_s3_buckets(s3_obj)
#upload_file(s3_obj,'python-project-s3',file_path,'test_file.txt')
list_file(s3_obj,'python-project-s3')
create_bucket(s3_obj,'python-project-s3_new')
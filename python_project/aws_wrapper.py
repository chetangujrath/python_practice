def show_s3_buckets(s3_obj):
    print("The S3 buckets is follows :")
    for bucket in s3_obj.buckets.all():
        print(bucket.name)

def create_bucket(s3_obj,bucket_name):
    s3_obj.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
    print(f"bucket {bucket_name} created successfully ")


def upload_file(s3_obj,bucket_name,file_path,key_name):
    file_data = open(file_path,'rb') #open file
    # CORRECT (Capitalize Key and Body)
    s3_obj.Bucket(bucket_name).put_object(Key=key_name, Body=file_data) #process file
    file_data.close() #closed file
    print("file uploaded successfully")

def list_file(s3_obj,bucket_name):
    print(f"The S3 buckets files in {bucket_name} as follow :- ")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)
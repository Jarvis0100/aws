import boto3

s3 = boto3.client('s3')

def list_objects(sb):
    try:
        objects = s3.list_objects(Bucket=sb)['Contents']
    except Exception as e:
        print("Error while fetching:", e)
    return objects

def copy_objects(ob, sb, db):
    try:
        files = []
        for obj in ob:
            objkey = obj['Key']
            files.append(objkey)
            response = s3.get_object(Bucket=sb, Key=objkey)
            data = response['Body'].read()
            response = s3.put_object(Body=data, Bucket=db, Key=objkey)
            print("file successfully uploaded at {}".format(db))
    except Exception as e:
        print(e)
    return files

def delete_objects(sb, files):
    for file in files:
        response = s3.delete_objects(Bucket=sb, Delete={'Objects': [{'Key': file}]})
        print("file {} deleted from {} ".format(file, sb))

def main():
    sourcebucket = 'aplhabucket123'
    destinationbucket = 'destinationbucketajay'
    objs = list_objects(sourcebucket)
    files = copy_objects(objs, sourcebucket, destinationbucket)
    print("All files successfully copied into Destination bucket")
    delete_objects(sourcebucket, files)
    print("All files Deleted from Source Bucket")

if __name__ == '__main__':
    main()

import boto3


def progress(num_bytes):
    print("Uploaded {} bytes...".format(num_bytes))


s3 = boto3.resource('s3')

s3.meta.client.upload_file(
    'box.jpeg',
    'simonfong-test-bucket',
    'box.jpeg',
    Callback=progress,
    ExtraArgs={'ACL': 'public-read'}
)

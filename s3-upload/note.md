## Things to do other than this coding

1. config system with aws_access_key_id and aws_secret_access_key

2. change bucket policy:
```
{
    "Version": "2012-10-17",
      "Statement": [
      {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:DeleteObject"

            ],
            "Resource": [
                "arn:aws:s3:::MY_BUCKET_NAME",
                "arn:aws:s3:::MY_BUCKET_NAME/*"
            ]
      }
      ]
}
```
To see the file, check the item and use the `Open` button in the s3 bucket.  
The url won't work because we are making it private.

from flask import Flask
import boto3

import os
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__,static_url_path="")

client = boto3.client('s3', 
         region_name='us-west-2',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
      )



app.config['SQLALCHEMY_DATABASE_URI']=os.environ["DB_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

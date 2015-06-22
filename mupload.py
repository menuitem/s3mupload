#!/usr/bin/env python
import sys
import boto
import os
conn = boto.connect_s3() 
from boto.s3.connection import Location
#Location.DEFAULT = 'eu-west-1'
buckets = conn.get_all_buckets()
for b in buckets[10:14]:
  print b.name
source=sys.argv[1]
destination=sys.argv[2]
#check if parameters are files name
filesToUpload = []
for args in sys.argv[1:-1]:
  print args
print "Argument list:", source, destination
print os.listdir(source)


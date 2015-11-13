#!/usr/bin/python
import boto.ec2

AWS_ACCESS_KEY_ID = 'AAAAAABBBBBBKKKKK'
AWS_SECRET_ACCESS_KEY = 'qjqqqqqqqjjjjjjjjkkkkkkkkkkkk'
REGION = 'eu-west-1'

conn = boto.ec2.connect_to_region(REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

reservations = conn.get_all_reservations()
instances = reservations[0].instances
for reservation in reservations:
    instances = reservations[0].instances
    inst = instances[0]
    print(inst.instance_type)

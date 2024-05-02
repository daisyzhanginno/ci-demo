#!/usr/bin/python3
import argparse
import json
import os
import sys

from rethinkdb import RethinkDB

r = RethinkDB()
# connect and make the connection available to subsequent commands 
r.connect('localhost', 28015).repl()

# lists the databases available in RethinkDB
print(r.db_list().run())

# creating a new database
#r.db_create('ci_demo').run()

#creating a new table
#r.db('ci_demo').table_create('projects').run()

# save projects table as a reference for the next operations
projects = r.db('ci_demo').table('projects')

'''
# insert one document
projects.insert({
    "project": "system", 
    "repo":"cidemo",
    "feature":"wallpaper",
    "branch":"master",
    "phone":"salami",
    "test_case":"power",
    "method":"idle",
    "build":"1",           
}).run()

# insert multiple documents
projects.insert([
  {
    "project": "system", 
    "repo":"cidemo",
    "feature":"wallpaper",
    "branch":"master",
    "phone":"salami",
    "test_case":"power",
    "method":"idle",
    "build":"2",           
  },
  {
    "project": "system", 
    "repo":"cidemo",
    "feature":"wallpaper",
    "branch":"master",
    "phone":"salami",
    "test_case":"power",
    "method":"idle",
    "build":"3",           
  },
  {
    "project": "system", 
    "repo":"cidemo",
    "feature":"interpolation",
    "branch":"master",
    "phone":"salami",
    "test_case":"power",
    "method":"idle",
    "build":"1",           
  }
]).run()
'''

# list all the documents who matches the filter
print(projects.filter({'build': '2'}).run())

# The server-side operation pluck allows fetching only the specified attributes of the result documents.
print(projects.filter({'build': '2'}).pluck('feature').run())

print(projects.filter(r.row['build']>='2').pluck('repo','build').run())

# update documents
'''
projects.update({
    'build': r.row['build']+'0',
}).run()
'''


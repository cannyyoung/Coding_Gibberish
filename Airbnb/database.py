from pymongo import MongoClient
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify

class DatabaseConnection():

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client["airbnblite"]

    def appendToObject(self, cursor):
        result = []
        for row in cursor:
            if row['_id']:
                row['_id'] = str(row['_id'])
            result.append(row)
        return result

    def findOne(self, collectionName, query):
        collection = self.db[collectionName]
        result = collection.find_one(query, {'_id':0})
        action = "Get for {}".format(collectionName)
        print(action)
        return result

    def findMany(self, collectionName, query):
        collection = self.db[collectionName]
        cursor = collection.find(query)
        result = self.appendToObject(cursor)
        return result

    def findAll(self,collectionName):
        action = "Get all documents for {}".format(collectionName)
        print(action)
        collection = self.db[collectionName]
        cursor = collection.find({})
        result = self.appendToObject(cursor)
        return result

    def insert(self,collectionName,document): #add_to_collection
        action = "Inserting one document into {}".format(collectionName)
        print(action)
        self.db[collectionName].insert_one(document)
        return True

    def update(self,collectionName,filter,query):
        self.db[collectionName].update_one(filter, query) #check_for_your_stuff
        return True
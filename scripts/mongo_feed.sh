#!/bin/bash

echo "Waiting for replica set setup..."
sleep 30
echo "done"

mongoimport --uri mongodb://mongo_1:27017/my_init_db --collection users --type json --file /data/init.json --jsonArray


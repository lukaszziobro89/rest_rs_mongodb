FROM mongo:latest

COPY init.json /data

CMD mongoimport --uri mongodb://mongo_server:27017/my_init_db --collection users --type json --file /data/init.json --jsonArray
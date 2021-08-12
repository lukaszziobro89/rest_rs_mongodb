Use the below command in ```mongosh``` terminal when want to query replica/secondary mongo (mongo_1/mongo_2) 
```sh
db.getMongo().setReadPref('secondary')
```

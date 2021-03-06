#!/bin/bash

echo "Waiting for startup.."
sleep 30
echo "done"

/usr/bin/mongo --host mongo_1:27017 --eval '''if (rs.status()["ok"] == 0) {
    rsconf = {
      _id : "rs0",
      members: [
        { _id : 0, host : "mongo_1:27017", priority: 1.0 },
        { _id : 1, host : "mongo_2:27017", priority: 0.5 },
        { _id : 2, host : "mongo_3:27017", priority: 0.5 }
      ]
    };
    rs.initiate(rsconf);
}
rs.conf();
rs.secondaryOk();
rs.status();
'''

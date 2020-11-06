import random
import time
import spooky_hash
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["hash"]
startTime = time.time()

while True:
        random.seed()
        loop = random.randint(1, 99999)
        result = random.randint(1, 99999)
        spooky_hash.Hash128(str(result)).hexdigest()
        executionTime = (time.time() - startTime)
        loopprint = spooky_hash.Hash128(str(loop)).hexdigest()
        print(loopprint)
        mylist = [
            {"number": loopprint}
        ]
        x = mycol.insert_many(mylist)
        print(x.inserted_ids)
        if spooky_hash.Hash128(str(loop)).hexdigest() == spooky_hash.Hash128(str(result)).hexdigest():
            print('Execution time in seconds: ' + str(executionTime))
            print("Primary generated number: " + str(loop)),spooky_hash.Hash128(str(loop)).hexdigest()
            print("Secondary generated number: " + str(result)),spooky_hash.Hash128(str(result)).hexdigest()
            break

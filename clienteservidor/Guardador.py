import pickle


db={}
db['saturacion']={}
db['usuarios']={}
db['cantidadMail']={}
db['bandeja']={}


def write_file():
 
    f = open('examplePickle', 'ab')
    db={}
    db['saturacion']={}
    db['usuarios']={}
    db['cantidadMail']={}
    db['bandeja']={}
    pickle.dump(db, f)
    f.close()
def storeData(dic):
    # initializing data to be stored in db
    
     
    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')
     
    # source, destination
    pickle.dump(dic, dbfile)                    
    #dbfile.close()
 
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')    
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()
def run():
    return 0
    
if __name__=="__main__":
    write_file()
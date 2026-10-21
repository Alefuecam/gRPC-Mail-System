import pickle


a = {'hello': 'world'}
db={}
db['saturacion']={}
db['usuarios']={}
db['cantidadMail']={}
db['bandeja']={}
#print(a)
with open('filename.pickle', 'wb') as handle:
    pickle.dump(db, handle, protocol=pickle.HIGHEST_PROTOCOL)

#with open('filename.pickle', 'rb') as handle:
   # b = pickle.load(handle)
  #  print(b)
    #b['saturacion']=1
    #b['otro']='mundo'
    #with open('filename.pickle', 'wb') as handle:
     #   pickle.dump(b, handle, protocol=pickle.HIGHEST_PROTOCOL)
    #with open('filename.pickle', 'rb') as handle:
     #   c = pickle.load(handle)


#print(c)
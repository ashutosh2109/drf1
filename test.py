import  requests
BASE_URL= 'http://127.0.0.1:8000/'
ENDPOINT ='ash3/'
resp=requests.get(BASE_URL+ENDPOINT)     #put,delete,post
data=resp.json()
print(data)
# print('#' * 50)
# print ('emp no:',data['eno'])
# print ('emp name:',data['ename'])
# print ('emp sal:',data['esal'])
##########################################      or          ######################
# import  requests
# BASE_URL= 'http://127.0.0.1:8000/'
# ENDPOINT ='ash3'
# resp=requests.put(BASE_URL+ENDPOINT)
# data=resp.json()
# print(data)
# print('#' * 50)
# print ('emp no:',data['eno'])
# print ('emp name:',data['ename'])
# print ('emp sal:',data['esal'])
# #####################################          or        ##########################
# import  requests
# BASE_URL= 'http://127.0.0.1:8000/'
# ENDPOINT ='ash3'
# resp=requests.post(BASE_URL+ENDPOINT)
# data=resp.json()
# print(data)
#################################           or         ################################
# import  requests
# BASE_URL= 'http://127.0.0.1:8000/'
# ENDPOINT ='ash3'
# resp=requests.put(BASE_URL+ENDPOINT)
# data=resp.json()
# print(data)
#
#

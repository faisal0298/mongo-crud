### temporary file 
#  password: admin@123

import copy
import pymssql
import time
import requests
from lxml.etree import fromstring
import os
from io import StringIO



buffer = StringIO()

headerdata = {'Content-Type': 'application/x-www-form-urlencoded'}


cnxn = pymssql.connect(
                      host="127.0.0.1",
                      user="sa",
                      password="admin@123",
                      database="TestDB")

cursor = cnxn.cursor()

def signIn(username="admin", password="admin",ip="192.168.1.190"):
    global Username, Password, headerdata
    ip = ip
    payload=f'Username={username}&Password={password}'
    url = f"http://{ip}/Security/UserAuth"

    response = requests.request("PUT", url, headers=headerdata, data=payload)
    response = fromstring(response.text.encode('utf-8'))
    elm = response.xpath('/ResponseStatus/statusCode').pop()
    testId = elm.text
    if testId == "0":
        Username = username
        Password = password
        headerdata["Authorization"] = "Basic {}".format(encode_header(Username, Password))
        return "Success"
    return "failed"    

import base64
def encode_header(Username,Password):
    message = "{}:{}".format(Username, Password)
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


signIn()

def addNewPersonAndFace(ip, name, sex, certificateid, groupid, 
                country,address, birthdate,image):

    global headerdata

    # buffer.write(open(f"{image}",'rb').read())

    payload = {'IgnoreError': 'false',
               'Name': name,
               'Sex': sex,
               'CertificateType': 'IC',
               'CertificateID': certificateid,
               'GroupID': groupid,
               'Country': country,
               'Address': address,
               'Birthday': birthdate,
               'FaceImageID': '1'}

    newheaders = copy.copy(headerdata)
    del newheaders["Content-Type"]


    url = f"http://{ip}/FaceGroup/AddPersonInfoAndFaceImage"
    try:
        files = [
        ('file', ('my_file.jpg', image, 'image/jpeg'))]
        response = requests.request(
            "POST", url, headers=newheaders, data=payload, files=files)
        print(response.content)
        response = fromstring(response.text.encode('utf-8'))
        
        elm = response.xpath('/ResponseStatus/statusCode').pop()
        testId = elm.text
        if testId == "4111" :
            print ("already exist")
        if testId == "0":
            print ("success")
        if testId == "4099" :
            print ("Image above 250 kb")
    except Exception as e:
        print (e," Unable to Reach Server ")


  
# image = open(f'/home/diycam/Downloads/Sachin.jpeg',"rb")

finaldata=[]
while True:
    cursor.execute("SELECT count(*) FROM facedata")
    count=cursor.fetchall()[0][0]
    if count > len(finaldata)   :
        cursor.execute("SELECT * FROM facedata;")
        for i in cursor:
            finaldata.append({"Mobile":i[0],"ClientName":i[1],"Email":i[2],"Address":i[3],
            "image":i[4]})
            addNewPersonAndFace("192.168.1.190", i[1],
                                "other",i[0],"2","India",i[3], "31/01/2023",i[4])
    time.sleep(3)


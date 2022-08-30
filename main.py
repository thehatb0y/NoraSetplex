import nora

def main():
    #Service Token
    token = "token"
    #Service JSessionID
    jsessionid = "jsessionid"
    #Service StreamName
    streamname = "servicename"
    #Customer Test
    customerID =  "id"
    #Set the date to receive the credit 
    data= "2022-08-06T18:58"
    data = data[:-6]
    #nora.noracheck(token, jsessionid, streamname, data, 1)
    nora.duplicate(streamname, token, jsessionid, customerID)
    
if __name__ == "__main__":
    main()

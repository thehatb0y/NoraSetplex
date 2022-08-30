import nora

def main():
    #Service Token
    token = "073827bd-b6ae-4541-b178-bbc4b74d6b97"
    #Service JSessionID
    jsessionid = "ZThiNjU3ZTctMjA2Mi00ZWRlLWJkNTctMzI2MTNhYjdiNjA1"
    #Service StreamName
    streamname = "unlimitedstreams"
    #Customer Test
    customerID =  30189254
    #Set the date to receive the credit 
    data= "2022-08-06T18:58"
    data = data[:-6]
    #nora.noracheck(token, jsessionid, streamname, data, 1)
    nora.duplicate(streamname, token, jsessionid, customerID)
    
if __name__ == "__main__":
    main()

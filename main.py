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
    daysToGive = 1
    

    r = 99
    while r != 0:
        print("Choose an option: ")
        print("0 to exit")
        print("1 to add time to a customer")
        print("2 to duplicate a customer")
        print("3 to export to Json")

        r = int(input())
        if r == 3:
            print("Copying...")
            nora.noraJsonExport(token, jsessionid, streamname, data, daysToGive)
            print("Exporting Complete")
        elif r == 2:
            print("Type Customer ID")
            customerID = int(input())
            nora.duplicate(streamname, token, jsessionid, customerID)
        elif r == 1:
            print("Type How Many Days To Give")
            daysToGive = int(input())
            nora.noracheck(token, jsessionid, streamname, data, daysToGive)
        elif r == 0:
            print("Exiting...")
            exit()
        
if __name__ == "__main__":
    main()


import random
import threading
import requests
import time

def set_header(token, jessionid, streamname, userid, addtime, duplicate, checkuser):
    header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-XSRF-TOKEN': token,
    'Origin': 'https://'+ streamname +'.norago.tv',
    'Content-Type': 'application/json;charset=utf-8',
    'Connection': 'keep-alive',
    'Referer': 'https://'+ streamname + '.norago.tv/nora/subscribers',
    'Cookie': 'XSRF-TOKEN='+ token +'; JSESSIONID='+ jessionid +'',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors', 
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
    }
    if addtime == True:
        header['Referer'] = 'https://'+ streamname +'.norago.tv/nora/subscribers/'+ str(userid) +'/activation'
    elif checkuser == True:
         header['Referer'] = 'https://'+ streamname +'.norago.tv/nora/subscribers/'+ str(userid) +''
    elif duplicate == True:
         header['Referer'] = 'https://'+ streamname +'.norago.tv/nora/subscribers/new'
    return header

def set_setSubPayload(subscriberid, daystogive):
   return "{\"approvalRequired\":false,\"currencyConverterType\":\"FIXER_IO\",\"currencyId\":14001,\"paymentKey\":null,\"subscriberId\":"+ str(subscriberid) + ",\"addOnIds\":[],\"autoPay\":false,\"comment\":null,\"devicesToPay\":4,\"length\":" + str(daystogive) + ",\"lengthType\":\"Days\",\"override\":true,\"paymentType\":\"Custom_Subscription\",\"price\":0,\"subscriptionId\":null,\"checkNumber\":null,\"creditCardId\":null,\"externalPaymentSystemType\":null,\"paymentSystemType\":\"CASH\",\"transactionId\":null,\"location\":null}"
 
def set_duplicateAccPayload(username, password, firstname, lastname, email, phone, address, city, zip, coutry):
    return "{\"id\":null,\"name\":\""+username+"\",\"accountNumber\":null,\"address\":\""+address+"\",\"city\":\""+city+"\",\"country\":\""+coutry+"\",\"creditCards\":[],\"currentPaymentStatement\":null,\"customChannels\":[],\"customVods\":[],\"dateOfBirth\":null,\"devices\":[],\"deviceSlots\":[],\"email\":\""+email+"\",\"enabled\":null,\"expirationTime\":null,\"firstname\":\""+firstname+"\",\"language\":null,\"lastAccess\":null,\"lastname\":\""+lastname+"\",\"network\":{\"id\":10000142,\"name\":\"R2\",\"backgroundColor\":null,\"categorySets\":[],\"customVideoUrl\":null,\"deviceCount\":0,\"listingType\":\"Sequence\",\"networkCatchupLinks\":[],\"networkChannelLinks\":[],\"networkThemeLinks\":[],\"overlays\":[],\"pincode\":\"1234\",\"platforms\":null,\"prefix\":\"RTWO\",\"startPageType\":null,\"staticChannel\":null,\"screenSaver\":null,\"subscriberCount\":null,\"subscribers\":[],\"timezone\":null,\"voucherSubscribersAllowed\":false,\"logoUrl\":null},\"notes\":[],\"password\":\""+password+"\",\"paymentStatements\":[],\"phone\":\""+phone+"\",\"pincode\":\"1234\",\"registered\":null,\"state\":\"null\",\"timeZone\":\"America/New_York\",\"user\":null,\"zipcode\":\""+zip+"\",\"type\":null}"

def set_url(page, streamname):
    return f'https://{streamname}.norago.tv/nora/api/subscribers/?count=1000&disabled=&new=&page={page}&sort-by=lastName&sort-order=asc'

def set_urlSubs(subid, streamname):
    return f"https://{streamname}.norago.tv/nora/api/subscribers/{subid}/payments" 

def set_checkCustomerUrl_subs(subid, streamname):
    return f"https://{streamname}.norago.tv/nora/api/subscribers/{subid}" 

def set_subscribersUrl_subs(streamname):
    return f"https://{streamname}.norago.tv/nora/api/subscribers/" 

def set_deviceSlotUrl(subid, streamname):
    return f"https://{streamname}.norago.tv/nora/api/subscribers/{subid}/slots/"

def add_time(response, streamname, token, jsessionid, daystogive, fromp):
    received_credit = 0
    for contact in response.json()['content']['content']:
        if contact['expirationTime'] != None:
            if contact['expirationTime'][:-6] == fromp:
                received_credit += 1
                requests.request("POST", 
                    set_urlSubs(contact['id'], streamname), 
                    headers = set_header(token, jsessionid, streamname, contact['id'], True, False, False),
                    data = set_setSubPayload(contact['id'], daystogive)
                )
                #create a text file with the customer id's that have been added time to
                with open('customerid.txt', 'a') as f:
                    f.write("\nID: " + str(contact['id']) + " Name: "+ str(contact['firstName']))
                    f.close()
    print(f"Received credit: {received_credit}")
    
def duplicate(streamname, token, jsessionid, customerID):
    r = requests.get(set_checkCustomerUrl_subs(customerID, streamname), headers=set_header(token, jsessionid, streamname, 0, False, False, True))
    if r.status_code == 200:
        r = r.json()
        password = str(random.randint(100000000, 999999999))

        resp = requests.request("POST", 
        set_subscribersUrl_subs(streamname), 
        headers = set_header(token, jsessionid, streamname, customerID, False, True, False),
        data = set_duplicateAccPayload(str(int(r['name'])+2), password, r['firstname'], r['lastname']+"2", r['email'], r['phone'], r['address'], r['city'], r['zipcode'], r['country'])
        )
        print("Username: " + str(int(r['name'])+2) + " Password: "+ password)
        resp = resp.json()
        
        for i in range(4):
            requests.request("POST", 
            set_deviceSlotUrl(resp['id'], streamname), 
            headers = set_header(token, jsessionid, streamname, resp['id'], True, False, False),
            data = set_duplicateAccPayload(str(int(r['name'])+2), password, r['firstname'], r['lastname']+"2", r['email'], r['phone'], r['address'], r['city'], r['zipcode'], r['country'])
            )
        
        requests.request("POST", 
            set_urlSubs(resp['id'], streamname), 
            headers = set_header(token, jsessionid, streamname, resp['id'], True, False, False),
            data = set_setSubPayload(resp['id'], 30)
            )
    else:
        exit()

def noracheck(token, jsessionid, streamname, fromp, daystogive):
    #Page num, starts in 0
    page = 0
    #Check if connection is working, if == 200 get the total pages
    response = requests.get(set_url(page, streamname), headers=set_header(token, jsessionid, streamname, 0, False, False, False))
    if response.status_code == 200:
        total_pages = response.json()['content']['totalPages']
    else:
        print(response.status_code)
        exit()

    time_init = time.time() 
    #Run all pages and check  through all the customerers. 
    #Each page holds 1000 customers
    for page in range(page, total_pages + 1):
        print(f"Scrapping page {page}")
        #t = threading.Thread(target=duplicate, args=(response, streamname, token, jsessionid))
        t = threading.Thread(target=add_time, args=(response, streamname, token, jsessionid, daystogive, fromp))
        t.start()
        response = requests.get(set_url(page, streamname), headers=set_header(token, jsessionid, streamname, 0, False, False, False))
        page = response.json()['content']['number']
    
    while (threading.active_count() > 1):
        time.sleep(1)

    time_end = time.time()
    print(f'Total time elapsed: {time_end - time_init}')   

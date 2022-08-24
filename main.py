import requests
from concurrent.futures import ThreadPoolExecutor
import time
import header

def main():
    #Service Token
    token = "token"
    #Service JSessionID
    jsessionid = "jsessionid"
    #Service StreamName
    streamname = "streamname"
    #Page num, starts in 0
    page = 0
    #Customers that received credit, starts in 0
    received_credit = 0

    #Customer Test
    customerID =  30189254
    #Set the date to receive the credit 
    data= "2022-08-06T18:58"
    data = data[:-6]

    #Check if connection is working, if == 200 get the total pages
    response = requests.get(nora.set_url(page, streamname), headers=nora.set_header(token, jsessionid, streamname, 0, False, False, False))
    if response.status_code == 200:
        total_pages = response.json()['content']['totalPages']
    else:
        print(response.status_code)
        exit()

    time_init = time.time() 
    #Run all pages and check  through all the customerers. 
    #Each page holds 1000 customers
    for page in range(0, total_pages + 1):
        print(f"Scrapping page {page}")
        for contact in response.json()['content']['content']:
            if contact['expirationTime'] != None:
                #if contact['id'] ==  customerID:
                if contact['expirationTime'][:-6] == data:
                    #r = requests.get(nora.set_checkCustomerUrl_subs(contact['id'], streamname), headers=nora.set_header(token, jsessionid, streamname, 0, False, False, True))
                    #r = r.json()

                    #requests.request("POST", 
                    #    nora.set_subscribersUrl_subs(streamname), 
                    #    headers = nora.set_header(token, jsessionid, streamname, contact['id'], False, True, False),
                    #    data = nora.set_duplicateAccPayload(str(r['name'])+"3", str(111111), r['firstname'], r['lastname']+"3", r['email'], r['phone'], r['address'], r['city'], r['zipcode'], r['country'])
                    #)
                    #exit()
                    requests.request("POST", 
                        nora.set_url_subs(contact['id'], streamname), 
                        headers = nora.set_header(token, jsessionid, streamname, contact['id'], False, False, False),
                        data = nora.set_setSubPayload(contact['id'], 2)
                    )
                    received_credit += 1
        response = requests.get(nora.set_url(page, streamname), headers=nora.set_header(token, jsessionid, streamname, 0, False, False, False))
        page = response.json()['content']['number']
    time_end = time.time()
    print(f'Total time elapsed: {time_end - time_init}')
    print(f'Total Customer that received credit: {received_credit}')
    
if __name__ == "__main__":

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

    #Set the date to receive the credit 
    data= "2022-08-06T18:58"
    data = data[:-6]

    #Check if connection is working, if == 200 get the total pages
    response = requests.get(header.set_url(page, streamname), headers=header.set_header(token, jsessionid, streamname))
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
                if contact['expirationTime'][:-6] == data:
                    print("Customerid:"+contact['id'])  
                    response = requests.request("POST", 
                        header.set_url_subs(contact['id'], streamname), 
                        headers = header.set_onedaypayload_header(token, jsessionid, contact['id'], streamname),
                        data = header.set_onedaypayload(contact['id'])
                    )
                    received_credit += 1
        response = requests.get(header.set_url(page, streamname), headers=header.set_header(token, jsessionid, streamname))
        page = response.json()['content']['number']
    time_end = time.time()
    print(f'Total time elapsed: {time_end - time_init}')
    print(f'Total Customer that received credit: {received_credit}')
    
if __name__ == "__main__":
    main()
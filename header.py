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


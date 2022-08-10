def set_header(token, jessionid, streamname):
    header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-XSRF-TOKEN': 'token',
    'Connection': 'keep-alive',
    'Referer': 'https://streamname.norago.tv/nora/subscribers',
    'Cookie': 'XSRF-TOKEN=token; JSESSIONID=jsessionid',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
    }
    header['X-XSRF-TOKEN'] = token
    header['Cookie'] = 'XSRF-TOKEN=' + token + '; JSESSIONID=' + jessionid
    header['Referer'] = 'https://'+ streamname + '.norago.tv/nora/subscribers'
    return header

def set_onedaypayload(subscriber_id):
    onedaypayload= "{\"approvalRequired\":false,\"currencyConverterType\":\"FIXER_IO\",\"currencyId\":14001,\"paymentKey\":null,\"subscriberId\":"+ str(subscriber_id) + ",\"addOnIds\":[],\"autoPay\":false,\"comment\":null,\"devicesToPay\":4,\"length\":1,\"lengthType\":\"Days\",\"override\":true,\"paymentType\":\"Custom_Subscription\",\"price\":0,\"subscriptionId\":null,\"checkNumber\":null,\"creditCardId\":null,\"externalPaymentSystemType\":null,\"paymentSystemType\":\"CASH\",\"transactionId\":null,\"location\":null}"
    return onedaypayload

def set_onedaypayload_header(token, jessionid, subscriberid, streamname):
    onedaypayload_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'pt-PT,pt;q=0.8,en;q=0.5,en-US;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json;charset=utf-8',
    'X-XSRF-TOKEN': 'token',
    'Origin': 'https://streamname.norago.tv',
    'Connection': 'keep-alive',
    'Referer': 'https://streamname.norago.tv/nora/subscribers/userid/activation',
    'Cookie': 'XSRF-TOKEN=token; JSESSIONID=jsessionid',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
    }
    onedaypayload_header['X-XSRF-TOKEN'] = token
    onedaypayload_header['Cookie'] = 'XSRF-TOKEN=' + token + '; JSESSIONID=' + jessionid
    onedaypayload_header['Referer'] = 'https://'+ streamname +'.norago.tv/nora/subscribers/' + str(subscriberid) + '/activation'
    onedaypayload_header['Origin'] = 'https://'+ streamname+ '.norago.tv'
    return onedaypayload_header

def set_url(page, streamname):
    url = f'https://{streamname}.norago.tv/nora/api/subscribers/?count=1000&disabled=&new=&page={page}&sort-by=lastName&sort-order=asc'
    return url

def set_url_subs(subid, streamname):
    url = f"https://{streamname}.norago.tv/nora/api/subscribers/{subid}/payments" 
    return url


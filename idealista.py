from http.client import Http

def get_oauth_token():
    http_obj = Http()
    url = "https://api.idealista.com/oauth/token"
    apikey= urllib.parse.quote_plus('e33zj325kwm2t4kwgza24q0zgdupqpnn')
    secret= urllib.parse.quote_plus('5zuQXuimFqOi')
    auth = base64.encode(apikey + ':' + secret)
    body = {'grant_type':'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Authorization' : 'Basic ' + auth}
    resp, content = http_obj.request(url,method='POST',headers=headers, body=urllib.parse.urlencode(body))
    return content

def search_api(token):
    http_obj = Http()
    url = "http://api.idealista.com/3.5/es/search?center=40.42938099999995,-3.7097526269835726&country=es&maxItems=50&numPage=1&distance=452&propertyType=bedrooms&operation=rent"
    headers = {'Authorization' : 'Bearer ' + token}
    resp, content = http_obj.request(url,method='POST',headers=headers)
    return content
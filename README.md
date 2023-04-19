# quotexapi
Quotex API  
Website    : https://autotradevip.com/en/  
Olmyptrade : https://youtu.be/zTZT7zDlmtU  
Binomo     : https://youtu.be/ww9rVMX5TK4  
IQ Option  : https://youtu.be/4i3YUEDRGWY  
Quotex     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA  
Expert Option     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA

### Import
```python
from quotexapi.stable_api import Quotex
```

### Support Login !
if connect sucess return True,None  

if connect fail return False,reason  
```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=account.connect()
print(check_connect,message)
```
### Login by pass PIN-Code !
```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=API.connect()
    API.change_balance("PRACTICE")
    if message == "PIN-code":
        print('##### PIN-code enabled #####')
        code_pin = input("Disable PIN-code from account settings: ")
        check_connect, message = API.connect_2fa(code_pin)

        print('##### second try #####')
        print('Status :', check_connect)
        print('Message :', message)
        print("Email :", API.email)
        account.close()
    
    if check_connect == True:
        print('Status :', check_connect)
        print('Message :', message)
        print("Email :", API.email)
        print("Balance:", account.get_balance())
        print("Balance:", account.get_balance_v2())
        account.close()
    else:
        print('########## Invalid email or password ')
        print('Status :', check_connect)
        print('Message :', message)
        print("Email :", API.email)
        account.close()
    
```
### Get Balance

```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=account.connect()
account.change_balance("PRACTICE")
balance=account.get_balance()
print(balance)
account.close()
```

### Get Balance V2

```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=account.connect()
account.change_balance("PRACTICE")
balance=account.get_balance_v2()
print(balance)
account.close()
```

### Buy
```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check,message=account.connect()
if check:
    account.change_balance("PRACTICE")
    asset="EURUSD"
    amount=1
    dir="call"#"call"/"put"
    duration=60#sec
    print(account.buy(asset,amount,dir,duration))
    account.close()
```


### Check_win & buy sample

```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=account.connect()
if check_connect:
    account.change_balance("PRACTICE")#"REAL"
    id = API.buy("AUDCAD_otc", "14000", "put", "60")
    print(API.check_win(id))
```

### Get Candle
```python
asset="AUDCAD_otc"
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check,message=account.connect()
if check:
    _time=int(time.time())#the candle end of time
    offset=3600#how much sec want to get     _time-offset --->your candle <---_time
    period=60#candle size in sec
    print("You will get the candle from: "+str(_time-offset)+" to: "+str(_time))
    print("------\n")
    candle=account.get_candle(asset,_time,offset,period)
    for c in candle["data"]:
        print(c)
    API.close()
```

### Get Candle V2
```python
asset="AUDCAD_otc"
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=account.connect()
print(check_connect,message)
if check_connect: 
    print("\n\n------get")
    a=account.get_candle_v2("AUDCAD_otc",60)
    for c in a:
        print(c)
    account.close()
```

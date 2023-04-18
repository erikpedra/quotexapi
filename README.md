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
check_connect,message=account.connect()
if message == "PIN-code":
    print('##### PIN-code enabled #####')
    code_pin = input("Disable PIN-code from account settings: ")
    check_connect, message = api.connect_2fa(code_pin)

    print('##### second try #####')
    print('Status :', check_connect)
    print('Message :', message)
    print("Email :", account.email)
    
print("Balance:", account.get_balance())
print("##############################")
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

### Buy Multi

```python
from quotexapi.stable_api import Quotex
account=Quotex(host="broker-qx.com",email="user@gmail.com", password="pwd")
check_connect,message=account.connect()
account.change_balance("PRACTICE")#"REAL"
if check_connect:
    account.change_balance("PRACTICE")#"REAL"
    API.buy_multi("AUDCAD_otc", "14000", "put", "60" , 5) #5 trade
```

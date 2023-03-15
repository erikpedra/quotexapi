# python
from quotexapi.api import QuotexAPI
import quotexapi.global_value as global_value
import threading
import time
import logging
import operator
from collections import defaultdict
from collections import deque
import json
import requests

def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))

class Quotex:
    __version__ = '2.1'
    def __init__(self, email=None, password=None, set_ssid=None, host=None, user_agent=None, cf_bm=None, proxies=None, auto_logout=True):
        self.size = [1, 5, 10, 15, 30, 60, 120, 300, 600, 900, 1800,
                    3600, 7200, 14400, 28800, 43200, 86400, 604800, 2592000]
        self.set_ssid = set_ssid
        self.proxies = proxies
        self.auto_logout = auto_logout
        self.email = email
        self.password = password
        self.account_mode_isDemo = 1
        self.client_callback = None
        
    
        
    def logout(self):
        pass
    
    def ping_server_go(self):
        pass
    
    def ping_to_server_go_2(self):
        pass
    
    def set_call_back_for_client(self, function):
        pass
    
    def get_ssid(self):
        pass
        
    def change_account(self, Balance_MODE):
        """Change active account `real` or `practice`"""
        real_id = None
        practice_id = None
        if Balance_MODE == "REAL":
            pass
        elif Balance_MODE == "PRACTICE":
            pass
        else:
            logging.error("ERROR doesn't have this mode")
            exit(1)
            
    def get_balance(self):
        pass
        

    def get_balances(self):
        pass
            
    # _____________________BUY________________________________

    # __________________FOR OPTION____________________________
    def buy(self, asset, amount, dir, duration):
        """ Buy Binary option""""
        pass
      
    def sell_option(self, options_ids):
        pass
    
    def check_win_raw(self, ticket, c_function):
        pass
        
    def check_win(self, ticket, polling = (1,)):
        """Check win based id""""
        time.sleep(polling)
        pass
      
    def get_signal_data(self):
      """ Get signal Quotex server""""
        pass
      
    def get_payment(self):
        """ payment Quotex server""""
        pass
    def check_user_data(self):
        laravel_session = self.api.response_cookies['laravel_session']
        cookies_dict = {
            'laravel_session': laravel_session }
        pass
      
      
    # ________________________________________________________________________
    # _______________________        CANDLE      _____________________________
    # ________________________self.api.getcandles() wss________________________
    def get_candles(self, asset, time, offset, period):
        while True:
            try:
                pass
            except:
                logging.error('**error** get_candles need reconnect')
                self.connect() #go connect
                
    def get_candle_v2(self, asset, period)):
        while True:
            try:
                pass
            except:
                logging.error('**error** get_candle_v2 need reconnect')
                self.connect() #go connect
                
                
    def start_candles_stream(self, asset, size):
        pass
    def stop_candles_stream(self, asset):
        pass
      
      
      
    #######################################################
    # ______________________________________________________
    # _____________________REAL TIME CANDLE_________________
    # ______________________________________________________
    #######################################################
    def get_realtime_candles(self, asset):
        if asset in self.api.realtime_price and len(self.api.realtime_price[asset]) > 0:
            return self.api.realtime_price[asset]
           
      
      
    def connect(self):
        try:
            self.api.close()
        except:
            pass
            # logging.error('**warning** self.api.close() fail')
        self.api = QuotexAPI("quotex.market", self.set_ssid)
        check = None
        check, reason = self.api.connect()
        if check == True:
            
            return True, None
        else:
            return False, reason
          
    def close(self):
        try:
            self.api.close()
        except:
            pass
          
    def check_connect(self):
        # True/False
        # if not connected, sometimes it's None, sometimes its '0', so
        # both will fall on this first case
        if not global_value.check_websocket_if_connect:
            return False
        else:
            return True

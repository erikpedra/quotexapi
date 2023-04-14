"""Module for IQ option websocket."""

import simplejson as json
import logging
import websocket
import quotexapi.global_value as global_value

class WebsocketClient(object):
    """Class for work with Quotex API websocket."""

    def __init__(self, api):
        """
        :param api: The instance of :class:`QuotexAPI
            <quotexapi.api.QuotexAPI>`.
        """
        self.api = api
        self.status = ''
        self.message_clos = '451-["s_orders/close",{"_placeholder":true,"num":0}]'
        self.message_cancel = '451-["s_orders/cancel",{"_placeholder":true,"num":0}]'
        self.cookie_token = 'referer=httpsd%3A%2F%2Fwww.google.com%2F;__cf_bm=' + self.api.cf_bm
        self.wss = websocket.WebSocketApp(
            self.api.wss_url, on_message=self.on_message,
            on_error=self.on_error, on_close=self.on_close,
            on_open=self.on_open,header=self.api.header,cookie=self.cookie_token)

    def on_message(self, wss, raw_message): # pylint: disable=unused-argument
        """Method to process websocket messages."""
        global_value.ssl_Mutual_exclusion=True
        logger = logging.getLogger(__name__)
        logger.debug(raw_message)
        if self.api.client_callback != None:
            self.api.client_callback(raw_message)
        if raw_message == '40' and global_value.check_auth_finish[id(wss)] == False:
            logger.debug(global_value.SSID[self.api.object_id])
            wss.send(global_value.SSID[self.api.object_id])
            global_value.auth_send_count[self.api.object_id] = global_value.auth_send_count[self.api.object_id] + 1
        if isinstance(raw_message, str) and '451-' in raw_message:
            self.api._temp_status = str(raw_message)
        try:
            if self.api._temp_status == '451-["settings/list",{"_placeholder":true,"num":0}]':
                self.api.settings_list = json.loads(raw_message[4:])
                self.api._temp_status = ''
            elif self.api._temp_status == '451-["history/list/v2",{"_placeholder":true,"num":0}]':
                tt = json.loads(raw_message[1:])
                self.api.candle_v2_data[tt['asset']] = tt['history']
                self.api._temp_status = ''
        finally:
            pass
        if raw_message == '42["s_authorization"]':
            global_value.check_websocket_if_connect[id(wss)] = 1
            global_value.check_auth_finish[id(wss)] = True
        try:
            ok_json = json.loads(raw_message[1:])
            if 'balance' in ok_json:
                if ok_json['isDemo'] == 0:
                    global_value.real_balance[id(wss)] = ok_json['balance']
                elif ok_json['isDemo'] == 1:
                    global_value.practice_balance[id(wss)] = ok_json['balance']
            if 'liveBalance' in ok_json and 'demoBalance' in ok_json:
                global_value.practice_balance[id(wss)] = ok_json['demoBalance']
                global_value.real_balance[id(wss)] = ok_json['liveBalance']
            if 'requestId' in ok_json:
                self.api.request_data[str(ok_json['requestId'])] = ok_json
            if self.status == self.message_clos:
                try:
                    pass
                finally:
                    pass
                self.status = ''
                if self.status == self.message_cancel:
                    self.api.check_win_refund_data[ok_json['ticket']] = ok_json
                    self.status = ''
                if raw_message == self.message_clos or raw_message == self.message_cancel:
                    self.status = raw_message
        except:
            pass
        global_value.ssl_Mutual_exclusion=False


    @staticmethod
    def on_error(wss, error):  # pylint: disable=unused-argument
        """Method to process websocket errors."""
        logger = logging.getLogger(__name__)
        logger.error(error)
        global_value.websocket_error_reason = str(error)
        global_value.check_websocket_if_error = True
        

    @staticmethod
    def on_open(wss):  # pylint: disable=unused-argument
        """Method to process websocket open."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket client connected.")
        global_value.check_websocket_if_connect = 1

    @staticmethod
    def on_close(wss, close_status_code, close_msg):  # pylint: disable=unused-argument
        """Method to process websocket close."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket connection closed.")
        global_value.check_websocket_if_connect = 0

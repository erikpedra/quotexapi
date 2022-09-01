"""Module for base Quotex base websocket chanel."""

class Base(object):
    """Class for base Quotex websocket chanel."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of :class:`QuotexAPI
            <quotexapi.api.QuotexAPI>`.
        """
        self.api = api
    
    def send_websocket_request(self, data):
        """Send request to Quotex server websocket.
        :param str name: The websocket chanel data.
        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_websocket_request(data)

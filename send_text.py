# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:34:49 2016

@author: Javid
"""

from twilio.rest import TwilioRestClient

account_sid = "ACf72a99e89029fa165158bf10eb554ec1" # Your Account SID from www.twilio.com/console
auth_token  = "795ca5b5dd1b8b28768dc82771f1ca9e"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Qaqas o qizdan uzaq dur yaxsi olmaz senin ucun",
    to="+994505044015",    # Replace with your phone number
    from_="+19073127193") # Replace with your Twilio number

print(message.sid)
TDA-API token generator for Python

This is a simple Python script to generate a token for the TDAmeritrade API.
It uses the tda-api package to generate the token, then returns it in JSON format.
It can then be copied and pasted out of the resulting window.

The main reason this was written was to be used in conjunction with the
TradeConnect software which requires a token to be generated and pasted into
the user control panel for manual authentication. However, this script
can be used to generate a token for any use with the TDAmeritrade API.

Before you can use this script, you must first register an application with
TDAmeritrade. See this for more information: https://tda-api.readthedocs.io/en/latest/getting-started.html#td-ameritrade-api-access

The only user setting is the callback URL to set in the config.py file. This callback URL
is the same URL you set when you create your app in the TDAmeritrade developer portal. These
URLs MUST match exactly, or you will receive an error upon opening the Chrome window.
See here for information on this: https://tda-api.readthedocs.io/en/latest/auth.html#a-third-party-application-may-be-attempting-to-make-unauthorized-access-to-your-account

You will also want to make sure you have the latest version of Google Chrome, and the latest
version of the Chromedriver executable installed in the same directory as app.py. The Chromedriver
executable can be downloaded from https://chromedriver.chromium.org/downloads.

When you start the program you will need to enter your TDAmeritrade API Key
from the developer portal (it may say 'Consumer Key'). Click continue and
the script will open a Chrome browser window. You will need to log in to
your TDAmeritrade account and authorize the app. You may need to enter a
code that is sent to your phone. Once you have authorized the app, the
script will close the browser window (you may briefly see an error screen) and
then return the token in JSON format that you can copy out of the window with
keyboard commands.

Written by Anthony Garcia of Sirius Technology, LLP.
Distributed freely.

www.gettradeconnect.com to connect TradingView to your
TDAmeritrade brokerage account!
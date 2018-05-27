"""
Shows basic usage of the Google Calendar API. Creates a Google Calendar API
service object and outputs a list of the next 10 events on the user's calendar.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
import pprint

# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

calendars = service.calendarList().list().execute().get('items', [])
pp = pprint.PrettyPrinter(indent=4)
##pp.pprint(calendars)
for calendar in calendars:
    print("{} {}".format(calendar['id'],calendar['summary']))

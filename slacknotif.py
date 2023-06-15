import urllib3
import os
import json
import traceback

WH_token = os.environ['SLACK']
slack_link = 'https://hooks.slack.com/services/' + WH_token

def slacknotif(msg):
  try:
    slack_msg = {'text': msg}
    link = urllib3.PoolManager()
    resp = link.request('POST',
                        slack_link,
                        body = json.dumps(slack_msg),
                        headers = {'Content-Type': 'application/json'},
                        retries = False)
  except:
    traceback.print_exc()

  return True

if (__name__ == '__main__'):
  import sys
  msg = "Module slacknotif test"
  if len(sys.argv) > 1:
    msg = sys.argv[1]
  slacknotif(msg)


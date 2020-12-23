import requests
import urllib3
import json
from st2common.runners.base_action import Action

class BaseAction(Action):
    def send_msg_teams(self,message):
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            result = requests.post("https://outlook.office.com/webhook/98bb3c69-bf86-4282-ad99-"+
                                       "905510536594@8ee0f3e4-b788-4efa-bd84-e6bfe7fe9943/IncomingWebhook/3a859"+
                                       "e3172264df18ed76932e94a9ac9/7b4115f8-5f26-4852-af09-417a5f48b30f",
                                       json.dumps({"Text": message}), verify=False).text
            return True,"msg send"
        except Exception as e:
            return False,e



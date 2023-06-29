import requests
import json

class ConvoDAO:
    def __init__(self, convo_link):
        self.convo_link = convo_link

    def mask_session(self, session_id):
        form_data = {
            "unique_ID" : session_id
        }
        form_headers = {
            "Content-Type": "application/json"
        }
        res = requests.post(
            f"{self.convo_link}/convo-api/mask-session",
            json=form_data, 
            headers=form_headers
        )
        return res.json()

    def update_summary(self, session_id, question, id_hits, new_cum_sum_user, new_cum_sum_bot):
        form_data = {
            "unique_ID": session_id,
            "global_hits": id_hits,
            "new_cum_sum_user": new_cum_sum_user,
            "new_cum_sum_bot": new_cum_sum_bot
        }
        form_headers = {
            "Content-Type": "application/json"
        }
        res = requests.post(
            f"{self.convo_link}/convo-api/update-summary",
            json=form_data,
            headers=form_headers
        )
        return res.json()

    def update_status(self, session_id, isResolved, isClosed):
        form_data = {
            "unique_ID": session_id,
            "isResolved": isResolved,
            "isClosed": isClosed
        }
        form_headers = {
            "Content-Type": "application/json"
        }
        res = requests.post(
            f"{self.convo_link}/convo-api/update-status",
            json=form_data,
            headers=form_headers
        )
        return res.json()


class GlobalDAO:
    def __init__(self, global_link):
        self.global_link = global_link

    def get_keyword_hits(self, keywords):
        headers = {
            "Content-Type": "application/json"
        }
        keyword_data = {
            "keywords": keywords
        }
        resp = requests.get(
            f"{self.global_link}/global-api/keyword-hits",
            json=keyword_data,
            headers=headers
        )
        return resp.json()

    def get_feedback(self, status, id_hits):
        payload = {
            "id": id_hits
        }
        res = requests.get(
            f"{self.global_link}/global-api/{status}-feedback",
            json=payload,
            headers={
                "Content-Type": "application/json"
            }
        )
        return res.json()

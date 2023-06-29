import json
from tools.get_completion import get_completion

def cumulative_summary(unique_id,user_query,response,csum_bot,csum_user):
    summary_user_sofar = {user_query,csum_user}
    summary_bot_sofar = {response,csum_bot}
    
    prompt = f"""Your task is to generate a short summary separtely of the conversations and return it as a JSON object with object 1 as "user_summary_text" and object 2 as "chatbot_summary_text" strictly follow these names\ Summarize separtely the contents below, delimited by triple \ backticks in at most 50 words Sum: ```{summary_user_sofar}`` ```{summary_bot_sofar}"""


    result = get_completion(prompt,task="summary")
    status = result["status"]
    response = result["content"]
    if status == "working":
        data = json.loads(response)

        user_summary_text = data["user_summary_text"]
        chatbot_summary_text = data["chatbot_summary_text"]

        return_sum = {
            "status" : status,
            "unique_ID": unique_id,
            "new_cum_sum_user": user_summary_text,
            "new_cum_sum_bot": chatbot_summary_text
        }
        return return_sum
    else :
        return_sum = {
            "status" : status,
            "unique_ID": unique_id,
            "new_cum_sum_user": "",
            "new_cum_sum_bot": ""
        }
        return return_sum

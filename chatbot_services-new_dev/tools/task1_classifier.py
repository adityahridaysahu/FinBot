from tools.get_completion import get_completion
from tools.task3_classifier import task3_classifier
from tools.task2_classifier import task2_classifier
import requests

def task1_classifier(question, bonds_link,sentences,csum_bot,csum_user):

    # prompt to classify as bonds db or not
    prompt =f"""You are a support executive at Goldman Sachs (An investments banking company).

       Now, assume that you have access to a public database named "BondsDB" having some essential information of various

       bonds in the market.

          The information present in BondsDB includes "ISIN", "category", "currency_of_issue", "coupon_rate", "maturity"

            and, "isOfferedByGS". ISIN is a unique identifier for every bond, Category is the type of bond,

            currency_of_issue is the type of currency in which the bond is issued, CouponRate is the rate of the

            coupon for that particular bond, and isOfferedByGS tells us whether Goldman Sachs offers that bond or not.

           

            conditions to check if QUESTION is related to bondsDB:

       -if you think that the question require any statistical or numerical data.

       - if it is related to bondsDB schema such as ISIN, category, currency of issue, coupon rate, or maturity.




       if it is bondsDB related QUESTION write an SQL query to query the 'bonds' table in ANSWER format based on given such as ISIN, category, currency of issue, coupon rate, or maturity.

    ANSWER: [only SQL query] nothing else should be printed.

 else write NO as answer.




 QUESTION:{question}

           

             

           """

    result = get_completion(prompt)
    status = result["status"]
    bonds_text = result["content"]
    # print(f"p1 {result}")
    input_string = bonds_text

    sqlquery = False
    if input_string.find("SELECT") != -1:
        sqlquery = True
        if input_string[-1] != ';':
            bonds_text += ';'
    print(bonds_text)
    if status == "working" :
        if sqlquery:
            query = {
                "sql_query" : bonds_text
            }
            headers = {
                "Content-Type": "application/json"
            }
            resp = requests.post(
                f"{bonds_link}/bonds-api",
                json = query,
                headers = headers
            )
            df = resp.text
            print(df)
            # get a result in result_mysql
            classifier = task2_classifier(question, df, csum_bot, csum_user)
            print(f"p2 {classifier}")
            if classifier["status"] == "working":
                return {
                    "bonds_db" : "required",
                    "status" : classifier["status"],
                    "api_status" : status,
                    "result" : classifier["data"]
                }
            else :
                return {
                    "bonds_db" : "required",
                    "status" : classifier["status"],
                    "api_status" : status,
                    "result" : classifier["data"]
                }
        else :
            classifier = task3_classifier(question, sentences, csum_bot, csum_user)
            if classifier["status"] == "working":
                # print(f"p3 {classifier}")
                return {
                    "bonds_db" : "not required",
                    "status" : classifier["status"],
                    "api_status" : status,
                    "result" : classifier["result"]
                }
            else :
                return {
                    "bonds_db" : "not required",
                    "status" : classifier["status"],
                    "api_status" : status,
                    "result" : classifier["result"]
                }
    else:
        return {
            "bonds_db" : "processing",
            "status" : status,
            "api_status" : status,
            "result" : bonds_text
        }

from tools.get_completion import get_completion

def task2_classifier(question, result_mysql, csum_bot, csum_user):

    # return the bonds db string
    # prompt =f"""You are a support executive at Goldman Sachs (An investments banking company).
    
    # Assume that you are given the conversation history between you and the customer enclosed in 2 backticks in JSON format where the key is either bot or customer and the value is the corresponding cumulative summary is ``"bot": {csum_bot}, "customer": {csum_user}``.
    
    # Most importantly, you are provided with the output of an SQL query enclosed in 3 backticks ```{result_mysql}``` which contains the actual data that you have to format to produce the correct string output of this prompt.When asked with a 'which bond' question, consider the ISIN value as the bond identifier. 

    # Now use the information in this prompt along with the QUESTION to generate an accurate and precise answer for the specified QUESTION.  Assume that the data enclosed in 3 backticks is correct and complete and do not produce "insuffient data" as the output no matter what. 

    # QUESTION:{question}

    # """

    prompt =f"""You are a support executive at Goldman Sachs (An investments banking company).

       




 Result is answer to the QUESTION. Now ,utilise QUESTION,CSUMBOT and CSUMUSER to generate response to the query in proper english format.

 QUESTION:{question}

 CSUMBOT:{csum_bot}

 CSUMUSER:{csum_user}

 Result:{result_mysql}



"""

    result = get_completion(prompt)
    status = result["status"]
    string_text = result["content"]
    # print(f"p2 result : {string_text}")
    
    return {
        "status" : status,
        "data" : string_text,
    }
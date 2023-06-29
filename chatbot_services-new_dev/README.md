# chatbot_services

- Contains the backend software code of the application FinBot.
- The production hosted code is in the `new_dev` branch.

## Setup

```
git clone https://pscode.lioncloud.net/chatbot/chatbot_services
cd chatbot_services/
pip3 install -r requirements.txt
cp .env.sample .env
```

- Populate the `.env` file
- Run the following commands in different terminal instances

```
python3 global_routes.py
python3 convo_routes.py
python3 bond_routes.py
python3 central_routes.py

```

- `config.json` contains connection variables used by APIs, which need to be edited based on PROD or DEV.
- `.env.sample` contains the format and environment variables, the codebase expects a corresponding `.env` file.
- `.DockerFile` files contains the configurations used for creation of docker files for the APIs
- `coverage.xml` contains the backend coverage data based on unit tests in the `tests` directory.
- `sonar-project.properties` contains the SonarQube softwares mandatory configurations.
- `.yaml` and `.yml` files are used for CI/CD pipeline setup.

## APIs

There are four APIs, namely:
- Central API
- Convo API
- Global API
- Bonds API

For each API service, the code is divided into : 
- a DAO file that interacts with the database
- a service file that handles the business logic
- an external routes file which has the externally accessible routes

Note : 
- The ports on which these services run are defined inside the `_routes.py` file.
- The corresponding databases can be created using the `tables.sql` file.

## Tests

Contains selenium integration tests and other unit tests. 
The tests can be ran using :
```
python3 -m unittest discover tests
python3 integration_selenium.py --front frontend_link
```
## Tools 

Contains mutiple independent modular functions which are used by Flask APIs.

## Deployment

Contains deployspec files for deployment.

## Utilized questions 

- What are the types of investment?
- What is a bond in financial terms?
- What kinds of investment does Goldman Sachs allow?
- Which bond has the maximum maturity rate?
- What is the average coupon rate of bonds offered by Goldman Sachs?

## ConvoDAO Class

### Methods:

### `__init__(self, convo_link)`

- Description: Initializes a ConvoDAO object with a conversation link.
- Parameters:
    - `convo_link` (str): The link to the conversation.

### `mask_session(self, session_id)`

- Description: Masks a session ID.
- Parameters:
    - `session_id` (str): The unique ID of the session.
- Returns:
    - (dict): JSON response of the request.

### `update_summary(self, session_id, question, id_hits, new_cum_sum_user, new_cum_sum_bot)`

- Description: Updates the summary of a session.
- Parameters:
    - `session_id` (str): The unique ID of the session.
    - `question` (str): The question asked during the session.
    - `id_hits` (str): The hits ID for global keyword matches.
    - `new_cum_sum_user` (str): The new cumulative summary from the user's perspective.
    - `new_cum_sum_bot` (str): The new cumulative summary from the bot's perspective.
- Returns:
    - (dict): JSON response of the request.

### `update_status(self, session_id, isResolved, isClosed)`

- Description: Updates the status of a session.
- Parameters:
    - `session_id` (str): The unique ID of the session.
    - `isResolved` (bool): Flag indicating whether the session is resolved.
    - `isClosed` (bool): Flag indicating whether the session is closed.
- Returns:
    - (dict): JSON response of the request.

## GlobalDAO Class

### Methods:

### `__init__(self, global_link)`

- Description: Initializes a GlobalDAO object with a global link.
- Parameters:
    - `global_link` (str): The link to the global database.

### `get_keyword_hits(self, keywords)`

- Description: Retrieves keyword hits from the global database.
- Parameters:
    - `keywords` (list): The list of keywords to search for.
- Returns:
    - (dict): JSON response of the request.

### `get_feedback(self, status, id_hits)`

- Description: Retrieves feedback based on the status and hits ID.
- Parameters:
    - `status` (str): The status of the feedback ("positive" or "negative").
    - `id_hits` (str): The hits ID for global keyword matches.
- Returns:
    - (dict): JSON response of the request.

## Flask App

### Routes:

### `/`

- Description: Returns the endpoint for creating a new session or fetching data from a previous session.
- Method: GET
- Returns:
    - (str): The endpoint information.

### `/convo-api/update-status`

- Description: Updates the status of a session.
- Methods: GET, POST
- Returns:
    - (dict): JSON response of the request.

### `/convo-api/mask-session`

- Description: Masks a session ID or retrieves data from a previous session.
- Methods: GET, POST
- Returns:
    - (dict): JSON response of the request.

### `/convo-api/update-summary`

- Description: Updates the summary of a session.
- Methods: GET, POST
- Returns:
    - (dict): JSON response of the request.

## CentralService Class

### Methods:

### `__init__(self, convo_dao, global_dao)`

- Description: Initializes a CentralService object with ConvoDAO and GlobalDAO instances.
- Parameters:
    - `convo_dao` (ConvoDAO): An instance of the ConvoDAO class.
    - `global_dao` (GlobalDAO): An instance of the GlobalDAO class.

### `update_summary(self, delay, session_id, question, id_hits, response, csum_bot, csum_user)`

- Description: Updates the summary of a session asynchronously.
- Parameters:
    - `delay` (int): The delay between requests.
    - `session_id` (str): The unique ID of the session.
    - `question` (str): The question asked during the session.
    - `id_hits` (str): The hits ID for global keyword matches.
    - `response` (str): The response generated for the question.
    - `csum_bot` (str): The cumulative summary from the bot's perspective.
    - `csum_user` (str): The cumulative summary from the user's perspective.

### `summary_runner(self, session_id, question, id_hits, response, csum_bot, csum_user)`

- Description: Runs the summary update task asynchronously.
- Parameters:
    - `session_id` (str): The unique ID of the session.
    - `question` (str): The question asked during the session.
    - `id_hits` (str): The hits ID for global keyword matches.
    - `response` (str): The response generated for the question.
    - `csum_bot` (str): The cumulative summary from the bot's perspective.
    - `csum_user` (str): The cumulative summary from the user's perspective.
- Returns:
    - (coroutine): An awaitable coroutine.

### `process_request(self)`

- Description: Processes a request for the central service.
- Returns:
    - (dict): The processed output of the request.

## FeedbackService Class

### Methods:

### `__init__(self, convo_dao, global_dao)`

- Description: Initializes a FeedbackService object with ConvoDAO and GlobalDAO instances.
- Parameters:
    - `convo_dao` (ConvoDAO): An instance of the ConvoDAO class.
    - `global_dao` (GlobalDAO): An instance of the GlobalDAO class.

### `update_feedback(self, delay, status, hits)`

- Description: Updates the feedback asynchronously.
- Parameters:
    - `delay` (int): The delay between requests.
    - `status` (str): The status of the feedback ("positive" or "negative").
    - `hits` (str): The hits ID for global keyword matches.

### `feedback_runner(self, status, hits)`

- Description: Runs the feedback update task asynchronously.
- Parameters:
    - `status` (str): The status of the feedback ("positive" or "negative").
    - `hits` (str): The hits ID for global keyword matches.
- Returns:
    - (coroutine): An awaitable coroutine.

### `process_feedback(self)`

- Description: Processes feedback for the feedback service.
- Returns:
    - (dict): The processed output of the feedback request.

## `cumulative_summary` Function

Calculates the cumulative summary of conversations.

### Parameters

- `unique_id` (str): The unique ID of the conversation.
- `user_query` (str): The user's query.
- `response` (str): The chatbot's response.
- `csum_bot` (str): The cumulative summary from the bot's perspective.
- `csum_user` (str): The cumulative summary from the user's perspective.

### Returns

A JSON object containing the following properties:

- `status` (str): The status of the summary generation process.
- `unique_ID` (str): The unique ID of the conversation.
- `new_cum_sum_user` (str): The newly generated cumulative summary from the user's perspective.
- `new_cum_sum_bot` (str): The newly generated cumulative summary from the bot's perspective.

## `get_completion` Function

Generates completion for a given prompt using OpenAI's GPT-3.5 Turbo model.

### Parameters

- `prompt` (str): The prompt for which completion is requested.
- `task` (str, optional): The task for which completion is requested. Defaults to "classification".

### Returns

A JSON object containing the following properties:

- `status` (str): The status of the completion process.
- `content` (str): The generated completion content.

Please note that the OpenAI API key is required for using the `get_completion` function. You should set the API key as an environment variable named `OPENAI_API_KEY` before using the function. Additionally, ensure that you have the `openai` and `dotenv` packages installed in your Python environment.

## Function

Extracts keywords from a given sentence using NLTK (Natural Language Toolkit).

### Dependencies

- `nltk`: The Natural Language Toolkit library. You can install it using `pip install nltk`.

### Parameters

- `sentence` (str): The sentence from which keywords need to be extracted.

### Returns

A list of keywords extracted from the sentence.

The example above extracts keywords from the given sentence using the `keyword_extractor` function and prints the result.

Please note that the NLTK library and its required resources (e.g., stopwords corpus) should be installed. You may need to download additional resources using the NLTK's `nltk.download()` function if they haven't been downloaded yet.

## `task1_classifier` Function

This function is used to classify a question as related to the BondsDB database or not, and perform appropriate actions based on the classification.

### Dependencies

- `requests`: A library for making HTTP requests. You can install it using `pip install requests`.
- `tools.get_completion.get_completion`: A function for generating completions using OpenAI GPT-3.5 Turbo. Please refer to the documentation for the `get_completion` function for more details.
- `tools.task3_classifier.task3_classifier`: A function for classifying questions and generating responses based on a given set of sentences. Please refer to the documentation for the `task3_classifier` function for more details.
- `tools.task2_classifier.task2_classifier`: A function for classifying questions and generating responses based on a given SQL query and DataFrame. Please refer to the documentation for the `task2_classifier` function for more details.

### Parameters

- `question` (str): The question to be classified and processed.
- `bonds_link` (str): The link to the BondsDB API.
- `sentences` (list): A list of sentences to be used for classification in the absence of a SQL query.
- `csum_bot` (str): The cumulative summary of the bot's responses.
- `csum_user` (str): The cumulative summary of the user's queries.

### Returns

A dictionary containing the following keys:

- `bonds_db` (str): Indicates whether the BondsDB is required or not.
- `status` (str): The status of the classification and processing.
- `api_status` (str): The status of the API call.
- `result` (str or dict): The result of the classification and processing. It can be a string or a dictionary depending on the classification and API call.

## `task2_classifier` Function

This function is used to generate a response to a query based on the provided question, SQL query result, and cumulative summaries.

### Dependencies

- `get_completion` function: A function for generating completions using OpenAI GPT-3.5 Turbo.

### Parameters

- `question` (str): The question for which a response is generated.
- `result_mysql` (str): The result of an SQL query enclosed in triple backticks.
- `csum_bot` (str): The cumulative summary of the bot's conversation history.
- `csum_user` (str): The cumulative summary of the user's conversation history.

### Returns

A dictionary containing the following keys:

- `status` (str): The status of the completion generation. Possible values are "working", "Rate Limit Error", or "Unknown Error".
- `data` (str): The generated response to the query.

## `task3_classifier` Function

This function is used to generate an ideal response to a given question based on the conversation history, global database response, and the specific knowledge of the support executive at Goldman Sachs.

### Dependencies

- `get_completion` function: A function for generating completions using OpenAI GPT-3.5 Turbo.

### Parameters

- `question` (str): The question for which an ideal response is generated.
- `glo_sentences` (str): The response from the global database enclosed in triple backticks.
- `csum_bot` (str): The cumulative summary of the bot's conversation history.
- `csum_user` (str): The cumulative summary of the user's conversation history.

### Returns

A dictionary containing the following keys:

- `result` (str): The generated ideal response to the question.
- `status` (str): The status of the completion generation. Possible values are "working", "Rate Limit Error", or "Unknown Error".

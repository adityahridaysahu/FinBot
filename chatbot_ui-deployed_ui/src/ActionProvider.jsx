const central_api="http://ab6f3edfa09a041689aa19eeb5342cdc-291235673.us-east-1.elb.amazonaws.com/"
class ActionProvider {
  constructor(createChatBotMessage, setStateFunc) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
    this.handleUserMessage = this.handleUserMessage.bind(this);
    // this.timeout = null; // Store the timeout reference
    this.timeout2 = null;
  }
  static timout1 = null;
  static sessionID = ""; // Initialize the sessionID as a global attribute

  resetSessionID() {
    console.log("resetSessionID getting Called");
    ActionProvider.sessionID = "";
  }
  refreshPage() {
    window.location.reload(false);
  }

  resetTimeout() {
    clearTimeout(ActionProvider.timout1);
  }

  resetTimeout2() {
    clearTimeout(this.timeout2);
  }

  handleEmptyMessage() {
    const botMessage = this.createChatBotMessage(
      "Please Enter a valid message!!"
    );
    this.addMessageToState(botMessage);
    // this.resetTimeout();
  }
 
  async handleUserMessage(message) {
    // Clear the timeout when a user message is received
    this.resetTimeout();

    console.log("sessionID into api = " + ActionProvider.sessionID);
    const response = await fetch(central_api, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: message,
        session_id: ActionProvider.sessionID,
      }), // Use sessionID here
    });

    const data = await response.json();
    console.log("API Response:", data); // Log the complete response to inspect it

    const chatbotResponse = data.response;
    console.log(data.session_id); // Use sessionID here
    ActionProvider.sessionID = data.session_id;
    console.log("heh");
    console.log(ActionProvider.sessionID);

    const botMessage = this.createChatBotMessage(chatbotResponse);
    this.addMessageToState(botMessage);

    // Start the timeout after sending the response
    this.startTimeout();
  }

  async handleOptionSelect(optionValue) {
    // this.removeOptionsMessage(); // Remove the options message from the state

    if (optionValue === "option1") {
      this.resetTimeout2();
      const responseMessage = this.createChatBotMessage(
        "Thank you for valuable response"
      );
      this.addMessageToState(responseMessage);
      // Perform actions specific to Option 1
      const response = await fetch(central_api+"feedback", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          session_id: ActionProvider.sessionID,
          timeout: false,
          clicked: true,
        }), // Use sessionID here
      });
    } else if (optionValue === "option2") {
      this.resetTimeout2();
      const responseMessage = this.createChatBotMessage(
        "We are really sorry to hear that. You can contact us at query@gs.com"
      );
      this.addMessageToState(responseMessage);
      // Perform actions specific to Option 2
      const response = await fetch(central_api+"feedback", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          session_id: ActionProvider.sessionID,
          timeout: false,
          clicked: false,
        }), // Use sessionID here
      });
    } else {
      this.startTimeout2();
    }
  }

  createOptionButton(option) {
    return (
      <button
        key={option.value}
        onClick={() => this.handleOptionSelect(option.value)}
        style={{
          backgroundColor: "#7399C6",
          color: "#fff",
          border: "none",
          padding: "8px 16px",
          margin: "4px",
          borderRadius: "4px",
          cursor: "pointer",
          transition: "background-color 0.3s ease",
          ":hover": {
            backgroundColor: "#5c7a9e",
          },
        }}
      >
        {option.label}
      </button>
    );
  }

  startTimeout() {
    ActionProvider.timout1 = setTimeout(() => {
      this.resetTimeout2();
      const options = [
        { label: "Yes", value: "option1" },
        { label: "No", value: "option2" },
      ];

      const optionsComponent = (
        <div className="options-message">
          {options.map((option) => (
            <button
              key={option.value}
              onClick={() => this.handleOptionSelect(option.value)}
              style={{
                backgroundColor: "#7399C6",
                color: "#fff",
                border: "none",
                padding: "8px 16px",
                margin: "4px",
                borderRadius: "4px",
                cursor: "pointer",
              }}
            >
              {option.label}
            </button>
          ))}
        </div>
      );

      const optionsMessage = this.createChatBotMessage(optionsComponent);

      const botMessage = this.createChatBotMessage(
        "It seems you haven't asked a question."
      );
      const initialMessage = this.createChatBotMessage(
        "Are you satisfied with the response provided by us:"
      );
      this.addMessageToState(botMessage);
      this.addMessageToState(initialMessage);
      this.addMessageToState(optionsMessage);
      this.startTimeout2();
      // resetTimout2
    }, 60000); // 60 seconds wait for message by user.
  }

  async handleSecondTimeout() {
    const response = await fetch(central_api+"feedback", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        session_id: ActionProvider.sessionID,
        timeout: true,
        clicked: false,
      }), // Use sessionID here
    });
  }

  startTimeout2() {
    this.timeout2 = setTimeout(() => {
      const botMessage = this.createChatBotMessage(
        "Since you haven't selected any of the above options we assume you query has been resolved.Have a nice day"
      );
      this.handleSecondTimeout();
      this.addMessageToState(botMessage);

      // setTimeout(() => {
      //   this.refreshPage();
      // }, 8000);
    }, 60000); // 60 seconds wait for message by user.
  }

  addMessageToState(message) {
    const botMessage = this.createChatBotMessage(message);

    this.setState((prevState) => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  }
}

export default ActionProvider;

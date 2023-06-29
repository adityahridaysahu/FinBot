class MessageParser {
  constructor(actionProvider) {
    this.actionProvider = actionProvider;
  }

  parse = (message) => {
    const lowercaseMessage = message.toLowerCase();

    if (lowercaseMessage.trim() === "") {
      // Handle empty message
      this.actionProvider.handleEmptyMessage();
    } else {
      this.actionProvider.handleUserMessage(message);
    }
  };
}

export default MessageParser;

import ActionProvider from "../ActionProvider";

// Mock the createChatBotMessage and setStateFunc functions
const mockCreateChatBotMessage = jest.fn();
const mockSetStateFunc = jest.fn();

// Create a new instance of ActionProvider with the mock functions
const actionProvider = new ActionProvider(
  mockCreateChatBotMessage,
  mockSetStateFunc
);

// Reset the sessionID before each test
beforeEach(() => {
  ActionProvider.sessionID = "";
});

// Test case for handleEmptyMessage method
test("handleEmptyMessage method adds welcome message to state", () => {
  actionProvider.handleEmptyMessage();

  expect(mockCreateChatBotMessage).toHaveBeenCalledWith(
    "Please Enter a valid message!!"
  );
  expect(mockSetStateFunc).toHaveBeenCalled();
});

// Test case for handleUserMessage method
test("handleUserMessage method sends message to API and adds response to state", async () => {
  // Mock the fetch function
  global.fetch = jest.fn().mockResolvedValue({
    json: jest.fn().mockResolvedValue({
      response: "Hello, how can I help you?",
      session_id: "abc123",
    }),
  });

  const message = "Hi";
  await actionProvider.handleUserMessage(message);

  expect(global.fetch).toHaveBeenCalledWith("http://ab6f3edfa09a041689aa19eeb5342cdc-291235673.us-east-1.elb.amazonaws.com/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: message,
      session_id: "",
    }),
  });

  expect(mockCreateChatBotMessage).toHaveBeenCalledWith(
    "Hello, how can I help you?"
  );
  expect(mockSetStateFunc).toHaveBeenCalled();
  expect(ActionProvider.sessionID).toBe("abc123");
});

// Test case for resetSessionID method
test("resetSessionID method resets the sessionID", () => {
  ActionProvider.sessionID = "xyz456";
  actionProvider.resetSessionID();

  expect(ActionProvider.sessionID).toBe("");
});

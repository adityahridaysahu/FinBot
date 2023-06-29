import MessageParser from "../MessageParser";

const mockActionProvider = {
  handleEmptyMessage: jest.fn(),
  handleUserMessage: jest.fn(),
};

const messageParser = new MessageParser(mockActionProvider);

test("parse method handles empty message", () => {
  messageParser.parse("");
  expect(mockActionProvider.handleEmptyMessage).toHaveBeenCalled();
});

test("parse method handles non-empty message", () => {
  const message = "Hello";
  messageParser.parse(message);
  expect(mockActionProvider.handleUserMessage).toHaveBeenCalledWith(message);
});

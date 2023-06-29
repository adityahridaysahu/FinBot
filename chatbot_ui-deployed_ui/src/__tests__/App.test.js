import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import App from "../App";

describe("App", () => {
  test("renders without errors", () => {
    render(<App />);
    const linkElement = screen.getByText(/New Chat/i);
    expect(linkElement).toBeInTheDocument();
  });

  test("toggles chatbot when 'New Chat' button is clicked", () => {
    const { getByTestId } = render(<App />);
    const chatButton = getByTestId("new-chat-button");
    fireEvent.click(chatButton);
    const linkElement = screen.getByText(/FinBOT/i);
    expect(linkElement).toBeInTheDocument();
  });
});

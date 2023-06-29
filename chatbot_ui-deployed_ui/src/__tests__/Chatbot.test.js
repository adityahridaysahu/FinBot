import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";
import ChatbotInterface from "../chatbot";

describe("ChatbotInterface", () => {
  test("renders chatbot interface correctly", () => {
    render(
      <ChatbotInterface onClose={() => {}} ReassignSessionID={() => {}} />
    );

    // Assert the presence of initial chat message
    const initialMessage = screen.getByText(/FinBOT 🤖/i);
    expect(initialMessage).toBeInTheDocument();
  });

  test("buttons checks", () => {
    render(
      <ChatbotInterface onClose={() => {}} ReassignSessionID={() => {}} />
    );

    // Assert the presence of initial chat message
    const initialMessage = screen.getByText(/FinBOT 🤖/i);
    expect(initialMessage).toBeInTheDocument();

    // Assert the presence of chatbot toggle button (- btn)
    const toggleButton2 = screen.getByTestId("chat-toggle-button11");
    expect(toggleButton2).toBeInTheDocument();

    // minimize btn working fine
    fireEvent.click(toggleButton2);
    const continueText2 = screen.getByText(/FinBOT 🤖/);
    expect(continueText2).toBeInTheDocument();

    // Assert the presence of chatbot toggle button (x btn)
    const toggleButton = screen.getByTestId("chat-toggle-button");
    expect(toggleButton).toBeInTheDocument();

    // minimize btn working fine
    fireEvent.click(toggleButton);
    const continueText = screen.getByText(/FinBOT 🤖/);
    expect(continueText).toBeInTheDocument();

    // Assert the presence of chatbot toggle button ([] btn)
    const toggleButton3 = screen.getByTestId("chat-toggle-button");
    expect(toggleButton3).toBeInTheDocument();

    // minimize btn working fine
    fireEvent.click(toggleButton3);
    const continueText3 = screen.getByText(/FinBOT 🤖/);
    expect(continueText3).toBeInTheDocument();
  });
});

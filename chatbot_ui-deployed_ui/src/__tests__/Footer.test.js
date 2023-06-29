import React from "react";
import { render, screen } from "@testing-library/react";
import Footer from "../components/Footer/Footer";

describe("Footer", () => {
  test("renders footer content correctly", () => {
    render(<Footer />);

    // Assert the presence of footer text
    const footerText = screen.getByText(/2023 GS/i);
    expect(footerText).toBeInTheDocument();

    // Assert the presence of social media icons
    const socialIcons = screen.getAllByRole("link");
    expect(socialIcons).toHaveLength(3); // Assuming there are three social media icons

    // Assert the presence of footer sections
    const sectionTitles = screen.getAllByRole("heading", { level: 3 });
    expect(sectionTitles).toHaveLength(3); // Assuming there are three footer sections

    // Assert the presence of footer bottom text
    const bottomText = screen.getByText(/All rights reserved/i);
    expect(bottomText).toBeInTheDocument();
  });
});

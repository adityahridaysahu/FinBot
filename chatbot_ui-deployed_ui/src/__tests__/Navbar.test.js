import { render, screen, fireEvent } from "@testing-library/react";
import Navbar from "../components/Navbar/Navbar";

test("renders logo and company name", () => {
  render(<Navbar />);

  const logoElement = screen.getByAltText("Logo");
  const companyNameElement = screen.getByText("Goldman Sachs");

  expect(logoElement).toBeInTheDocument();
  expect(companyNameElement).toBeInTheDocument();
});

test("toggles dropdown menu on button click", () => {
  render(<Navbar />);

  const dropdownButton = screen.getByTestId("dropdown-btn");
  fireEvent.click(dropdownButton);

  const companyNameElement = screen.getByText("FAQ");
  expect(companyNameElement).toBeInTheDocument();

  const companyNameElement2 = screen.getByText("About Us");
  expect(companyNameElement2).toBeInTheDocument();

  const companyNameElement3 = screen.getByText("What We Do");
  expect(companyNameElement3).toBeInTheDocument();
});

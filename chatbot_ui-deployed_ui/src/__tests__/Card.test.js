import { render, screen } from "@testing-library/react";
import Card from "../components/Card/Card";

const mockCardData = {
  // mock object for the card
  natural: false,
  dateBuilt: "2022",
  imageUrl: "example.jpg",
  title: "Sample Title",
  location: "Sample Location",
  googleMapsUrl: "https://maps.google.com",
  description: "Sample Description",
  key: 1,
};

test("renders card with correct data", () => {
  render(<Card {...mockCardData} />);

  const titleElement = screen.getByText(mockCardData.title);
  const descriptionElement = screen.getByText(mockCardData.description);
  const imageElement = screen.getByAltText(mockCardData.title);

  expect(titleElement).toBeInTheDocument();
  expect(descriptionElement).toBeInTheDocument();
  expect(imageElement).toBeInTheDocument();
  expect(imageElement).toHaveAttribute("src", mockCardData.imageUrl);
});

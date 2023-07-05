import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders Anmelden button", () => {
  render(<App />);
  const buttonElement = screen.getByText(/Anmelden/i);
  expect(buttonElement).toBeInTheDocument();
});

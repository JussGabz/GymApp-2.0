// __tests__/MyComponent.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import MyComponent from '../MyComponent';

test('renders the component with a title', () => {
  render(<MyComponent />);
  const titleElement = screen.getByText(/my component/i);
  expect(titleElement).toBeInTheDocument();
});

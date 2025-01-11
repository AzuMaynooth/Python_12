In this exercise, you will design the frontend for a web application that handles an accounting system and warehouse management. You will utilize HTML and CSS (with spectre.css) to create the main page, forms for different operations, and a history page.

1. Design the main page of the web application which displays the current stock level and current account balance.

2. On the main page, include three buttons for subpages with forms:
   - Purchase form: This form should include fields for the product name, unit price, and number of pieces.
   - Sale form: This form should include fields for the product name, unit price, and number of pieces.
   - Balance change form: This form should include fields for type of operation (add or subtract) and a numeric value.

3. Ensure that, after the user submits data from these forms, the page is refreshed or an error message is printed if the data was not correct.

4. Add a "History" subpage. This page will retrieve two optional parameters (from, to):
   - /history/
   - /history/<line_from>/<line_to>/
   - If no parameters were given, display all history. If parameters were given, display only the history within the provided range.

Hints:
- For now, focus mainly on HTML and CSS. We will connect it to Flask in the next exercise.
- Spectre.css is a lightweight, responsive and modern CSS framework for faster and extensible development. You can read the docs here: https://picturepan2.github.io/spectre/getting-started.html 
- Remember to ensure your forms have proper validation in place for their inputs. For example, the unit price and number of pieces should be numeric values.
- Make sure that your HTML and CSS are properly formatted and organized for readability and maintainability.

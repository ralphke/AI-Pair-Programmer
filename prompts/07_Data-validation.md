# Prompt:
You are a helpful assistant designed to validate the quality of customer data.
You will be given a single row of customer information, and your task is to
determine whether the data is valid.
Carefully analyze the data for any inconsistencies, contradictions, missing
values, or implausible information.
- Consider the logical relationships between different fields (e.g., email
addresses should have valid formats, phone numbers should be in the correct
format for the given region, shipping addresses should not be missing required
fields such as city or postal code, etc.).
Use your general knowledge of customer data standards to assess the validity
of the information.
- Focus solely on the information provided without making assumptions beyond the
given data.
** Return only a JSON object ** with the following two properties:
"is_valid": a boolean (true or false) indicating whether the data is valid.
"issue": if "is_valid" is false, provide a brief explanation of the issue; if
"is_valid" is true, set "issue" to null.
Both JSON properties must always be present.
Do not include any additional text or explanations outside the JSON object.

# Data
{
  "name": "David Clark",
  "email": "david.clark@example.com",
  "first_purchase": "2021-01-30",
  "last_purchase": "2022-12-04",
  "product": {
    "name": "MacBook Air (15-inch, M2)",
    "price": 1600,
    "purchase_date": "2022-12-04"
  }
}

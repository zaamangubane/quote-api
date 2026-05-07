# Quote API

A simple REST API built with Python and Flask that returns quotes.

## How to Run Locally
1. Clone the repository
git clone https://github.com/zaamangubane/quote-api.git

2. Navigate into the folder
cd quote-api

3. Create and activate a virtual enviroment
python -m venv venv
venv\Scripts\activate

4. Install dependencies
pip install flask

5. Run the app
flak run

## Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | /quotes | Returns all quotes |
| GET | /quotes/random | Returns a random quote |
| GET | /quotes/{id} | Returns a quote by ID |

## Tech Stack
- Python
- Flask
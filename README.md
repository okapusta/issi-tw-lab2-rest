# issi-tw-lab2-rest

A simple FastAPI movie catalog

## Running

1. Install deps `uv sync`
2. Run `uv run fastapi dev main.py `

## API examples

1. List movies:
    ```
    curl -X GET localhost:8000/movies | jq
    ```
2. Create a movie
    ```
    curl -X POST  localhost:8000/movies -d '{ "title": "Tester", "year": 1999, "actors": "Testing Actor", "description": "Testing 123", "director": "Tester" }' -H "Content-Type: application/json"
    ```
3. Update a movie
    ```
    curl -X PUT localhost:8000/movies/6 -d '{ "title": "Tester", "year": 1999, "actors": "Testing Actor", "description": "Testing 123", "director": "Tester" }' -H "Content-Type: application/json"
    ```
4. Delete a movie
    ```
     curl -X DELETE localhost:8000/movies/6
    ```

# flask_api_project

* replace finhub api key, google client id and secret key
* use docker compose up to build and start docker containers 
* on localhost/5000 use following endpoints
* /login -> invokes oauth2 for google and redirects to 2fa for google
* / -> home page will show user email with request to add stock ticker for value
* /?symbol= {ticker} to fetch ticker details

* project uses authlib to leverage google auth services and redis to cache response of valid ticker 
* login via oauth2
* ![ouath2 for login](https://user-images.githubusercontent.com/68659171/209512173-819813ee-316f-4c78-b38a-c47ea8c65be9.png)
* logged in user
* ![logged_id](https://user-images.githubusercontent.com/68659171/209512229-f102616a-e2dc-40ae-b061-c58c5c78529c.png)
* msft ticker cache miss
* ![msft-cache-miss](https://user-images.githubusercontent.com/68659171/209512261-de11df3f-2551-4c02-891c-3cd2cc8b73be.png)
* msft ticker cache hit
* ![msft-cache-hit](https://user-images.githubusercontent.com/68659171/209512276-56ca5060-f208-4715-8380-483462332487.png)

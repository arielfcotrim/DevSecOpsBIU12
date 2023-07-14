## Compose sample application

### Use with Docker Development Environments



### React application with a Spring backend and a MySQL database

Project structure:
```
.
├── backend
│   ...
├── db
│   └── password.txt
├── frontend
│   ├── ...
└── README.md
```

deploy this app with docker compose 

env :
  for the back end : 
         MYSQL_HOST: db
  for the db :
      - MYSQL_DATABASE=example
      - MYSQL_ROOT_PASSWORD_FILE=/run/secrets/db-password
      
      
 secrets fot the db and the backend : 
 secrets:
      - db-password
      
      
  front end runs on port 3000
  

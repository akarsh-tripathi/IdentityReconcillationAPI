# Identity Reconciliation API

A Contact Reconciliation Console that helps in finding, updating & handling records with similar email IDs, phone number in the database. This Console also helps to create reconciliation and joining of primary contact linked to multiple secondary contacts containing similar records.

## Demo
[Demo Link ](https://identityreconcillationapi-1.onrender.com)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)


## Installation

The Framework it has been based on is Django & Database used is sqllite(For DEMO Purpose)

##Thoughts & Assumptions 
- The current implementation makes use of function created to cater the changes everytime the /identiy enpoint is called causing it load on the response timing & the server to cater the taks immediately.
- The solution to this could be to create a Background Celery Worker that uses Redis PubSub to process the task of remapping the DB if record of phone or number is found on a different worker thread.
- This implementation will be best suited to create a better, faster implementation for search & updation of DB

To run the code, Kindly install the following packages- 

```bash
pip install Django  Django-rest-framework celery streamlit
```


## Usage

To Run the command 

```bash
python manage.py migrate
python manage.py runserver
```

To Run the Frontend the command 

```bash
streamlit run streamlit_UI.py
```
## API Endpoints

List and details of API endpoints are here.

#Demo Endpoints for Creation & Viewing of Database 
- `GET /api/test/getData/`: Provides a list of all the records present in DB.

Response Body
```
[
  {
        "id": 28,
        "phonenumber": 9971234496,
        "email": "a99@a.com",
        "linkedId": 27,
        "linkPrecedence": "secondary",
        "createdAt": "2024-06-04T08:54:29.992711Z",
        "updatedAt": "2024-06-04T08:55:32.858338Z",
        "deletedAt": null
    }
]
```

- `POST /api/test/createData`: Create data from the JSON request body

Request Body
```
{
    "phonenumber": "9971234105",
    "email": "a105@a.com"
}   
```

 #Identity Endpoint
- `POST /api/identity/`: Provides a list of all records associated with the Phonenumber/Emails with secondaryContacts.

Request Body
```
{
    "phonenumber": "9971234105",
    "email": "a105@a.com"
}
```

Response Body
```
{
    "Contact": {
        "primaryContatctId": 33,
        "emails": [
            "a105@a.com"
        ],
        "phoneNumbers": [
            9971234105
        ],
        "secondaryContactIds": []
    }
}
```

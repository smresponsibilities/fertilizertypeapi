# Fertilizer Recommendation API Documentation

## Overview

The Fertilizer Recommendation API provides a way to predict the appropriate fertilizer based on input parameters such as temperature, humidity, moisture, soil type, crop type, nitrogen, potassium, and phosphorous levels.

## Base URL

```
https://fertilizertypebysm.onrender.com
```

## Endpoints

### 1. Home Endpoint

#### https://fertilizertypebysm.onrender.com/

```
GET /
```

#### Description

This endpoint returns a welcome message indicating that the API is running.

#### Response

- **Status Code:** 200 OK
- **Body:**

  ```json
  "This is a Fertilizer Recommendation API!"
  ```

### 2. Fertilizer Recommendation Endpoint

#### https://fertilizertypebysm.onrender.com/fertilizername

```
POST /fertilizername
```

#### Description

This endpoint accepts a JSON payload with various input parameters and returns the recommended fertilizer name.

#### Request

- **Method:** POST
- **Headers:**
  - `Content-Type: application/json`
- **Body:**

  ```json
  {
    "temperature": float,
    "humidity": float,
    "moisture": float,
    "soilType": int,
    "cropType": int,
    "nitrogen": int,
    "potassium": int,
    "phosphorous": int
  }
  ```

#### Response

- **Status Code:** 200 OK
- **Body:**

  ```json
  {
    "Fertilizername": "string"
  }
  ```

- **Status Code:** 400 Bad Request
- **Body:**

  ```json
  {
    "error": "Invalid input data"
  }
  ```

- **Status Code:** 500 Internal Server Error
- **Body:**

  ```json
  {
    "error": "string"
  }
  ```

## Example Usage

### Request

```sh
curl -X POST https://fertilizertypebysm.onrender.com/fertilizername \
     -H "Content-Type: application/json" \
     -d '{
           "temperature": 25.0,
           "humidity": 60.0,
           "moisture": 30.0,
           "soilType": 1,
           "cropType": 2,
           "nitrogen": 10,
           "potassium": 5,
           "phosphorous": 3
         }'
```

### Response

```json
{
  "Fertilizername": "20-20"
}
```

## Error Handling

### Invalid Input Data

If the input data is invalid or missing required fields, the API will return a `400 Bad Request` status code with the following response:

```json
{
  "error": "Invalid input data"
}
```

### Internal Server Error

If an unexpected error occurs, the API will return a `500 Internal Server Error` status code with the following response:

```json
{
  "error": "string"
}
```

## Dependencies

The API relies on the following Python packages:

- Flask==3.0.3
- Flask-Cors==5.0.0
- numpy==2.1.1
- scikit-learn==1.5.2
- xgboost==2.1.1

Ensure these dependencies are installed by running:

```sh
pip install -r requirements.txt
```

## Running the Application

To run the application locally, execute the following command:

```sh
python app.py
```

The application will be available at [https://fertilizertypebysm.onrender.com].


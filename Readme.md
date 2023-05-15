
---

# Address Book Application

This is an address book application built using FastAPI and SQLite. It provides an API for creating, updating, deleting, and retrieving addresses, as well as querying addresses within a given distance.

## Prerequisites

- Python 3.7 or above installed on your system

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal or command prompt.

## Setting up the Virtual Environment

1. Create a new virtual environment by running the following command:

   ```bash
   python3 -m venv env
   ```

2. Activate the virtual environment:

   - For macOS/Linux:
     ```bash
     source env/bin/activate
     ```

   - For Windows:
     ```bash
     .\env\Scripts\activate
     ```

## Install Dependencies

1. Ensure that the virtual environment is activated.
2. Run the following command to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Ensure that the virtual environment is activated.
2. Start the FastAPI server by running the following command:

   ```bash
   uvicorn project.main:app --reload
   ```

3. The application will be running at `http://localhost:8000`. You can access the FastAPI's Swagger documentation and test the API endpoints in your browser.

## API Endpoints

The following endpoints are available:

- **POST /addresses/**: Create a new address.
- **PUT /addresses/{address_id}/**: Update an existing address.
- **DELETE /addresses/{address_id}/**: Delete an address.
- **GET /addresses/?latitude={latitude}&longitude={longitude}&distance={distance}**: Retrieve addresses within a given distance from the specified latitude and longitude.

Refer to the FastAPI Swagger documentation for detailed information on the request and response formats for each endpoint.

## Deactivating the Virtual Environment

To deactivate the virtual environment, run the following command:

```bash
deactivate
```

## License

This project is licensed under the [MIT License](LICENSE).

---

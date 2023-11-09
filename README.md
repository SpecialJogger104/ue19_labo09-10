# OpenSky Network Flight Counter
This Python script queries the OpenSky Network API to retrieve the number of flights in a specified area.

## How It Works
The script utilizes the requests library to make a request to the OpenSky Network API. You need to provide your credentials (username and password) to access the API.

## Installation
1. Ensure you have Python installed on your machine.
2. Install the dependencies by running the following command in the terminal:
    ```bash
    pip install requests
    ```

## Usage
1. Replace 'your_username' and 'your_password' with your OpenSky Network credentials in the app.py script.
2. Run the script using the following command in the terminal:
    ```bash
    python app.py
    ```
The script will display the number of flights in the specified area.

## Docker
If you prefer to run the script in a Docker container, follow these steps:
1. Build the Docker image using the following command:
    ```bash
    docker build -t opensky-flight-counter .
    ```
2. Run the container using the following command:

    ```bash
    docker run -e USERNAME='your_username' -e PASSWORD='your_password' opensky-flight-counter
    ```
Make sure to replace 'your_username' and 'your_password' with your OpenSky Network credentials.

Remember to keep your credentials secure and never share them publicly.

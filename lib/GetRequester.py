import requests
import json

class GetRequester:
    """A class to make GET requests and parse JSON data."""

    def __init__(self, url):
        """Initialize the requester with a URL."""
        self.url = url

    def get_response_body(self):
        """Send a GET request to the URL and return the response body."""
        response = requests.get(self.url)  # Send GET request
        response.raise_for_status()  # Raise an error for bad responses
        return response.content  # Return the raw response body

    def load_json(self):
        """Load JSON data from the response body and return it as a Python object."""
        response_body = self.get_response_body()  # Get the response body
        return json.loads(response_body)  # Convert JSON string to Python object

# FastAPI Proxy Server

## Overview

This FastAPI application acts as a proxy server to download files from a specified URL. It handles incoming requests, forwards them to the target URL, and streams the response back to the client. This allows users to download files from a different domain while bypassing CORS restrictions.

## Features

- **CORS Support:** Configured to accept requests from any origin.
- **Dynamic URL Handling:** Downloads files from URLs specified in the query parameter.
- **Custom Headers:** Utilizes custom headers and user-agent to mimic browser requests.
- **Streaming Responses:** Efficiently streams file content to clients with support for large files.

## Installation

To run this FastAPI application, you'll need Python 3.7 or higher. You also need to install the required dependencies. You can use `pip` to install them:

```bash
pip install -r requirements.txt
```

## Running the Application

Save the provided code to a file named `main.py`, and then use `uvicorn` to run the FastAPI application:

```bash
uvicorn main:app --reload
```

By default, the server will be available at `http://127.0.0.1:8000`.

## API Endpoint

### `GET /download/`

This endpoint proxies the request to the specified URL and streams the file back to the client.

#### Query Parameters

- `url` (required): The URL of the file to download.
- `host` (optional): The host header to use in the request (default: `deva-cpmav9sk6x5.cimanowtv.com`).

#### Example Request

```bash
curl "http://127.0.0.1:8000/download/?url=https://example.com/path/to/file.zip"
```

#### Response

The server responds with a `StreamingResponse`, allowing for the file to be downloaded. The `Content-Disposition` header is set to suggest a filename for the downloaded file.

## Security

The application disables SSL verification by setting `verify=False` in the requests. This should be used with caution, especially in production environments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used.
- [requests](https://docs.python-requests.org/en/latest/) - HTTP library for making requests.
- [user_agent](https://pypi.org/project/user-agent/) - Library for generating user-agent strings.
```

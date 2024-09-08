from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote
from urllib3.exceptions import InsecureRequestWarning
from user_agent import generate_user_agent
import requests
import warnings

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {}

@app.get("/download/")
async def proxy_request(url: str = Query(...), host: str = Query("deva-cpmav9sk6x5.cimanowtv.com")):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8,ar-EG;q=0.7,ar;q=0.6,id;q=0.5",
        "Connection": "keep-alive",
        "Host": host,
        "Referer": "https://bs.cimanow.cc/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": generate_user_agent(),
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"'
    }
    
    response = requests.get(url, headers=headers, stream=True, verify=False)

    filename = unquote(url).split("/")[-1]

    return StreamingResponse(
        response.iter_content(chunk_size=8192),
        headers={
            "Content-Disposition": f"attachment; filename={filename}",
            "Content-Type": response.headers.get("Content-Type", "application/octet-stream"),
        }
    )

warnings.simplefilter('ignore', InsecureRequestWarning)

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
        html_content = """
    <html>
        <head>
            <title>GuardianFlow</title>
        </head>
        <body>
            <h1>PARKING LOT!</h1>
            <h2>Coming soon...</h2>
        </body>
    </html>
    """
        return HTMLResponse(content=html_content, status_code=200)

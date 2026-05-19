from fastapi import FastAPI
# pyrefly: ignore [missing-import]
import pyjokes

app = FastAPI()

@app.get("/")
async def root():
    random_joke = pyjokes.get_joke("en","neutral")
    return {"random_joke": random_joke}

from fastapi import FastAPI

app = FastAPI()  # Yahan kya aayega?

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager"} # Yahan message likhiye
from package import *
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI



app = FastAPI(root_path="/fastapi")

app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3000"], 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('API starting...')



@app.get("/")
def test():
    return {"message": "FastAPI running 🚀"}

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def reverse(prompt: Prompt):
    reversed = prompt.text[::-1]
    return {"response": reversed}


@app.get("/assessperform")
def reverse():
    c = approx_10s_function()
    return {"nb iteration": str(c)}

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import asyncio
import uvicorn

app = FastAPI(title="Media Processing API", version="1.0.0")

class InputMedia(BaseModel):
    audiourl: str
    videourl: str | None = None
    imageurl: str | None = None
    videoresolution: str | None = None

def inference(
    videourl, audiourl, imageurl, videoresolution,
    x_username, x_password,
    x_foldername=None, x_resend_api_key=None,
    x_email_receiver=None, x_email_unifidrive=None,
    x_pass_unifidrive=None
):
    print("Running inference...")
    return {
        "status": "success",
        "video": videourl,
        "audio": audiourl,
        "image": imageurl,
        "resolution": videoresolution,
        "user": x_username
    }

@app.get("/")
def home():
    return {"message": "FastAPI server running"}


@app.post("/api/add-image-to-exists-video")
async def myfunc(
    payload: InputMedia,
    x_username: str = Header(..., alias="X-Username"),
    x_password: str = Header(..., alias="X-Password"),
    x_foldername: str | None = Header(None, alias="X-Foldername"),
    x_resend_api_key: str | None = Header(None, alias="X-resend_api_key"),
    x_email_receiver: str | None = Header(None, alias="X-email_receiver"),
    x_email_unifidrive: str | None = Header(None, alias="X-email_unifidrive"),
    x_pass_unifidrive: str | None = Header(None, alias="X-pass_unifidrive"),
):
    await asyncio.sleep(5)
    videourl = payload.videourl
    audiourl = payload.audiourl
    imageurl = payload.imageurl
    videoresolution = payload.videoresolution
    print(
        "video:", videourl,
        "audio:", audiourl,
        "image:", imageurl,
        "resolution:", videoresolution,
        "user:", x_username,
        "folder:", x_foldername
    )
    output = inference(
        videourl, audiourl, imageurl, videoresolution,
        x_username=x_username, x_password=x_password,
        x_foldername=x_foldername,
        x_resend_api_key=x_resend_api_key,
        x_email_receiver=x_email_receiver,
        x_email_unifidrive=x_email_unifidrive,
        x_pass_unifidrive=x_pass_unifidrive,
    )
    return {"Hello": output}

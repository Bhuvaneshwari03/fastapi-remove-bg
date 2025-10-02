from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
import io

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    # Read uploaded file
    input_bytes = await file.read()

    # Remove background
    output_bytes = remove(input_bytes)

    # Return PNG with transparent background
    return StreamingResponse(io.BytesIO(output_bytes), media_type="image/png")

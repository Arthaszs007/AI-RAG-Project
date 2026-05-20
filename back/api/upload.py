from fastapi import APIRouter,UploadFile,File
from utils import docs_saver

router = APIRouter()

@router.post("/upload")
async def upload(file:UploadFile= File(...)):
    '''
    pass
    '''
    if not file:
        print("failed")
    docs_saver.save_docs_local(file)

    content = await file.read()
    return {
        "filename":file.filename,
        "size":len(content)
    }
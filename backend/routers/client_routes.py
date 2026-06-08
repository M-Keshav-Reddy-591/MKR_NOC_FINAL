from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/client",
    tags=["Client"]
)

@router.get("/info")
def get_client_info():

    return {
        "message": "Client endpoint ready"
    }
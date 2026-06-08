from fastapi import (
    APIRouter,
    Request
)

router = APIRouter(
    prefix="/api/v1/network",
    tags=["Network"]
)


@router.get("/my-ip")
def get_my_ip(
    request: Request
):

    return {

        "ip": request.client.host

    }
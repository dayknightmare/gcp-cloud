from src.use_cases.get_os_data import GetOSDataCase
from src.dto.get_os_data_dto import GetOSDataDTO
from fastapi import APIRouter, Request


os_info_route = APIRouter()

@os_info_route.get('/', response_model=GetOSDataDTO)
async def get_os_data(request: Request) -> dict:
    return await GetOSDataCase().handler(request)
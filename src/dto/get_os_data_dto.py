from pydantic import BaseModel
from typing import Optional


class GetOSDataDTO(BaseModel):
    worker_id: str
    host_name: str
    python_version: list[str]
    dist: str
    linux_distribution: str
    system: str
    machine: str
    platform: str
    uname: list[str]
    version: str
    mac_ver: Optional[list]

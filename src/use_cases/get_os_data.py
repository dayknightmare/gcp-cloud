from fastapi import Request
import platform
import socket
import sys


class GetOSDataCase:
    def linux_distribution(self) -> str:
        try:
            return platform.linux_distribution()

        except Exception:
            return "N/A"

    def dist(self) -> str:
        try:
            return platform.dist()

        except Exception:
            return "N/A"

    async def handler(self, request: Request) -> dict:
        return {
            'worker_id': request.app.state.uuid,
            'host_name': socket.gethostname(),
            'python_version': sys.version.split('\n'),
            'dist': str(self.dist()),
            'linux_distribution': self.linux_distribution(),
            'system': platform.system(),
            'machine': platform.machine(),
            'platform': platform.platform(),
            'uname': platform.uname(),
            'version': platform.version(),
            'mac_ver': platform.mac_ver(),
        }
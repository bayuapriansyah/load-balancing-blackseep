from blacksheep import Application
from blacksheep.server.responses import text
from blacksheep.server.routing import Router
import socket

router = Router()

@router.get("/")
async def home(request):
    return text(f"Halo dari Blacksheep! Host: {socket.gethostname()}")

app = Application(router=router)

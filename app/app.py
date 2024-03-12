from typing import List
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.structures import Node
from app.utils import get_path, create_tree_from_commands

app = FastAPI()

root: Node | None = None


class CommandsList(BaseModel):
    commands: List[str]


@app.post("/commands")
async def upload_commands_log_history(commands_list: CommandsList):
    global root
    root = create_tree_from_commands(commands_list.commands)
    return {"message": "Log of issued commands have been parsed"}


@app.get("/rcrs/{command}")
async def get_rcr_of_command(command: str):
    if not root:
        raise HTTPException(status_code=404, detail="Log of issued commands needs to be inserted first")
    else:
        rcr = get_path(root, command)
        if not rcr:
            raise HTTPException(status_code=404, detail=f"Command {command} has no RCR, probably it was not in "
                                                        f"logs history")
        return {"rcr": rcr}

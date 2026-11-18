"""Read aggregate keystrokes and explicitly counted editor characters on the local host."""
import json
from pathlib import Path
from datetime import date
from serve import page
INTERVAL=2
def snapshot(o,m):
    day=date.today().isoformat()
    def load(key):
        path=Path(o[key]).expanduser()
        if not path.exists():return None
        return json.loads(path.read_text()).get(day,{"count":0,"minutes":[]})
    global_count=load("key_file");editor=load("character_file")
    def view(name,value,units):
        if value is None:return page(name,"No data","Start the local collector",units)
        return page(name,value["count"],units,f'{len(value["minutes"])} active minutes')
    if global_count is None and editor is None:raise ValueError("Start a collector first")
    return dict(state="Counts only / today",key=str((global_count or {}).get("count",0)//100)+"/"+str((editor or {}).get("count",0)//100),pages=[
        view("KEY PRESSES",global_count,"Mac session key-downs"),view("CHARACTERS",editor,"Explicit writer field")])

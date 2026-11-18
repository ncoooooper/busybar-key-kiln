"""A local opt-in writing pad. Persist counts, never entered text."""
import json,sys,time,tkinter as tk
from datetime import date
from pathlib import Path
out=Path(sys.argv[1]).expanduser()
counts=json.loads(out.read_text()) if out.exists() else {}
root=tk.Tk();root.title("Key Kiln • counted writing pad")
tk.Label(root,text="Characters entered here count toward today. Text stays in this window.").pack()
pad=tk.Text(root,width=62,height=16,wrap="word");pad.pack(fill="both",expand=True)
old=pad._w+"_original";pad.tk.call("rename",pad._w,old)
def proxy(command,*args):
    result=pad.tk.call(old,command,*args)
    if command=="insert" and len(args)>1:
        amount=sum(len(x) for x in args[1::2]);day=date.today().isoformat()
        item=counts.setdefault(day,{"count":0,"minutes":[]});item["count"]+=amount
        minute=int(time.time()//60)
        if amount and (not item["minutes"] or item["minutes"][-1]!=minute):item["minutes"].append(minute)
        tmp=out.with_suffix(out.suffix+".tmp");tmp.write_text(json.dumps(counts));tmp.replace(out)
    return result
pad.tk.createcommand(pad._w,proxy);pad.focus_set();root.mainloop()

#! /usr/bin/env python
'''
Description: 
FilePath: /wired_controller/gui.py
Author: qxsoftware@163.com
Date: 2020-10-28 09:52:27
LastEditTime: 2020-10-28 16:16:08
Refer to: https://github.com/QixuanAI
'''


from config import Config
import tkinter as tk
from pathlib import Path

WIN_NAME = 'Wired Controller'
WIN_WIDTH = 600
WIN_HEIGHT = 800


def createControlPanel(win: tk.Tk, conf: Config):
    pass


def createConfChoosePanel(win: tk.Tk, confdir):
    def seleconf_click():
        if len(lbox_conf.curselection())>0:
            print(lbox_conf.selection_get())
    flist=[p for p in Path(confdir).rglob('*') if p.is_file()]
    if len(flist) == 0:
        createDirChoosePanel(win)
    label=tk.Label(win,text="Please select a config file, then click 'Select' button.")
    lbox_conf = tk.Listbox(win, width=80, height=20)
    lbox_conf.insert(0, *)
    lbox_conf.selection_set(0)
    btn_sele = tk.Button(win, text="Select", command=seleconf_click)

    label.pack()
    lbox_conf.pack()
    btn_sele.pack()


def createMainWindow(name):
    win = tk.Tk(baseName=name)
    win.title(name)
    return win


def main(args):
    win = createMainWindow(WIN_NAME)
    # win.geometry("{}x{}".format(WIN_WIDTH,WIN_HEIGHT))
    if args.config:
        createControlPanel(win, args.config)
    elif args.confdir:
        createConfChoosePanel(win, args.confdir)
    win.mainloop()


if __name__ == "__main__":
    import argparse
    parse = argparse.ArgumentParser(description="Here is command description.")
    parse.add_argument("-d", "--confdir", type=str,
                       default='config', help="Where is the config files in")
    parse.add_argument("-c", "--config", type=str,
                       help="Which config file to use")
    args = parse.parse_args()
    main(args)

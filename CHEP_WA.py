import sys,os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'packages'))

from lib import *
# Python 2
try:
    import Tkinter as tk
    import ttk
    #from ttkthemes import themed_tk as theme
    import ScrolledText as scrolledtext
# Python 3
except:
    import tkinter as tk
    from tkinter import ttk
    from ttkthemes import themed_tk as theme
    from tkinter import scrolledtext


operations = Operations()

#Applying Themes for Python3
try:
    root = theme.ThemedTk()
    root.get_themes()
    root.set_theme("radiance")
#Using Basic theme for Python2
except:
    root = tk.Tk()
    
root.title('Schneider-CHEP')
root.geometry("1200x900")
root.resizable(0, 0)

f = ttk.Frame(root, height=900, width=1500, relief='flat', borderwidth=4)
f.pack()

setings.raw_job_text = scrolledtext.ScrolledText(f, height=20, width=100, wrap=tk.WORD)
setings.raw_job_text.bind("<Control-Key-a>", operations.select_all_t)
setings.raw_job_text.bind("<Delete>", operations.delete_all)
setings.raw_job_text.config(padx=10, pady=10)
setings.raw_job_text.insert("1.0", 'Place Schneider CHEP Work Assignment')
setings.raw_job_text.pack(side=tk.TOP)

setings.trigger_transform_button = ttk.Button(f, text='Transform', command=operations.retrieve_text)
# setings.trigger_transform_button.config(padx=10, pady=10)
setings.trigger_transform_button.pack(side=tk.TOP)

setings.transformed_text = scrolledtext.ScrolledText(f, height=20, width=100, wrap=tk.WORD)
setings.transformed_text.bind("<Control-Key-a>", operations.select_all_t)
setings.transformed_text.insert("1.0", 'Transformed CHEP Work Assignment')
setings.transformed_text.config(padx=10, pady=10)
setings.transformed_text.pack(side=tk.BOTTOM)

root.mainloop()

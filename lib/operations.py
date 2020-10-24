import json
import setings
from schema import Schema
#Python 3
try:
    import tkinter as tk
    from tkinter import messagebox
#Python2
except:
    import Tkinter as tk
    import tkMessageBox as messagebox

schema = Schema()


class Operations(object):

    def __init__(self):
        print('Operations Initialised')

    def retrieve_text(self):
        try:
            setings.transformed_text.delete("1.0", tk.END)
            entered_text = json.loads(setings.raw_job_text.get("1.0", tk.END))
            if schema.validate_json(entered_text):
                transformed_text = self.transform_text(entered_text)
                setings.transformed_text.insert("1.0", json.dumps(transformed_text, sort_keys=False, indent=4))
        except ValueError:
            messagebox.showerror("ERROR", "Invalid Json Please Insert Json String")

    def transform_text(self, text):
        text['job']['shipment_details']['master_bill_of_lading'] = \
            str(int(text['job']['shipment_details']['master_bill_of_lading']) + 1)
        for step in text['job']['steps']:
            for external_data in step['external_data']:
                if external_data['label'] is not None and external_data['value'] is not None:
                    if external_data['label'] == 'Master BOL' or external_data['label'] == 'Shipper ID' \
                            or external_data['label'] == 'Shipper Order':
                        external_data['value'] = str(int(external_data['value']) + 1)
        return text

    def select_all(self, event):
        setings.transformed_text.tag_add(tk.SEL, "1.0", tk.END)
        setings.transformed_text.mark_set(tk.INSERT, "1.0")
        setings.transformed_text.see(tk.INSERT)
        return 'break'

    def select_all_t(self, event):
        setings.raw_job_text.tag_add(tk.SEL, "1.0", tk.END)
        setings.raw_job_text.mark_set(tk.INSERT, "1.0")
        setings.raw_job_text.see(tk.INSERT)
        return 'break'

    def delete_all(self, event):
        setings.raw_job_text.delete("1.0", tk.END)
        return 'break'

from jsonschema import validate, ValidationError

# Python3
try:
    from tkinter import messagebox
# Python2
except:
    import tkMessageBox as messagebox


class Schema(object):

    def __init__(self):
        self.schema = {
            "type": "object",
            "required": [
                "job"
            ],
            "properties": {
                "job": {
                    "type": "object",
                    "required": [
                        "steps",
                        "shipment_details"
                    ],
                    "properties": {
                        "steps": {
                            "type": "array",
                            "minItems": 1,
                            "additionalItems": True,
                            "items": {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "required": [
                                            "external_data"
                                        ],
                                        "properties": {
                                            "external_data": {
                                                "type": "array",
                                                "additionalItems": True,
                                                "items": {
                                                }
                                            }
                                        },
                                        "additionalProperties": True
                                    }
                                ]
                            }
                        },
                        "shipment_details": {
                            "type": "object",
                            "required": [
                                "master_bill_of_lading"
                            ],
                            "properties": {
                                "master_bill_of_lading": {
                                    "type": "string",
                                    "minLength": 1,
                                    "message": "Short Short",
                                }
                            },
                            "additionalProperties": True
                        }
                    },
                    "additionalProperties": True
                }
            },
            "additionalProperties": True
        }

    def validate_json(self, json_data):
        try:
            validate(instance=json_data, schema=self.schema)
        except ValidationError as err:
            messagebox.showerror("ERROR", err.message)
            return False
        return True

# -*- encoding: utf-8 -*-

strategy_list = [
    "Random",
    "MovingAverage",
    "SampleStrategy",
]

choices = list(zip(strategy_list, strategy_list))

parameters = {
    "": {},
    "Random": {
        "seed": {
            "dtype": int,
            "label": "Seed value",
            "placeholder": "Pick a seed number",
            "default": None,
        },
    },
    "MovingAverage": {
        "window": {
            "dtype": int,
            "label": "Window size",
            "placeholder": "Choose a window size",
            "default": None,
        },
        "smoothing": {
            "dtype": bool,
            "label": "Do some magical smoothing",
            "default": True,
        },
    },
    "SampleStrategy": {
        "int_value": {
            "dtype": int,
            "label": "Integer",
            "placeholder": "Insert a valid integer",
            "default": None,
        },
        "float_value": {
            "dtype": float,
            "label": "Float point value",
            "placeholder": "Insert a float point",
            "default": None,
        },
        "string_value": {
            "dtype": str,
            "label": "String",
            "placeholder": "Enter some text",
            "default": "Example",
        },
        "bool_value": {
            "dtype": bool,
            "label": "Checkbox boolean",
            "default": True,
        },
    },
}

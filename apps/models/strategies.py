# -*- encoding: utf-8 -*-

strategy_list = [
    "Random",
    "MovingAverage",
    "SampleStrategy",
]

choices = list(zip(strategy_list, strategy_list))

parameters = {
    "": {},
    "Random": {"seed": int},
    "MovingAverage": {"window": int, "smoothing": bool},
    "SampleStrategy": {"int": int, "float": float, "string": str, "bool": bool},
}

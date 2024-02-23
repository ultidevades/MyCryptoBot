import importlib
import inspect
import os
from typing import get_args

from stratestic.utils.helpers import get_extended_name, clean_docstring

from model.service.cloud_storage import download_models, get_saved_models, check_aws_config
from model.service.helpers import (
    STRATESTIC_STRATEGIES_LOCATION,
    LOCAL_STRATEGIES_LOCATION,
    LOCAL_MODELS_LOCATION
)


def map_type(element):

    try:
        type_ = element.__name__
    except AttributeError:
        type_ = type(element).__name__

    if type_ in ['int', 'float']:
        return {
            "type": "number",
            "func": "Number"
        }
    elif type_ == 'str':
        return {
            "type": "string",
            "func": "String"
        }


def process_ml_strategies(strategies_obj):

    estimator = strategies_obj["MachineLearning"]["optionalParamsOrder"][0]

    strategies_obj = {
        **strategies_obj,
        "MachineLearning": {
            **strategies_obj["MachineLearning"],
            "name": "MachineLearning (Create)",
            "params": {
                estimator: strategies_obj["MachineLearning"]["optionalParams"].pop(estimator)
            },
            "paramsOrder": [strategies_obj["MachineLearning"]["optionalParamsOrder"].pop(0)],
        },
        "MachineLearning-load": {
            **strategies_obj["MachineLearning"],
            "name": "MachineLearning (Load)",
            "params": {"load_model": {
                "type": {
                    "type": "string",
                    "func": "String"
                },
                "options": get_saved_models(LOCAL_MODELS_LOCATION)
            }},
            "paramsOrder": ["load_model"],
            "optionalParams": {},
            "optionalParamsOrder": [],
        }
    }

    return strategies_obj


def compile_strategies():

    # Download models from the cloud
    if os.getenv('USE_CLOUD_STORAGE') and check_aws_config():
        download_models(LOCAL_MODELS_LOCATION)

    strategies = {}

    for location in [STRATESTIC_STRATEGIES_LOCATION, LOCAL_STRATEGIES_LOCATION]:

        for name, cls in inspect.getmembers(importlib.import_module(location), inspect.isclass):

            required = {}
            optional = {}
            required_ordering = []
            optional_ordering = []

            params = inspect.signature(cls.__init__).parameters

            for param, props in params.items():

                if param in ["self", "data", "kwargs"]:
                    continue

                is_required = False

                if props.default is inspect._empty:
                    is_required = True

                args = get_args(props.annotation)

                if len(args) != 0:
                    param_info = {"type": map_type(args[0])}

                    if type(args[0]) is not type:
                        param_info.update({"options": args})
                else:
                    param_info = {
                         "type": map_type(props.annotation)
                    }

                if is_required:
                    required_ordering.append(param)
                    required[param] = param_info
                else:
                    optional_ordering.append(param)
                    optional[param] = param_info

            strategies[name] = {
                "name": get_extended_name(name),
                "className": name,
                "info": clean_docstring(cls.__doc__),
                "params": required,
                "optionalParams": optional,
                "paramsOrder": required_ordering,
                "optionalParamsOrder": optional_ordering
            }

    return process_ml_strategies(strategies)

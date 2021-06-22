#!/usr/bin/env python3
"""Script used to setup runtime environment and invoke quantum program."""

import sys
import json

from qiskit import Aer
from qiskit.providers.ibmq.runtime import UserMessenger, RuntimeDecoder
from program import main


if __name__ == '__main__':
    backend = Aer.get_backend('aer_simulator')

    messenger = UserMessenger()

    params_filename = 'params.json'
    if len(sys.argv) > 1:
        params_filename = sys.argv[1]

    try:
        with open(params_filename) as f:
            params = f.read()
    except FileNotFoundError:
        print("params file was not found")
        raise

    try:
        user_params = json.loads(params, cls=RuntimeDecoder)
    except json.decoder.JSONDecodeError:
        print(f"error loading {params_filename}: {params}")
        raise

    main(backend, messenger, **user_params)

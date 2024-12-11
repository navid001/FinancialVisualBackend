#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$DIR/venv/bin/activate"

"$DIR/venv/bin/gunicorn" run:app
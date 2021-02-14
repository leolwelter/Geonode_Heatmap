#!/bin/bash

# pkill -TERM -fl supervisor first, then
supervisord -c "$PWD"/supervisord.conf

#!/usr/bin/env bash

find $1 -maxdepth 1 \( -name '*.c' -or -name '*.so' -or -name '*.pyc' \) -delete

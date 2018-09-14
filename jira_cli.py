#!/usr/bin/env python3

"""ncurses, depending on argv[0] different presets are used from .conf file
e.g. start ncurses, get password on stdin, try to log in, select issue type if argv[0] is ambiguous,
set title, severity, description, sprint number, assign to me,
if incident: severity: high by defautl
if change: use change template, dont set in progress
"""
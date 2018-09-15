#!/usr/bin/env python3

import curses
from jira import JIRA
import yaml
import argparse

"""ncurses, depending on argv[0] different presets are used from .conf file
e.g. start ncurses, get password on stdin, try to log in, select issue type if argv[0] is ambiguous,
set title, severity, description, sprint number, assign to me,
if incident: severity: high by defautl
if change: use change template, dont set in progress
"""




def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-p', '--password-file', action='store', default='',
                        help='file with password, otherwise stdin is read')
    parser.add_argument('-c', '--config', action='store', default='~/.jira_cli.conf',
                        help='jira_cli config file')
    parser.add_argument('-i', '--issue', action='store', default='', help='type of issue, e.g. incident, change ...')



def main():
    parse_arguments()
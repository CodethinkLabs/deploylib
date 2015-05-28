# Copyright (C) 2015  Codethink Limited
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


'''Utility functions used by deploylib.'''


import os
import subprocess


def shell_quote(string):
    '''Return a shell-quoted version of `string`.'''
    lower_ascii = 'abcdefghijklmnopqrstuvwxyz'
    upper_ascii = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '-_/=.,:'
    safe = set(lower_ascii + upper_ascii + digits + punctuation)

    quoted = []
    for character in string:
        if character in safe:
            quoted.append(character)
        elif character == "'":
            quoted.append('"\'"')
        else:
            quoted.append("'%c'" % character)

    return ''.join(quoted)


def run_ssh_command(host, command):
    '''Run `command` over SSH on `host`.'''
    ssh_cmd = ['ssh', host, '--'] + [shell_quote(arg) for arg in command]
    return subprocess.check_output(ssh_cmd)


def write_from_dict(filepath, d, validate=lambda x, y: True):
    '''Takes a dictionary and appends the contents to a file

    An optional validation callback can be passed to perform validation on
    each value in the dictionary.

    e.g.

        def validation_callback(dictionary_key, dictionary_value):
            if not dictionary_value.isdigit():
                raise Exception('value contains non-digit character(s)')

    Any callback supplied to this function should raise an exception
    if validation fails.
    '''

    # Sort items asciibetically
    # the output of the deployment should not depend
    # on the locale of the machine running the deployment
    items = sorted(d.iteritems(), key=lambda (k, v): [ord(c) for c in v])

    for (k, v) in items:
        validate(k, v)

    with open(filepath, 'a') as f:
        for (_, v) in items:
            f.write('%s\n' % v)

        os.fchown(f.fileno(), 0, 0)
        os.fchmod(f.fileno(), 0644)

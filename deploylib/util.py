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

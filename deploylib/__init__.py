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


"""deploylib module

This module contains common code used by the deployment scripts in
scripts/write. A "write" script can subclass
`deploylib.writeexts.WriteExtension` and implement a `run_extension()`
function to be able to make use of its helper methods.

"""


from deploylib import util
from deploylib import writeexts


class ScriptError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

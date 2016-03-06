# Data Dissector - A modular and user friendly portable offline web platform
# designed to aid in diagnostic, repair and system information aggregation.
#
# Copyright (C) 2016  Joshua Michael Pendergrast
#
# This file is part of Data Dissector.
#
#    Data Dissector is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Data Dissector is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Data Dissector. If not, see <http://www.gnu.org/licenses/>.
#

import os.path

dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, "static")
TEMPLATE_PATH = os.path.join(dirname, "template")

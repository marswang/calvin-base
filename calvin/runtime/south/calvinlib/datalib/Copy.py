# -*- coding: utf-8 -*-

# Copyright (c) 2017 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from calvin.runtime.south.calvinlib import base_calvinlib_object
import copy

class Copy(base_calvinlib_object.BaseCalvinlibObject):
    """
    Functions for making copies of data
    """

    init_schema = {
        "description": "setup copy functions",
    }
    
    copy_schema = {
        "description": "create a copy given data",
        "type": "object"
        
    }

    def init(self):
        pass
        
    def copy(self, string):
        return copy.copy(string)


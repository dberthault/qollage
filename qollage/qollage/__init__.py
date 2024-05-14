# Copyright © 2023-2024 HQS Quantum Simulations GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

"""Typst interface and backend for qoqo.

Translates qoqo circuits to a Typst image via the Backend,
and saves the image as a png file or diplay it in the output.

.. autosummary::
    :toctree: generated/

    TypstBackend

"""

from .qollage import *  # type: ignore

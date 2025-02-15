# Copyright 2024 DeepMind Technologies Limited
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
# ==============================================================================
"""Utility functions for USD exporter."""
import numpy as np


def set_attr(attr, value, frame) -> None:
    if frame is None:
        attr.Set(value)
    else:
        attr.Set(value, frame)


def get_texture_name(texid, rgba) -> str:
    # returns a name for image to store
    res = f"texid{str(texid)}"
    res += f"_rgba"
    for v in rgba[0:3]:
        res += f"_{str(v)}"
    res += ".png"
    return res


def create_transform_matrix(rotation_matrix, translation_vector) -> np.array:
    # Ensure rotation_matrix and translation_vector are NumPy arrays
    rotation_matrix = np.array(rotation_matrix)
    translation_vector = np.array(translation_vector)

    transform_matrix = np.eye(4)
    transform_matrix[:3, :3] = rotation_matrix
    transform_matrix[:3, 3] = translation_vector

    return transform_matrix

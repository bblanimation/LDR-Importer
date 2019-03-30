# -*- coding: utf-8 -*-
"""LDR Importer GPLv2 license.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

"""

# Blender imports
import bpy

# Addon imports
from . import import_ldraw

bl_info = {
    "name": "LDR Importer",
    "description": "Import LDraw models in .ldr and .dat format",
    "author": "LDR Importer developers and contributors",
    "version": (1, 4, 1),
    "blender": (2, 80, 0),
    "api": 31236,
    "location": "File > Import",
    "warning": "Incomplete Cycles support, MPD and Bricksmith models not supported",  # noqa
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Import-Export/LDRAW_Importer",  # noqa
    "tracker_url": "https://github.com/le717/LDR-Importer/issues",
    "category": "Import-Export"
    }


def menuImport(self, context):
    """Import menu listing label."""
    self.layout.operator(import_ldraw.IMPORT_SCENE_OT_ldraw.bl_idname,
                         text="LDraw (.ldr/.dat)")

def make_annotations(cls):
	"""Add annotation attribute to class fields to avoid Blender 2.8 warnings"""
	if not hasattr(bpy.app, "version") or bpy.app.version < (2, 80):
		return cls
	bl_props = {k: v for k, v in cls.__dict__.items() if isinstance(v, tuple)}
	if bl_props:
		if '__annotations__' not in cls.__dict__:
			setattr(cls, '__annotations__', {})
		annotations = cls.__dict__['__annotations__']
		for k, v in bl_props.items():
			annotations[k] = v
			delattr(cls, k)
	return cls

def b280():
    return bpy.app.version >= (2,80,0)

classes = [import_ldraw.IMPORT_SCENE_OT_ldraw]

def register():
    """Register Menu Listing."""
    for cls in classes:
        make_annotations(cls)
        bpy.utils.register_class(cls)
    getattr(bpy.types, "TOPBAR_MT_file_import" if b280() else "INFO_MT_file_import").append(menuImport)


def unregister():
    """Unregister Menu Listing."""
    getattr(bpy.types, "TOPBAR_MT_file_import" if b280() else "INFO_MT_file_import").remove(menuImport)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

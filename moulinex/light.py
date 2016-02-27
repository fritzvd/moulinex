import bpy
import mathutils
from math import radians

from moulinex.material import add_material


def create_light(location=(0, 0, 20), scale=(20, 20, 20), strength=1):
    """
    Add a mesh light for cycles
    """

    # Add new plane)

    bpy.ops.mesh.primitive_plane_add(location=location)
    plane = bpy.context.active_object
    plane.name = 'Light Plane'
    plane.scale = mathutils.Vector(scale)
    # tilt
    # plane.rotation_euler.rotate_axis('Y', radians(40))

    material, emission = add_material(
        plane,
        'Plane Light Emission Shader',
        'ShaderNodeEmission'
    )
    emission.inputs['Strength'].default_value = strength

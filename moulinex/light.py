import bpy
import mathutils

from moulinex.material import add_material


def create_light(location=(0, 0, 20), scale=(20, 20, 20), strength=1):
    """
    Create a mesh that emits light.

    Keyword arguments:
    location -- 3d vector that expects the location in x, y, z format.
    scale -- 3d vector that expects the scale in x, y, z format.
    strength -- how much the mesh should be emitting
    """


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
    return plane

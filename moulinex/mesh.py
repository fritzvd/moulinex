import bpy
import mathutils
from math import radians

from moulinex.material import add_mix_material, add_material


def add_ball(location=(0, 2, 1), material=add_mix_material,
             color=(0.8, 0.8, 0.8, 0.9)):
    bpy.ops.mesh.primitive_uv_sphere_add(
        location=location
        )
    bpy.ops.object.shade_smooth()
    bpy.ops.rigidbody.object_add()
    material(bpy.context.active_object, 'Ball Material', color=color)
    return bpy.context.active_object


def passive_underground():
    bpy.ops.mesh.primitive_plane_add(location=(0, 0, 0))
    bpy.ops.rigidbody.objects_add()
    mesh = bpy.context.active_object
    mesh.name = 'Underground'
    mesh.scale = mathutils.Vector((20, 20, 20))
    bpy.ops.rigidbody.object_add()
    mesh.rigid_body.type = 'PASSIVE'
    material, new_shader_material = add_material(mesh, 'DiffuseUnderground')
    mesh.active_material = material
    return mesh


def create_room():
    wall = passive_underground()
    wall.rotation_euler.rotate_axis('Y', radians(90))
    wall.location.x = -19
    wall2 = passive_underground()
    wall2.location.y = 19
    wall2.rotation_euler.rotate_axis('X', radians(90))


def duplicate_object(scene, name, copyobj):

    # Create new mesh
    mesh = bpy.data.meshes.new(name)

    # Create new object associated with the mesh
    ob_new = bpy.data.objects.new(name, mesh)

    # Copy data block from the old object into the new object
    ob_new.data = copyobj.data.copy()
    ob_new.scale = copyobj.scale
    ob_new.location = copyobj.location

    # Link new object to the given scene and select it
    scene.objects.link(ob_new)
    ob_new.select = True

    return ob_new

"""
Helper functions that don't belong anywhere else.

* bake
* setup
"""

import bpy

def setup(samples=100):
    """Setup a blender scene, with some preferred defaults.

    Meaning, remove the standard objects, and give me a blank space, without
    cameras, lights or anything. And switch the rendering engine to Cycles.
    """
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = samples
    bpy.context.scene.render.tile_x = 128
    bpy.context.scene.render.tile_y = 128

    for obj in bpy.data.objects:
        try:
            bpy.context.scene.objects.unlink(obj)
        except:
            print('already out of scene')
        try:
            bpy.data.objects.remove(obj)
        except:
            print('already out of data')


def bake():
    """Bake shorthand function."""
    bpy.ops.ptcache.free_bake_all()
    bpy.ops.ptcache.bake_all()

import bpy

def setup(samples=100):
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
    bpy.ops.ptcache.free_bake_all()
    bpy.ops.ptcache.bake_all()

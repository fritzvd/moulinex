import bpy

def setup():
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 100
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

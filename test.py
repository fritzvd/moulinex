from moulinex import mesh
from moulinex import light
from moulinex import camera
from moulinex import render
from moulinex import general


def main():
    general.setup()
    mesh.passive_underground()
    light.create_light(scale=(5, 5, 5))

    ball = mesh.add_ball()
    mesh.add_modifier(ball, 0, 6, 6)
    mesh.add_modifier(ball, 1, 6, 6)
    mesh.add_modifier(ball, 2, 6, 6)

    camera.create_dof_camera()
    render.render_to_still()

main()

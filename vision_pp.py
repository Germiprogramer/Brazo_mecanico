from pyniryo2 import *

def vision_pick_and_place(robot: NiryoRobot, workspace_name: str):

    # Definimos la posicion en la que el robot observará el objeto
    observation_pose = PoseObject(
    x=0.16, y=0.0, z=0.35,
    roll=0.0, pitch=1.57, yaw=0.0,
    )

    # Posicion donde se colocara el objeto
    place_pose = PoseObject(
    x=0.0, y=-0.2, z=0.12,
    roll=0.0, pitch=1.57, yaw=-1.57
    )

    # Ponemos el robot para que pueda ver el escritorio
    print("Poniendo el robot en posición de visión...")
    robot.move_to_pose(observation_pose)

    # Trying to pick target using camera
    obj_found, shape_ret, color_ret = robot.vision.vision_pick(workspace_name)
    if obj_found:
        robot.place_from_pose(place_pose)
    else:
        print("No se ha encontrado ningún objeto. Revisa:")
        print("\n")
        print("Nothing obstruct the camera field of view")
        print("The workspace’s 4 markers are visible")
        print("At least 1 object is placed fully inside the workspace")

    robot.set_learning_mode(True)



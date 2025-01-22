from pyniryo2 import *

robot = NiryoRobot("10.10.10.10")

try:
    robot.calibrate_auto()
    robot.update_tool()

    # Captura imagen y detecta color
    workspace_name = "default_workspace"
    detected_objects = robot.get_color_detection(workspace_name)

    for obj in detected_objects:
        color = obj["color"]
        x, y, z = obj["position"]

        print(f"Detectado objeto {color} en posición {x, y, z}")

        # Mueve el objeto dependiendo del color
        if color == "red":
            robot.move_pose(x, y, z)
            robot.grasp_with_tool()
            robot.move_pose(0.1, 0.1, 0.1)  # Área para objetos rojos
            robot.release_with_tool()
        elif color == "blue":
            robot.move_pose(x, y, z)
            robot.grasp_with_tool()
            robot.move_pose(0.2, 0.2, 0.1)  # Área para objetos azules
            robot.release_with_tool()

finally:
    robot.close_connection()

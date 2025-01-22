from pyniryo2 import *

def launch():
    try: 
        # Creamos el robot
        robot = NiryoRobot("<Direccion brazo>")
        print("Conexión establecida")

        # Calibramos el brazo
        print("Calibrando...")
        robot.calibrate_auto()

        # Definir las posiciones

        # Posicion inicial del brazo
            # pitch = 1.57 rad para que mire hacia abajo
            # z = 0.2 m de altura

        print("Definiendo posiciones...")
        home_pose = PoseObject(x=0.0, y=0.0, z=0.2, roll=0.0, pitch=1.57, yaw=0.0)

        # Posicion del objeto
            # pitch = 1.57 rad para que mire hacia abajo
            # z = 0.1 m de altura
            # y = 0.1 m de distancia a la derecha
            # x = 0.2 m de distancia hacia adelante
        object_pose = PoseObject(x=0.2, y=0.1, z=0.1, roll=0.0, pitch=1.57, yaw=0.0) 

        # Moverse al objeto
        print("Moviéndose al objeto...")
        robot.move_to_pose(object_pose)

        # Coger el objeto
        print("Cogiendo el objeto...")
        robot.close_gripper()

        # Moverse a la posición inicial
        print("Volviendo a la posición inicial...")
        robot.moveto_pose(home_pose)

        # Soltar el objeto
        print("Soltando el objeto...")
        robot.open_gripper()

        print("Proceso completado.")

    except NiryoRobotException as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión
        robot.close_connection()
        print("Conexión cerrada.")
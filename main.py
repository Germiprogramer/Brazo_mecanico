from launch import pick_and_place

if __name__ == "__main__":
    try: 
        # Creamos el robot
        workspace_name = "UAX_lab"
        robot = NiryoRobot("<Direccion brazo>")
        print("Conexión establecida")

        # Calibramos el brazo
        print("Calibrando...")
        robot.calibrate_auto()

    except NiryoRobotException as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión
        robot.end()
        print("Conexión cerrada.")


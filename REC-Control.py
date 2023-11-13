import time
import codrone

# Create a Codrone object
codrone = codrone.Codrone()

# Map the left joystick to the left motor
codrone.set_motor_control(codrone.MOTOR_LEFT, codrone.LEFT_JOYSTICK)

# Map the right joystick to the right motor
codrone.set_motor_control(codrone.MOTOR_RIGHT, codrone.RIGHT_JOYSTICK)

# Map the left button to the yaw motor
codrone.set_motor_control(codrone.MOTOR_YAW, codrone.LEFT_BUTTON)

# Map the right button to the pitch motor
codrone.set_motor_control(codrone.MOTOR_PITCH, codrone.RIGHT_BUTTON)

# Start the motors
codrone.start_motors()

try:
    while True:
        # Get the joystick values
        left_joystick_x, left_joystick_y = codrone.get_joystick_values(codrone.LEFT_JOYSTICK)
        right_joystick_x, right_joystick_y = codrone.get_joystick_values(codrone.RIGHT_JOYSTICK)

        # Set the motor speeds
        codrone.set_motor_speed(codrone.MOTOR_LEFT, left_joystick_y)
        codrone.set_motor_speed(codrone.MOTOR_RIGHT, right_joystick_y)

        # Set the yaw motor speed
        if left_joystick_x < -0.5:
            codrone.set_motor_speed(codrone.MOTOR_YAW, -1)
        elif left_joystick_x > 0.5:
            codrone.set_motor_speed(codrone.MOTOR_YAW, 1)
        else:
            codrone.set_motor_speed(codrone.MOTOR_YAW, 0)

        # Set the pitch motor speed
        if right_joystick_x < -0.5:
            codrone.set_motor_speed(codrone.MOTOR_PITCH, -1)
        elif right_joystick_x > 0.5:
            codrone.set_motor_speed(codrone.MOTOR_PITCH, 1)
        else:
            codrone.set_motor_speed(codrone.MOTOR_PITCH, 0)

        # Wait for a short period of time
        time.sleep(0.01)

except KeyboardInterrupt:
    # Stop the motors
    codrone.stop_motors()

    # Exit the program
    exit(0)

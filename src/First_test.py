from fanucpy import Robot
from multiprocessing import Process

RightBot = Robot(
    robot_model="Fanuc",
    host="192.168.5.52",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)

LeftBot = Robot(
    robot_model="Fanuc",
    host="192.168.5.153",
    port=18735,
    ee_DO_type="RDO",
    ee_DO_num=7,
)
def right_bot_routine():
    RightBot.__version__()
    RightBot.connect()
    # move in joint space
    RightBot.move(
        "joint",
        vals=[0, 0, 0, 0, 0, 0],
        velocity=100,
        acceleration=100,
        cnt_val=0,
        linear=False
    )
    # move in cartesian space
    #RightBot.move(
    #    "pose",
    #    vals=[0.0, -28.0, -35.0, 0.0, -55.0, 0.0],
    #    velocity=50,
    #    acceleration=50,
    #    cnt_val=0,
    #    linear=False
    #)

#test response

#def left_bot_routine():
#    LeftBot.__version__()
#    LeftBot.connect()
    



# get robot state
print(f"Current pose: {RightBot.get_curpos()}")
print(f"Current joints: {RightBot.get_curjpos()}")
print(f"Energy consumption: {RightBot.get_ins_power()}")
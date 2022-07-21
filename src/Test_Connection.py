import multiprocessing
from fanucpy import Robot
from multiprocessing import Process

NUM_THREADS = 2

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


def left_bot_routine():
    
    LeftBot.__version__()
    LeftBot.connect() 
    for x in range(1,50): 
        LeftBot.move(
            "joint",
            vals=[-90, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )
        print(f"Current pose: {LeftBot.get_curpos()}")
        LeftBot.move(
            "joint",
            vals=[0, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )
        print(f"Current pose: {LeftBot.get_curpos()}")



def right_bot_routine():
    RightBot.__version__()
    RightBot.connect()
    for x in range(1,50):
        RightBot.move(
            "joint",
            vals=[90, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )
        print(f"Current pose: {RightBot.get_curpos()}")
        RightBot.move(
            "joint",
            vals=[0, 0, 0, 0, 0, 0],
            velocity=50,
            acceleration=50,
            cnt_val=0,
            linear=False
        )
        print(f"Current pose: {RightBot.get_curpos()}")



if __name__=='__main__':
    max_speed = 100
    max_accel = 100 
    
    p1 = multiprocessing.Process(target = left_bot_routine())
    p2 = multiprocessing.Process(target = right_bot_routine())
    p1.start()
    p2.start()
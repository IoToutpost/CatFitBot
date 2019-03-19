#!/usr/bin/env python

import logging
import random
import time

import pantilthat
from gpiozero import LED
from gpiozero import MotionSensor

DELAY = 1
HORIZONTAL_RANGE = 90
VERTICAL_RANGE = 90
SWITHCH_ON_LED = 0
LOG_FILENAME = 'logs/CatFitBot.log'

# Create a custom logger
logger = logging.getLogger(__name__)
handler2 = logging.StreamHandler()  # handler for routine view
handler1 = logging.FileHandler(LOG_FILENAME)

# Create handlers
format1 = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
format2 = logging.Formatter('%(name)s - %(message)s')
handler1.setFormatter(format1)
handler2.setFormatter(format2)

# Create formatters and add it to handlers

logger.addHandler(handler1)
logger.addHandler(handler2)

logger.info('This is an error')
logger.log(level=40, msg='This is an error4')

logger.log(level=40, msg="The Application is starting")
logger.log(level=40, msg='This is an information')

pir = MotionSensor(4)
led3 = LED(18)
led1 = LED(24)
led2 = LED(23)


def led_random(number=1):
    """
    :param number: maximum number of led(s) simultaneously switch on.
    in case of zero only one ld is used.
    :return: none
    """
    if number == 0:
        uplimit = 1
    elif number == 1:
        uplimit = 3
    elif number == 2:
        uplimit = 6
    else:
        uplimit = 7

    k = random.randint(1, uplimit)
    time.sleep(DELAY * k / 20.)
    if k == 1:
        led1.off()
        led2.off()
        led3.on()
    elif k == 2:
        led1.off()
        led2.on()
        led3.off()
    elif k == 3:
        led1.on()
        led2.off()
        led3.off()
    elif k == 4:
        led1.on()
        led2.on()
        led3.off()
    elif k == 5:
        led1.on()
        led2.off()
        led3.on()
    elif k == 6:
        led1.off()
        led2.on()
        led3.on()
    elif k == 7:
        led1.on()
        led2.on()
        led3.on()


while True:
    led1.off()
    led2.off()
    led3.off()
    print("Waiting")
    logger.log(level=40, msg="Waiting to start")
    pir.wait_for_motion()
    logger.log(level=40, msg="Started the post wait")

    led_random(number=SWITHCH_ON_LED)
    print("Led 1 on")

    # Reset the time
    t = time.time()
    t2 = time.time()

    a1 = random.randint(40, 90) * (-1)

    k = random.randint(1, 10)
    b1 = random.randint(0, 80) - 40
    while t2 - t < 60:
        logger.info('routi for 1 minute')
        print("Time: t2--> {} t--> {} delta--> {}".format(t2, t, t2 - t))
        # Get th
        a2 = random.randint(40, 90) * (-1)

        #k = random.randint(1, 10)
        b2 = random.randint(0, 80) - 40
        print("{}  {}".format(a1, b1))
        print("{}  {}".format(a2, b2))

        a_step = (a1 - a2) / 10
        b_step = (b1 - b2) / 10

        # micro movement
        for i in range(10):
            print("init {} finale{} step {} posizione {} delta {}".format(a1, a2, i, int(a1 - i * a_step), a_step))
            pantilthat.pan(int(b1 - i * b_step))
            pantilthat.tilt(int(a1 - i * a_step))

            # Two decimal places is quite enough!
            print(round(b1, 2))

            led_random(number=SWITHCH_ON_LED)
            time.sleep(DELAY * 0.1)
        a1 = a2
        b1 = b2
        k = random.randint(1, 10)

        time.sleep(DELAY * 5 / k)
        t2 = time.time()
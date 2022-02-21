import switch
import camera
import signal
import RPi.GPIO as GPIO


def handler(signum, frame):
    GPIO.cleanup()

if __name__ == "__main__":
    print("---This is a Motor control application developed by InTunnelz---")
    signal.signal(signal.SIGINT, handler)
    switch.setupButton()
    camera.captureFrame()

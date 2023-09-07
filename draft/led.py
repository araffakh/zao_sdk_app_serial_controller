import time

def flash_led(led):
    status=False
    while True:
        if status==True:
            led_status="on"
            status=False
            print(f"the {led} is",led_status)
        else:
            led_status="off LED"
            status=True
            print(f"the {led} is",led_status)
        time.sleep(1)
    
for i in range(10):
    flash_led("Tx")
    
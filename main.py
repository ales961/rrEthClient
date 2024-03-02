import connection

LED_RED_GET_STATE = '0xA001'
LED_RED_ON = '0xA002'
LED_RED_OFF = '0xA003'
LED_YELLOW_GET_STATE = '0xA011'
LED_YELLOW_ON = '0xA012'
LED_YELLOW_OFF = '0xA013'
LED_GREEN_GET_STATE = '0xA021'
LED_GREEN_ON = '0xA022'
LED_GREEN_OFF = '0xA023'
BUTTON_GET_STATE = '0xB001'
BUZZER_ON = '0xC002'
BUZZER_OFF = '0xC003'

commands = {'led red state': LED_RED_GET_STATE, 'led red on': LED_RED_ON, 'led red off': LED_RED_OFF,
            'led yellow state': LED_YELLOW_GET_STATE, 'led yellow on': LED_YELLOW_ON, 'led yellow off': LED_YELLOW_OFF,
            'led green state': LED_GREEN_GET_STATE, 'led green on': LED_GREEN_ON, 'led green off': LED_GREEN_OFF,
            'button state': BUTTON_GET_STATE, 'buzzer on': BUZZER_ON, 'buzzer off': BUZZER_OFF}

if __name__ == '__main__':
    while True:
        input('Press ENTER to connect...')
        s = connection.tcpConnect()
        print("Connected")
        while True:
            try:
                user_input = input()
                for command in commands:
                    if command == user_input:
                        bytes_data = bytes.fromhex(commands[command].replace('0x', ''))
                        swapped_bytes_data = bytes_data[1:2] + bytes_data[0:1] + bytes_data[2:]
                        s.sendall(swapped_bytes_data)
                        recv_data = s.recv(256)
                        print(recv_data.decode('utf-8'))
                        break
            except:
                print("Unable to connect")

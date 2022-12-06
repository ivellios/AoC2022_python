

def process_signal(input_data, message_length):
    position = 1
    window = [*(input_data[:message_length])]
    for i in input_data:
        window = window[-(message_length-1):]
        window.append(i)
        if len(set(window)) == message_length:
            break
        position += 1
    return position

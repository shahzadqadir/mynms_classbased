from log import Log


def load_messages_from_text_file(filename):
    log_messages = []
    with open(filename) as file:
        for line in file:
            log = Log()
            log.load_from_string(line)
            log_messages.append(log)
    return log_messages

def flush_empty_logs(filename):
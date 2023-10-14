from utilities import load_messages_from_text_file

for log in load_messages_from_text_file("data/logs.txt"):
    if log.severity_level and log.severity_level >= 5:
        print(str(log).strip())

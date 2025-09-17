import logging

with open("soc_logs.log" ,"r" , encoding="utf-8") as file_read:
    for line in file_read:
        if ("Failed login" in line):
            with open("logineError.log", "a", encoding="utf-8") as file_error:
                file_error.write(line)
            

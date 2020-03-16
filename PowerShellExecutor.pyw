import os
import subprocess
from datetime import datetime
import time


def config_handler(start_text, end_text, config_file):
    # The following code is designed to import text from a config file.
    # It's designed to do this line by line.
    # start_text: The program will start importing after this point.
    # end_text: The program will stop importing when it reaches this point.
    # config_file: location where config file is stored.

    fr = open(config_file, 'r')
    text = fr.read()
    start = text.find(start_text) + len(start_text + "\n")
    end = text.find("\n" + end_text)
    substring = text[start:end]
    fr.close()

    return substring


def hedwig_protocol(listen_or_take, file_name, take_this):
    # THERE ARE TWO PARTS TO THIS FUNCTION:
    # -------------------------------------------------------------------------------------
    #
    # LISTEN:
    # This code is ment to be placed in a continues while loop.
    # If "listen" is selected the code will monitors a specific folder.
    # If there are text files inside, it will choose the oldest one and return the output.
    # Following this it will also remove the file.
    #
    # listen_or_take = "listen"
    # filename = The file path of the file you are monitoring.
    # take_this = ""
    #
    # -------------------------------------------------------------------------------------
    #
    # TAKE:
    # Code creates a file with text inside.
    #
    # listen_or_take = "take"
    # filename = The file path of the file you want to create.
    # take_this = The text you want to write to the file.
    #
    # -------------------------------------------------------------------------------------

    if listen_or_take == "listen":

        try:

            # Counts number of files in folder.
            file_count = sum([len(files) for r, d, files in os.walk(file_name)])

            if file_count > 0:
                # The following code is used to determine the oldest file in the folder.
                path = file_name
                os.chdir(path)
                files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

                oldest_file = files[0]
                # newest_file = files[-1]

                # now do something with the oldes file....
                fr = open(oldest_file)
                text = fr.read()
                fr.close()

                os.remove(oldest_file)  # Removes oldest file.

                return text

        except:
            # When a file is being copied while the Hedwig_protocol is running
            # it can cause and error, a delay helps with this.
            time.sleep(1)

    elif listen_or_take == "take":

        # WRITE TO A FILE
        fw = open(file_name, 'w')
        fw.write(take_this)
        fw.close()


PowerShellExecutorConfig = "PowerShellExecutorConfig.txt"
receive_form = config_handler("PowerShellExecutor Receive:", "PowerShellExecutor Send:", PowerShellExecutorConfig)
send_to = config_handler("PowerShellExecutor Send:", "End of Config", PowerShellExecutorConfig)


while True:
    now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    new_file = send_to + "\\" + now + ".txt"
    file_count = sum([len(files) for r, d, files in os.walk(receive_form)])

    if file_count > 0:

        script = hedwig_protocol("listen", receive_form, "")

        p1 = subprocess.run(["powershell.exe", script], capture_output=True, text=True)
        dof = open(new_file, "w")

        for line in p1.stdout.split('\n'):
            dof.write(line)
        dof.close()

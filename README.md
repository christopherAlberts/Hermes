# Hermes
A message bot worthy of the gods!

![](Images/HermesBanner.png)

This bot makes use of the Telegram API, it is however designed to work a bit unconventunaly...

## How It Works

The idea behind this bot was not to make a bot with a template reply. But rather one that that can interact with your programs, whatever they might be. This is done through means of an *exschange*. When a message is sent through. Hermes will determine which PO.Box in the exchange it should go to. It will then take the message to the *"From_Hermes"* folder in the PO.Box. The idea is that what ever program you are interacting with, will monitor the *"From_Hermes"* folder. Once a message comes throught the program will execute the command and return to output to the *"To_Hermes"* folder, at which point Hermes will take the output and use it as the responce to the original message sent.

The Beauty of this setup is that Hermes can interact with any program written in any languge, be it python, java, C# , C++ or even .bat scripts. Below is a diagram illestrating how this process works.

![](Images/Hermes_Workflow.png)

## Try It Out

### Getting All The Files And Libraries
First things first, you'll need to get your Telegram API key. It's free and simple just speak to the BotFather...https://core.telegram.org/bots#6-botfather

The Hermes messanger bot makes use of the pyTelegramBorAPI libary. Inoder for this program to work you'll need to install the required packages. The following link describes how to do this:   https://github.com/eternnoir/pyTelegramBotAPI

You can now proceed in pressing the big green button *"Clone or download"* located on the top right conner of the page and selecting *"Download ZIP"*.

### Creating The Exchange ###

The *Exchange* complex thou it might seem is just a set of folders inside each other.

You'll need on one main folder titled "Excange". With in this folder you need to create a "POBox#" folder for each program. The '#' reprasents the program's number, i.e "POBox0", "POBox1", "POBox2"... Remember computers start counting at "0" so start with "POBox0".
Inside every POBox folder you'll need the last remaining two folders namely, From_Hermes and To_Hermes.
The "From_Hermes" folder will contain the original message sent through. Your program will then take this as input. The output of the program should then be placed in the To_Hermes folder. Hermes will then take this and send it through as the responce to the original message.

You'll need to referince the path of the "From_Hermes" and "To_Hermes" folders in the config file. 

### Editing the Config File ###

You do not have to change any of the code you can use the executabile file as is. The only thing you'll need to change is the config file and to create the PO.Box file directories and refrince them accrodingly in this file. Also insure there are no blank lines in the config file. The file should also be located in the same directory as the Hermes.exe file and have the title "HermesConfig.txt". There is no limit to the number of programs Hermes can interact with.

Here's an example of the config file layout:

```
Hermes_Bot_Token:
982gkjh28746u42hraodsmcnB87345gjhg7347
Hermes 2 Exchange:
C:\Users\zeus\Codes\Python\scr\Exchange\POBox0\From_Hermes
C:\Users\zeus\Codes\Python\scr\Exchange\POBox1\From_Hermes
C:\Users\zeus\Codes\Python\scr\Exchange\POBox2\From_Hermes
C:\Users\zeus\Codes\Python\scr\Exchange\POBox3\From_Hermes
Exchange 2 Hermes:
C:\Users\zeus\Codes\Python\scr\Exchange\POBox0\To_Hermes
C:\Users\zeus\Codes\Python\scr\Exchange\POBox1\To_Hermes
C:\Users\zeus\Codes\Python\scr\Exchange\POBox2\To_Hermes
C:\Users\zeus\Codes\Python\scr\Exchange\POBox3\To_Hermes
Hermes Chat History File:
C:\Users\zeus\Codes\Python\scr\HermesChatHistory.txt
End of Config
```

With the config file, you'll also need to create a chat history file called "HermesChatHistory.txt". This file should also be refirinced in the config file.

### I'm Alive! ###

Once you are confident that you have edited the config file correctly and compiled the excange folder heirachy accordingly, then you can run the executable and send the wake-up command:

Either of the following will do:

```
/start  
/wakeup 
/areyoualive 
/areyoualive?
```

If everthing is set up correctly, you'll then recieve the following:

```
I'm alive!
```
This will indicate everything is working as it should. You can now start sending your commands through.


### Compiling The .exe ###

If you are cuirias to see how the code looks feel free to have a look at the Hermes.pyw file. The code is writen in such a way that no changes need to be made. You can use the Hermes.exe file as is. The only file that requires editing is the config file. 

If you do want to edit the code and run it as a .exe file, then there is a little trick you sould know about. The more perseptive of you might have noticed that we are using a .pyw file instead of a .py. The reason for this, to qoute the official documentation is as follows:

*"Python scripts (files with the extension .py) will be executed by python.exe by default. This executable opens a terminal, which stays open even if the program uses a GUI. If you do not want this to happen, use the extension .pyw which will cause the script to be executed by pythonw.exe by default (both executables are located in the top-level of your Python installation directory). This suppresses the terminal window on startup."* https://docs.python.org/2/using/windows.html

The reason we don't want to open the terminal, is somehow this lets the program run once and then it kills it. However we want Hermes to run continuasl non-stop and for this we'll need the .pyw exstension.

Now to make the .pyw file a .exe you'll need to install pyinstaller, learn how to do it over here:  https://www.pyinstaller.org/
When this is done you'll need to go to the directory via the command line and execute spesifically the following command:

```powershell
pyinstaller -F --hidden-import "babel.numbers" Hermes.pyw
```
### The Achilles Heel ###

There two things that should be noted. These are the two big limitation of this code. The first being that when Hermes sends a message through, it exspects a responce. __Nothing will happen until it recieves a responce.__ Only after a response is received, will you be able to send the next message through.

The second thing that sould be kept in mind is that Hermes only looks at the "To_Hermes" foolder (folder containing responce from the program) after a message is sent to the "From_Hermes" folder. What this means is a program that sends updated throught periodically will not work. Those updates will only be recieved after a message is sent.

## Create Your Own Program To Work With Hermes ##




![](Images/pythonpoweredlengthgif.gif)

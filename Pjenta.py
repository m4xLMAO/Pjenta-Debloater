from colorama import init, Fore, Back, Style
import sys
import os, shutil
from pathlib import Path
import winshell
import subprocess
import winreg




init()
print(" ")
print(Fore.YELLOW + "====================== PJENTA WIN10 DEBLOATER V.0.1 ======================")
print(Fore.WHITE + "=============== https://github.com/m4xLMAO/Pjenta-Debloater ==============")
print(Fore.WHITE + "================= Author: maxLMAO - youtube.com/@m4xLMAO =================")
print(" ")
print(Fore.WHITE + "Purpose: Optimize your computer or laptop for improved performance.")
print(" ")
print(Fore.RED + "NOTE: It's highly advisable to create a system restore point before initiating any modifications to your device. \n      Please be aware that we cannot accept responsibility for any potential damage to your device. ")
print(" ")

while True: 
        continue_res = input(Fore.WHITE + "      Continue? (" + Fore.LIGHTCYAN_EX + "y" + Fore.WHITE + "/" + Fore.RED + "n" + Fore.WHITE + "): ")
        

        if continue_res != "y" and continue_res != "n":
            print(Fore.RED + "==> ERROR: Choose " + Fore.LIGHTCYAN_EX + "y " + Fore.WHITE + "or" + Fore.RED + " n")

        elif continue_res == "n":
            sys.exit()
        else:
            print(" ")
            print("--------- " + Fore.YELLOW + "Performance Options" + Fore.WHITE + " --------------------------------------------")
            print(Fore.WHITE + "      1. Clean " + Fore.CYAN + "Temporary Files")
            print(Fore.WHITE + "      2. Clean " + Fore.CYAN + "Recycle Bin")
            print(Fore.WHITE + "      3. Disable all " + Fore.LIGHTBLUE_EX + "Startup Apps" + Fore.RED + " [This requires administrator]")
            print(Fore.WHITE + "      4. Disable all " + Fore.LIGHTBLUE_EX + "Visual Effects")
            print(Fore.WHITE + "      5. high performance " + Fore.LIGHTMAGENTA_EX + "Power Plan" + Fore.RED + " [Not recommended on Laptops]")
            print(Fore.WHITE + "      6. Repair " + Fore.LIGHTMAGENTA_EX + "Windows System " + Fore.WHITE + "files" + Fore.RED + " [This requires administrator]" + Fore.WHITE )
            print("--------------------------------------------------------------------------")
            print(" ")
            Choice = input("      Choice (" + Fore.GREEN + "1" + Fore.WHITE + "/" + Fore.GREEN + "6" + Fore.WHITE + "): ")
            print()
            if Choice != "1" and Choice != "2" and Choice != "3" and Choice != "4" and Choice != "5" and Choice != "6":
                 print(Fore.RED + "==> ERROR:" + Fore.WHITE + " Choose an existing option.\n") 

            def one():
                    try:
                        user_name = os.getlogin()
                        _temp_ =  "C:\\Users\\" + user_name + "\AppData\\Local\\Temp"
                        temp = "C:\\Windows\\Temp"

                        for filename in os.listdir(_temp_):
                            file_path = os.path.join(_temp_, filename)
                            try:
                                if os.path.isfile(file_path) or os.path.islink(file_path):
                                    os.unlink(file_path)
                                elif os.path.isdir(file_path):
                                    shutil.rmtree(file_path)
                            except Exception as e:
                                pass
                        
                        for filename in os.listdir(temp):
                            file_path = os.path.join(temp, filename)
                            try:
                                if os.path.isfile(file_path) or os.path.islink(file_path):
                                    os.unlink(file_path)
                                elif os.path.isdir(file_path):
                                    shutil.rmtree(file_path)
                            except Exception as e:
                                pass

                        print(Fore.GREEN + "Finished cleaning " + Fore.LIGHTGREEN_EX + "Temporary Files")

                    except PermissionError: 
                        print(Fore.RED + "==> ERROR: " + Fore.LIGHTYELLOW_EX + "Access Denied. Some files couldn't be deleted. Try running it as administrator \n")

            if Choice == "1":
                 print("Cleaning " + Fore.LIGHTYELLOW_EX + "Temporary Files" + Fore.WHITE + "...")
                 print(" ")
                 one()

            def two():
                print("Cleaning " + Fore.LIGHTYELLOW_EX + "Recycle Bin" + Fore.WHITE + "...")
                try:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                    print(Fore.GREEN + "Finished cleaning " + Fore.LIGHTGREEN_EX + "Recycle bin")
                except:
                    print(Fore.RED + "\n==> ERROR: Your Recycle Bin is Empty\n")

            if Choice == "2":
                two()

            def three():
                print(Fore.GREEN + "Finding all " + Fore.YELLOW + "Startup Apps" + Fore.GREEN +"... \n")
                def get_startup_app_names():
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
                    startup_app_names = []

                    try:
                        index = 0
                        while True:
                            name, _, _ = winreg.EnumValue(key, index)
                            startup_app_names.append(name)
                            index += 1
                    except WindowsError:
                        pass

                    return startup_app_names

                if __name__ == "__main__":
                    startup_app_names = get_startup_app_names()
                    for name in startup_app_names:
                        print(Fore.LIGHTCYAN_EX + "- " + name + "\n")
               
                print(Fore.GREEN + "Disabling " + Fore.LIGHTYELLOW_EX + "all Startup Apps" + Fore.GREEN + "...\n")

                def disable_all_startup_apps():
                                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)

                                    try:
                                        index = 0
                                        while True:
                                            name, _, _ = winreg.EnumValue(key, index)
                                            winreg.DeleteValue(key, name)
                                            index += 1
                                            print(Fore.GREEN + "All " + Fore.LIGHTGREEN_EX + "Startup Apps " + Fore.WHITE + "have been disabled.\n")
                                    except WindowsError:
                                        print(Fore.RED + "==> ERROR:" + Fore.WHITE + " An error has occured. Try running it as admininstrator.\n")


                if __name__ == "__main__":
                    disable_all_startup_apps()

                



            if Choice == "3":
                three()

            def four():
                try:
                    def disable_visual_effects():
                        print("Disabeling " + Fore.LIGHTYELLOW_EX + "Visual Effects" + Fore.WHITE + "...\n")
                        subprocess.Popen(['systempropertiesperformance.exe'])
                        
                        os.system("timeout /t 2 /nobreak > nul")

                        try:
                            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Control Panel\\System\\Performance')
                            
                            winreg.SetValueEx(key, 'VisualEffects', 0, winreg.REG_DWORD, 2)
                            
                            winreg.CloseKey(key)
                            print("\nFinished disabeling " + Fore.LIGHTYELLOW_EX + "Visual Effects" + Fore.WHITE + "...\n")
                        except Exception as e:
                            print(f"An error occurred: {e}")

                    if __name__ == "__main__":
                        disable_visual_effects()
                
                except OSError:
                     print(Fore.RED + "==> ERROR: " + Fore.WHITE + "Run the program with administrator.\n")
            
            if Choice == "4":
                 four()

            def five():

                command = 'powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c' 

                try:
                    print("Changing " + Fore.LIGHTYELLOW_EX + "Power Plan" + Fore.WHITE + "...\n")
                    subprocess.run(command, check=True, shell=True)
                    print("\nFinished changing " + Fore.LIGHTYELLOW_EX + "Power Plan" + Fore.WHITE + "...\n")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
            
            if Choice == "5":
                five()

            def six():
                command = ["DISM", "/Online", "/Cleanup-Image", "/RestoreHealth"]

                try:
                    print("Repairing " + Fore.LIGHTYELLOW_EX + "Windows System Files" + Fore.WHITE + "...\n")
                    subprocess.run(command, check=True)
                    print("\nFinished repairing " + Fore.LIGHTYELLOW_EX + "Windows System Files " + Fore.WHITE + "...\n")
                except subprocess.CalledProcessError:
                    print(Fore.RED + "\n ==> ERROR:" + Fore.WHITE + " An error has occured. Try running it as admininstrator.\n")

            if Choice == "6":
                 six()

            
                

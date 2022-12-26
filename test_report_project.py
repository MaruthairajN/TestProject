import json
import math
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

try:
    def main():
        def testing():
            print("Test Name Given For Report Generation :", str(sys.argv[1]))

            if (str(sys.argv[1]) == 'irtest'):
                ir_test()
                print("\t")
            elif (str(sys.argv[1]) == 'balancetest'):
                balance_test()
                print("\t")
            elif (str(sys.argv[1]) == 'bdvtest'):
                bdv_test()
                print("\t")
            else:
                print("Input invalid, kindly give a Correct Test name to generate report.")

        Tfr_Testing = testing()


    def ir_test():
        print("File Name entered :", sys.argv[2])
        try:
            with open(sys.argv[2], 'r') as f:
                data = json.load(f)
            print(Back.WHITE + Fore.BLACK + "Insulation Resistance Test Report")
            print("\t")
            print("Connection : ", data['1_Connections'], " ", " Applied Voltage : ", data['1_AppVolt'], "V")
            print("1 Min Value : ", data['1_OneMinValue'], " ", "10 Min Value : ", data['1_TenMinValue'])
            Pivalue1 = float(data['1_TenMinValue']) / float(data['1_OneMinValue'])
            if (Pivalue1 >= 2):
                print("PI value : ", round(Pivalue1, 3), " ", "Condition : ", Fore.GREEN + "GOOD")
            elif (Pivalue1 < 2 and Pivalue1 >= 1):
                print("PI value : ", round(Pivalue1, 3), " ", "Condition : ", Fore.YELLOW + "FAIR")
            else:
                print("PI value : ", round(Pivalue1, 3), " ", "Condition : ", Fore.RED + "POOR")
                print("Suggestion : Need Improvement")
            print("\t")

            print("Connection : ", data['2_Connections'], " ", "Applied Voltage : ", data['2_AppVolt'], "V")
            print("2 Min Value : ", data['2_OneMinValue'], " ", "10 Min Value : ", data['2_TenMinValue'])
            Pivalue2 = float(data['2_TenMinValue']) / float(data['2_OneMinValue'])

            if (Pivalue2 >= 2):
                print("PI value : ", round(Pivalue2, 3), " ", "Condition : ", Fore.GREEN + "GOOD")
            elif (Pivalue2 < 2 and Pivalue2 >= 1):
                print("PI value : ", round(Pivalue2, 3), " ", "Condition : ", Fore.YELLOW + "FAIR")
            else:
                print("PI value : ", round(Pivalue2, 3), " ", "Condition : ", Fore.RED + "POOR")
                print("Suggestion : Need Improvement")
            print("\t")

            print("Connection : ", data['3_Connections'], " ", "Applied Voltage : ", data['3_AppVolt'], "V")
            print("3 Min Value : ", data['3_OneMinValue'], " ", "10 Min Value : ", data['3_TenMinValue'])
            Pivalue3 = float(data['3_TenMinValue']) / float(data['3_OneMinValue'])

            if (Pivalue3 >= 2):
                print("PI value : ", round(Pivalue3, 3), " ", "Condition : ", Fore.GREEN + "GOOD")
            elif (Pivalue3 < 2 and Pivalue3 >= 1):
                print("PI value : ", round(Pivalue3, 3), " ", "Condition : ", Fore.YELLOW + "FAIR")
            else:
                print("PI value : ", round(Pivalue3, 3), " ", "Condition : ", Fore.RED + "POOR")
                print("Suggestion : Need Improvement")
            print("\t")
            print(Back.BLUE + Fore.BLACK + "IR Test Condition Verified & Report Generated")
        except:
            print("Invalid File input, unable to read json file")


    def balance_test():
        print("File Name entered :", sys.argv[2])
        try:
            with open(sys.argv[2], 'r') as f:
                data = json.load(f)
            print(Back.WHITE + Fore.BLACK + "Balance Test Report")
            print("\t")
            print("Phase Reading Values")
            print("R-Phase : ", data['1U1V'], " ", data['1V1W'], " ", data['1W1U'])
            print("B-Phase : ", data['2U2V'], " ", data['2V2W'], " ", data['2W2U'])
            print("Y-Phase : ", data['3U3V'], " ", data['3V3W'], " ", data['3W3U'])
            print("\t")
            A1 = float(data['1V1W']) + float(data['1W1U'])
            B1 = float(data['2U2V']) + float(data['2W2U'])
            C1 = float(data['3U3V']) + float(data['3V3W'])

            phase1 = math.isclose(data['1U1V'], A1, abs_tol=0.5)
            phase2 = math.isclose(data['2V2W'], B1, abs_tol=0.5)
            phase3 = math.isclose(data['3W3U'], C1, abs_tol=0.5)

            if phase1 is True:
                print("R Phase Condition : ", Fore.GREEN + "GOOD")
            else:
                print("R Phase Condition : ", Fore.RED + "POOR")
            if phase2 is True:
                print("B Phase Condition : ", Fore.GREEN + "GOOD")
            else:
                print("B Phase Condition : ", Fore.RED + "POOR")
            if phase3 is True:
                print("Y Phase Condition : ", Fore.GREEN + "GOOD")
            else:
                print("Y Phase Condition : ", Fore.RED + "POOR")
            print("\t")
            if (phase1 and phase2 and phase3) is False:
                print("Balance Test : ", Back.RED + "FAILED")
                print("Suggestion : Transformer Cannot Processed")
            else:
                print("Balance Test : ", Back.GREEN + "PASSED")
                print("Result : All Phase Conditions are Good enough")

            if phase1 is False:
                print(Back.CYAN + "R Phase Need Improvement")
            if phase2 is False:
                print(Back.CYAN + "Y Phase Need Improvement")
            if phase3 is False:
                print(Back.CYAN + "B Phase Need Improvement")
            print("\t")
            print(Back.BLUE + Fore.BLACK + "Phase Balance Test Condition Verified & Report Generated")
        except:
            print("Invalid File input, unable to read json file")


    def bdv_test():
        print("File Name entered :", sys.argv[2])
        try:
            with open(sys.argv[2], 'r') as f:
                data = json.load(f)
            with open(sys.argv[2], 'w') as f:
                json.dump(data, f)

            jsonData = data["bdv"]
            for x in jsonData:
                keys = x.keys()
                values = x.values()

            print(Back.WHITE + Fore.BLACK + "OIL BDV Test Report")
            print("\t")
            print("Test Reading Values in KV")

            for i in values:
                print(i)

            print("Total Sum of the Value is ", sum(values), "for", len(values), "readings")
            Average = sum(values) / len(values)
            print("Average Value : ", round(Average, 2), "KV")

            if Average > 60:
                print("Oil Condition : ", Fore.GREEN + "GOOD")
            elif (Average > 50 and Average <= 60):
                print("Oil Condition : ", Fore.YELLOW + "FAIR")
            else:
                print("Oil Condition : ", Fore.RED + "POOR")
                print(Back.BLUE + "Suggestion : Need Improvement")
            print("\t")
            print(Back.BLUE + Fore.BLACK + "Oil BDV Test Condition Verified & Report Generated")
        except:
            print("Invalid File input, unable to read json file")


    main()
except:
    print("Invalid syntax to execute file")
    print("Syntax : python <python file name.py>  <testname>  <additional filename with extensible>")
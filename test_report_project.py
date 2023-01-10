import json
import math
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import matplotlib.pyplot as plt
def ir_test():
    print("File Name entered :", sys.argv[1])
    try:
        with open(sys.argv[1], 'r') as f:
            data = json.load(f)
        data['1_Connections']
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
        print("1 Min Value : ", data['2_OneMinValue'], " ", "10 Min Value : ", data['2_TenMinValue'])
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
        print("1 Min Value : ", data['3_OneMinValue'], " ", "10 Min Value : ", data['3_TenMinValue'])
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
        connections = ['HV-LV', 'HV-E', 'LV-E']
        PIValue = [Pivalue1, Pivalue2, Pivalue3]
        colors = ['green', 'blue', 'purple']
        plt.bar(connections, PIValue, color=colors)
        plt.title('IR Test Output', fontsize=14)
        plt.xlabel('Connections', fontsize=14)
        plt.ylabel('PI Value', fontsize=14)
        plt.show()
    except:
        print("\t")
        print("Invalid File input, unable to read json file")
def balance_test():
    print("File Name entered :", sys.argv[1])
    try:
        with open(sys.argv[1], 'r') as f:
            data = json.load(f)
        data['1U1V']
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
        connections = ['U1', 'U2', 'V1', 'V2', 'W1', 'W2']
        PhaseValue = [data['1U1V'], A1, data['2V2W'], B1, data['3W3U'], C1]
        colors = ['green', 'green', 'blue', 'blue', 'purple', 'purple']
        plt.bar(connections, PhaseValue, color=colors)
        plt.title('Phase Balance Test Output', fontsize=14)
        plt.xlabel('U V W Phases', fontsize=14)
        plt.ylabel('Phase Voltage', fontsize=14)
        plt.grid(True)
        plt.show()
    except:
        print("\t")
        print("Invalid File input, unable to read json file")
def bdv_test():
    print("File Name entered :", sys.argv[1])
    try:
        with open(sys.argv[1], 'r') as f:
            data = json.load(f)
        with open(sys.argv[1], 'w') as f:
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
        connections = ['BDV']
        PhaseValue = [Average]
        colors = ['blue']
        plt.bar(connections, PhaseValue, color=colors)
        plt.title('Oil BDV Test Output', fontsize=14)
        plt.xlabel('BDV Reading', fontsize=14)
        plt.ylabel('Average Voltage Value', fontsize=14)
        plt.grid(True)
        plt.show()
    except:
        print("\t")
        print("Invalid File input, unable to read json file")
def main():
    if (str(sys.argv[1]) == 'irtest.json'):
        ir_test()
        print("\t")
    elif (str(sys.argv[1]) == 'balancetest.json'):
        balance_test()
        print("\t")
    else:
        (str(sys.argv[1]) == 'bdvtest.json')
        bdv_test()
        print("\t")

if __name__ == "__main__":
    main()
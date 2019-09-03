import cv2
import numpy as np
import os
import csv
import urllib.request
import json
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

img = cv2.imread(file_path)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img)


kp = sorted(kp, key=lambda x: -x.response)[:1]
kp, dsc = sift.compute(img, kp)

dsc = dsc.flatten()
if dsc.size < 128:
    dsc = np.concatenate([dsc, np.zeros(128 - dsc.size)])

data = {
            "Inputs": {
                "input1":
                    [
                        {
                            'Vector 1': "{}".format(dsc[0]),
                            'Vector 2': "{}".format(dsc[1]),
                            'Vector 3': "{}".format(dsc[2]),
                            'Vector 4': "{}".format(dsc[3]),
                            'Vector 5': "{}".format(dsc[4]),
                            'Vector 6': "{}".format(dsc[5]),
                            'Vector 7': "{}".format(dsc[6]),
                            'Vector 8': "{}".format(dsc[7]),
                            'Vector 9': "{}".format(dsc[8]),
                            'Vector 10': "{}".format(dsc[9]),
                            'Vector 11': "{}".format(dsc[10]),
                            'Vector 12': "{}".format(dsc[11]),
                            'Vector 13': "{}".format(dsc[12]),
                            'Vector 14': "{}".format(dsc[13]),
                            'Vector 15': "{}".format(dsc[14]),
                            'Vector 16': "{}".format(dsc[15]),
                            'Vector 17': "{}".format(dsc[16]),
                            'Vector 18': "{}".format(dsc[17]),
                            'Vector 19': "{}".format(dsc[18]),
                            'Vector 20': "{}".format(dsc[19]),
                            'Vector 21': "{}".format(dsc[20]),
                            'Vector 22': "{}".format(dsc[21]),
                            'Vector 23': "{}".format(dsc[22]),
                            'Vector 24': "{}".format(dsc[23]),
                            'Vector 25': "{}".format(dsc[24]),
                            'Vector 26': "{}".format(dsc[25]),
                            'Vector 27': "{}".format(dsc[26]),
                            'Vector 28': "{}".format(dsc[27]),
                            'Vector 29': "{}".format(dsc[28]),
                            'Vector 30': "{}".format(dsc[29]),
                            'Vector 31': "{}".format(dsc[30]),
                            'Vector 32': "{}".format(dsc[31]),
                            'Vector 33': "{}".format(dsc[32]),
                            'Vector 34': "{}".format(dsc[33]),
                            'Vector 35': "{}".format(dsc[34]),
                            'Vector 36': "{}".format(dsc[35]),
                            'Vector 37': "{}".format(dsc[36]),
                            'Vector 38': "{}".format(dsc[37]),
                            'Vector 39': "{}".format(dsc[38]),
                            'Vector 40': "{}".format(dsc[39]),
                            'Vector 41': "{}".format(dsc[40]),
                            'Vector 42': "{}".format(dsc[41]),
                            'Vector 43': "{}".format(dsc[42]),
                            'Vector 44': "{}".format(dsc[43]),
                            'Vector 45': "{}".format(dsc[44]),
                            'Vector 46': "{}".format(dsc[45]),
                            'Vector 47': "{}".format(dsc[46]),
                            'Vector 48': "{}".format(dsc[47]),
                            'Vector 49': "{}".format(dsc[48]),
                            'Vector 50': "{}".format(dsc[49]),
                            'Vector 51': "{}".format(dsc[50]),
                            'Vector 52': "{}".format(dsc[51]),
                            'Vector 53': "{}".format(dsc[52]),
                            'Vector 54': "{}".format(dsc[53]),
                            'Vector 55': "{}".format(dsc[54]),
                            'Vector 56': "{}".format(dsc[55]),
                            'Vector 57': "{}".format(dsc[56]),
                            'Vector 58': "{}".format(dsc[57]),
                            'Vector 59': "{}".format(dsc[58]),
                            'Vector 60': "{}".format(dsc[59]),
                            'Vector 61': "{}".format(dsc[60]),
                            'Vector 62': "{}".format(dsc[61]),
                            'Vector 63': "{}".format(dsc[62]),
                            'Vector 64': "{}".format(dsc[63]),
                            'Vector 65': "{}".format(dsc[64]),
                            'Vector 66': "{}".format(dsc[65]),
                            'Vector 67': "{}".format(dsc[66]),
                            'Vector 68': "{}".format(dsc[67]),
                            'Vector 69': "{}".format(dsc[68]),
                            'Vector 70': "{}".format(dsc[69]),
                            'Vector 71': "{}".format(dsc[70]),
                            'Vector 72': "{}".format(dsc[71]),
                            'Vector 73': "{}".format(dsc[72]),
                            'Vector 74': "{}".format(dsc[73]),
                            'Vector 75': "{}".format(dsc[74]),
                            'Vector 76': "{}".format(dsc[75]),
                            'Vector 77': "{}".format(dsc[76]),
                            'Vector 78': "{}".format(dsc[77]),
                            'Vector 79': "{}".format(dsc[78]),
                            'Vector 80': "{}".format(dsc[79]),
                            'Vector 81': "{}".format(dsc[80]),
                            'Vector 82': "{}".format(dsc[81]),
                            'Vector 83': "{}".format(dsc[82]),
                            'Vector 84': "{}".format(dsc[83]),
                            'Vector 85': "{}".format(dsc[84]),
                            'Vector 86': "{}".format(dsc[85]),
                            'Vector 87': "{}".format(dsc[86]),
                            'Vector 88': "{}".format(dsc[87]),
                            'Vector 89': "{}".format(dsc[88]),
                            'Vector 90': "{}".format(dsc[89]),
                            'Vector 91': "{}".format(dsc[90]),
                            'Vector 92': "{}".format(dsc[91]),
                            'Vector 93': "{}".format(dsc[92]),
                            'Vector 94': "{}".format(dsc[93]),
                            'Vector 95': "{}".format(dsc[94]),
                            'Vector 96': "{}".format(dsc[95]),
                            'Vector 97': "{}".format(dsc[96]),
                            'Vector 98': "{}".format(dsc[97]),
                            'Vector 99': "{}".format(dsc[98]),
                            'Vector 100': "{}".format(dsc[99]),
                            'Vector 101': "{}".format(dsc[100]),
                            'Vector 102': "{}".format(dsc[101]),
                            'Vector 103': "{}".format(dsc[102]),
                            'Vector 104': "{}".format(dsc[103]),
                            'Vector 105': "{}".format(dsc[104]),
                            'Vector 106': "{}".format(dsc[105]),
                            'Vector 107': "{}".format(dsc[106]),
                            'Vector 108': "{}".format(dsc[107]),
                            'Vector 109': "{}".format(dsc[108]),
                            'Vector 110': "{}".format(dsc[109]),
                            'Vector 111': "{}".format(dsc[110]),
                            'Vector 112': "{}".format(dsc[111]),
                            'Vector 113': "{}".format(dsc[112]),
                            'Vector 114': "{}".format(dsc[113]),
                            'Vector 115': "{}".format(dsc[114]),
                            'Vector 116': "{}".format(dsc[115]),
                            'Vector 117': "{}".format(dsc[116]),
                            'Vector 118': "{}".format(dsc[117]),
                            'Vector 119': "{}".format(dsc[118]),
                            'Vector 120': "{}".format(dsc[119]),
                            'Vector 121': "{}".format(dsc[120]),
                            'Vector 122': "{}".format(dsc[121]),
                            'Vector 123': "{}".format(dsc[122]),
                            'Vector 124': "{}".format(dsc[123]),
                            'Vector 125': "{}".format(dsc[124]),
                            'Vector 126': "{}".format(dsc[125]),
                            'Vector 127': "{}".format(dsc[126]),
                            'Vector 128': "{}".format(dsc[127]),

                        }
                    ],
            },
            "GlobalParameters": {
            }
        }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/d1ba1d2c85a140fc8f7bdd5838f2fc65/services/d15e8a028a574235bec4bbff13407b28/execute?api-version=2.0&format=swagger'
api_key = 'UiLf7vNYyAO9dTZI+XXNjWflvSBcuOiiGENfdy6Z1lhXNt9uKBbaqkVE3k83ChqoUEtXJ4nrM2WsKdhIdlNg6g=='  # Replace this with the API key for the web service
headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)


except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))

input("press any key to exit")





import serial
import numpy as np
import pickle


model = pickle.load(open("rsf_model.sav", 'rb'))
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #depend on the communication method
ser.flush()
while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            data = line.split()
            data_arr = np.array(data)
            data_arr_float = np.asfarray(data_arr,float)
            y = np.expand_dims(data_arr_float, axis=0)
            y_pred=model.predict(y)
            if y_pred[0]==1:
                print ("The machine is failing")
            else:
                print("normal")
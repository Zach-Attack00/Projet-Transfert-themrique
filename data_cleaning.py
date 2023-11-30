import pandas as pd


def Concierge():
    #Fonction permettant de nettoyer le CSV pour avoir les valeurs plus efficacement
    empty_data = []
    df = pd.read_csv("data_brutes.csv")
    for headers in df.colums[:]:
        if headers != "DATE":
            data = df[headers]
            if headers != "Text":
                array = []
                for i in range(1, len(data)):
                    array.append(float(data[i].strip().replace(",", ".")))
                empty_data.append(array)
            if headers == "Text":
                ar = []
                for k in range(1, len(data)):
                    array_text.append(data[k])
                empty_data.insert(2, array_text)
        if headers == "DATE":
            time = df["DATE"]
            array_date = []
            for j in range(1, len(time)):
                array_date.append(time[j])
            empty_data.insert(0, array_date)
    vals = {n:empty_data[k] for n, k in enumerate(df.columns)}
    df.to_csv("data.csv", index=False)

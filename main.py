# importing lib's
import streamlit as st
import pandas as pd
import joblib
from var import *

# configuring page default's
st.set_page_config(page_title="Mobile Price Prediction", page_icon="fav.png")
st.title("Mobile Price Prediction")

# function to process input
def process_mobile_info(data):
    loaded_model = joblib.load("SPmodel.joblib")
    dft = pd.DataFrame(data)
    dft.columns = d2
    obj_columns = dft.select_dtypes(include="object").columns
    for col in obj_columns:
        if col in values:
            dft[col].fillna(values[col], inplace=True)
    # label encoder/ converts user input into encoded values
    label_encoders = joblib.load("bin.dat")
    # tranforms using label_encoder
    for i in range(21):
        try:
            dft[obj_columns[i]] = label_encoders[i].transform(dft[obj_columns[i]])
        except:
            dft[obj_columns[i]] = label_encoders[i].transform([values[obj_columns[i]]])
    return loaded_model.predict(dft)[0]


def main():
    st.title("Enter Mobile Details")
    # Taking Input's
    c1, c2 = st.columns(2)
    # Left column
    with c1:
        brand = st.selectbox("Enter the brand of the mobile:", brandvals)
        os = st.selectbox("Enter the operating system of the mobile:", osvals)
        pro = st.selectbox("Enter the processor type (e.g., octa-core):", pvals)
        promk = st.selectbox("Enter the processor make:", pmvals)
        ff = st.selectbox("Enter the form factor of the mobile:", ffvals)
        year = st.number_input(
            "Enter the release year:", min_value=0, step=1, value=2000
        )
        ram = st.number_input("Enter the RAM of the mobile in MB:", min_value=0, step=1)
        sto = st.number_input(
            "Enter the internal storage of the mobile:", min_value=0, step=1
        )
        h = st.number_input("Enter the height of themobile:")
        b = st.number_input("Enter the breadth of the mobile:")
        w = st.number_input("Enter the width of the mobile:")
        wt = st.number_input("Enter the weight of the mobile:", min_value=0, value=100)
        hp = st.selectbox("Does it have a headphone jack?:", ["Yes", "No"])
        wf = st.selectbox("Does it have WiFi?:", ["Yes", "No"])
        blu = st.selectbox("Does it have Bluetooth?:", ["Yes", "No"])
        ts = st.selectbox("Does it have touchscreen?:", ["Yes", "No"])
        acc = st.selectbox("Does it have an accelerometer?:", ["Yes", "No"])
        ps = st.selectbox("Does it have a proximity sensor?:", ["Yes", "No"])
    # right column
    with c2:
        est = st.selectbox(
            "Enter the type of expandable storage:",
            ["microSD", "Nano Memory Card", "SD card"],
        )
        esl = st.number_input("Enter the expandable storage:", min_value=0, step=1)
        g43 = st.selectbox("Enter the network of the mobile:", ["4G", "3G"])
        stype = st.selectbox(
            "Enter the SIM type of the mobile:", ["Nano-SIM", "Micro-SIM", "Regular"]
        )
        gscd = st.selectbox("Enter the GSM/CDMA type:", ["GSM", "GSM + CDMA", "CDMA"])
        bat = st.number_input(
            "Enter the battery of the mobile:", min_value=0, step=1, value=4000
        )
        res = st.number_input(
            "Enter the resolution of the mobile:", min_value=1080, step=1
        )
        rcc = st.number_input("Enter the number of rear cameras:", min_value=0, step=1)
        rc = st.number_input("Enter the pixels of the main camera:", min_value=0)
        fcc = st.number_input("Enter the number of front cameras:", min_value=0, step=1)
        fc = st.number_input("Enter the pixels of the front camera:", min_value=0)
        sc = st.number_input("Enter the screen size of the mobile:")
        als = st.selectbox("Does it have a light sensor?:", ["Yes", "No"])
        es = st.selectbox("Does it have expandable storage?:", ["Yes", "No"])
        rf = st.selectbox("Does it have a rear flash?:", ["Yes", "No"])
        gyro = st.selectbox("Does it have a gyroscope?:", ["Yes", "No"])
        gps = st.selectbox("Does it have GPS?:", ["Yes", "No"])
        cm = st.selectbox("Does it have a compass?:", ["Yes", "No"])
    # making into list so we can pass it into function
    data = [
        [
            brand,
            rcc,
            rc,
            fcc,
            fc,
            year,
            sc,
            os,
            sto,
            wf,
            blu,
            bat,
            ram,
            ts,
            ff,
            acc,
            ps,
            als,
            es,
            rf,
            pro,
            gps,
            res,
            promk,
            h,
            b,
            w,
            wt,
            cm,
            hp,
            gyro,
            est,
            g43,
            st,
            gscd,
            esl,
        ]
    ]
    # submit button logic
    if st.button("Submit"):
        result = process_mobile_info(data)
        st.success(f"The predicted price of the mobile is {result}")


if __name__ == "__main__":
    main()

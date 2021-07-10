from os import lchown
import pickle
from altair.vegalite.v4.schema.core import Day, Month
import streamlit as st
import datetime

pickle_in = open("msft_poly1.pkl","rb")
model1=pickle.load(pickle_in)


def predict(open_ip,high_ip,low_ip,day_ip,month_ip,year_ip,time_hr_ip,time_min_ip):
        our_pred = model1.predict([[open_ip,high_ip,low_ip,day_ip,month_ip,year_ip,time_hr_ip,time_min_ip]])
        print(our_pred)
        return our_pred



def main():
        st.title("Stock Price Prediction!")
        html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">StockPrice Prediction </h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        st.title("Enter Value's")
        open_ip = st.text_input("OPEN","")
        high_ip = st.text_input("HIGH","") 
        low_ip = st.text_input("LOW", "")
        calendar_ip = st.date_input('DATE')
        day_ip =  calendar_ip.day
        month_ip = calendar_ip.month
        year_ip = calendar_ip.year
        time_hr_ip = st.text_input("TIME IN HR","")
        time_min_ip = st.slider("MINUTES", 1, 59)
        result = ""
        if st.button("Predict"):
                 result = predict(open_ip,high_ip,low_ip,day_ip,month_ip,year_ip,time_hr_ip,time_min_ip)
                 print()
                 st.success('The output is {}'.format(result))



if __name__=='__main__':
            main()
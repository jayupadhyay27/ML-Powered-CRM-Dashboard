import streamlit as st
import joblib
model = joblib.load("models/Lead_Conversion_model.pkl")
customer_model = joblib.load("models/customer_segmentation_model.pkl")
sales_model= joblib.load("models/sales_forecasting_model.pkl")
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="ML Powered CRM",
    page_icon="🚀",
    layout="wide"
    
)

st.title("🚀 ML Powered CRM Dashboard")

#Sidebarr code

menu=st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Lead Conversion Prediction",
        "Sales Forecasting",
        "Customer Segmentation"
      ]
    )

if menu== "Home":

    st.markdown("""
       <div style="
       width:85%;         
       padding:20px;
       border-radius:10px;
       background-color:#1e293b;
       color:white;
       font-size:18px;">
       AI-powered CRM platform for Lead Conversion Prediction,
       Sales Forecasting and Customer Segmentation.
       </div>
       """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Project overview")

    col1,col2,col3,=st.columns(3)
    with col1:
         st.metric(
              label="Modules",
              value="3"
         )
    with col2:
         st.metric(
              label="ML Models",
              value="3"
         )
    with col3:
         st.metric(
              label="Dataset",
              value="CRM"  
         ) 

    st.markdown("---")            
    st.subheader("Available Modules")

    col1,col2,col3=st.columns(3)

    with col1:
         st.warning("Lead Conversion Prediction")
    with col2:
         st.success("Sales Forecasting")
    with col3:
         st.info("Customer Segmentation")

    st.markdown("---")
    st.subheader("Technology stack")

    st.markdown("""
    - Python

    -  Streamlit

    -  Pandas

    -  Scikit-Learn

    -  Plotly
     """)
    
    st.markdown("---")

    st.caption(
    "Developed by Jay | ML Powered CRM Dashboard | 2026"
)

 #Lead conversion prediction 

elif menu=="Lead Conversion Prediction":

    st.header("Lead Conversion Prediction")

    age = st.number_input("Enter Age")
    income = st.number_input("Enter Income")
    Calls_made = st.number_input("Enter Calls_made")
    Website_visitss = st.number_input("Enter Website_visitss")

    st.write("Age:", age)
    st.write("Income:", income)
    st.write("Calls_made:", Calls_made)
    st.write("Website_visitss:", Website_visitss)

    if st.button("Predict"):

        prediction = model.predict(
            [[age, income, Calls_made, Website_visitss]]
        )

        if prediction[0] == 1:
            st.success("✅ Lead likely to convert")
            st.info("Recommendation: Assign sales representative immediately")
            
        else:
            st.error("❌ Lead not likely to convert")
            st.info("Recommendation: Increase engagement through follow-ups")

        st.markdown("---")
        st.subheader("Lead summary")

        col1,col2 =st.columns(2)

        with col1:
             st.metric(
                  label="income",
                  value=f"₹{income:,.0f}"
             )    
         
        with col2:
             st.metric(
                  label="Status",
                  value="Likely" if prediction[0] == 1 else "Not Likely"
             )  
        st.markdown("---")
        st.subheader("Lead KPIs")

        col1,col2,col3,col4=st.columns(4)
             
        with col1:
             st.metric(
                  label="Age",
                  value=age
             )

        with col2:
             st.metric(
                  label="income",
                  value=income
                  )
                      
        with col3:
             st.metric(
                  label="Calls_made",
                  value=Calls_made
                  )         

        with col4:
             st.metric(
                  label="Website_visitss",
                  value=Website_visitss
                  )
        st.markdown("---")     

        st.subheader("Lead insights")

        lead_data=pd.DataFrame({
             "Feature":["Age","income(K)","Calls","Website visitss"],
                  "Value":[age,income/1000,Calls_made,Website_visitss]
             })

        fig=px.bar(
                  lead_data,
                  x="Feature",
                  y="Value",
                  title="Lead factors"
             )

        st.plotly_chart(fig, use_container_width=True)     

elif menu=="Sales Forecasting":
        st.header("Sales Forecasting")

        income=st.number_input("Enter income")
        Calls_made=st.number_input("Enter Calls_made")
        Website_visitss=st.number_input("Enter Website_visitss")

        st.write("income", income)
        st.write("Calls_made", Calls_made)
        st.write("Website_visitss", Website_visitss)

        if st.button("Forecast sales"):
             
             prediction= sales_model.predict(
                  [[income,Calls_made,Website_visitss]]
             )


             st.success(
                  f"💰 Predicted Deal Size: ₹{prediction[0]:,.2f}"
             )

             if prediction[0]<80000:
                  st.error("🔴 Low revenue opportunity")
                  st.info("💡Recommendation: Increase marketing efforts and Customer outreach ")

             elif prediction[0]<150000:
                  st.warning("🟡Medium revenue opportunity") 
                  st.info("💡Recommendation: Focus on follow ups to increase conversion")

             else:
                  st.success("🟢High revenue opportunity") 
                  st.info("💡Recommendation: High value opportunity..Prioritize this lead immediately")

             st.markdown("---")
             st.subheader("Forecast summary")
             col1,col2=st.columns(2)

             with col1:
                  st.metric(
                       label="Prediction revenue",
                       value=f"₹{prediction[0]:,.0f}"
                  )           
             
             with col2:
                  st.metric(
                       label="status",
                       value="High" if prediction[0]>=150000 else
                             "Medium" if prediction[0]>=80000 else
                             "Low"
                  )

             st.markdown("---")
             st.subheader("Business KPIs")
             k1,k2,k3=st.columns(3)

             with k1:
                       st.metric(
                            "Revenue",
                            f"₹{prediction[0]:,.0f}"
                       )

             with k2:
                       st.metric(
                            "Calls",
                            Calls_made
                       )

             with k3:
                       st.metric(
                            "Website_visitss",
                            Website_visitss
                       )     

             import pandas as pd
             chart_data=pd.DataFrame({
                       "Metric":["income","Calls_made","Website_visitss"],
                       "Value":[
                            income,
                            Calls_made*5000,
                            Website_visitss*1000
                       ]
                  })
             
             st.markdown("---")
             st.subheader("Revenue drivers")

             st.bar_chart(
                       chart_data.set_index("Metric")
                  )
             st.markdown("---")
             st.subheader("Action plan")

             if prediction[0] < 80000:

                     st.error("📢 Low Revenue Lead")

                     st.write("• Increase marketing campaigns")
                     st.write("• Improve website engagement")
                     st.write("• Send promotional emails")

             elif prediction[0] < 150000:

                     st.warning("📞 Medium Revenue Lead")

                     st.write("• Schedule follow-up calls")
                     st.write("• Offer discounts")
                     st.write("• Build stronger relationship")

             else:

                     st.success("🚀 High Revenue Lead")

                     st.write("• Prioritize immediately")
                     st.write("• Assign senior sales executive")
                     st.write("• Prepare premium proposal")
                  



            
elif menu=="Customer Segmentation": 
        st.header("Customer Segmentation") 

        income=st.number_input("Enter income")
        Calls_made=st.number_input("Enter Calls_made")
        Website_visitss=st.number_input("Enter Website_visitss")

        st.write("Income",income)
        st.write("Calls_made",Calls_made)
        st.write("Website_visitss",Website_visitss)

        if st.button("predict segment"):
            segment=customer_model.predict(
         
            [[income,Calls_made,Website_visitss]]
    )

            st.write("segment:",segment[0])

            if  segment[0]==0:
                 st.success("🟢 High Value Customer")#success green box ke liye
                 st.info("Recommendation:  Offer premium services and prioritize retention")

            elif segment[0]==2:
                 st.warning("🟡 Medium Value Customer")#warning yellow box ke liye
                 st.info("Recommendation: Increase engagement through targetd campaigns")

            else:
                 st.error("🔴 Low Value Customer")#error red box ke liye
                 st.info("Recommendation:Run promotional offers and re-engagement campaigns")

            st.markdown("---")
            st.subheader("Customer summary")
            col1,col2=st.columns(2)

            with col1:
                 st.metric(
                    label="income",
                    value=f"₹{income:,.0f}"
                 )
            with col2:
                 st.metric(
                    label="Status",
                    value="High" if segment[0]==0 else
                          "medium"if segment[0]==2 else
                          "Low"
                 )  

            st.markdown("---")
            st.subheader("Business KPIs")

            k1,k2,k3=st.columns(3)

            with k1:
                      st.metric(
                           label="income",
                           value=f"₹{income:,.0f}"
                      )

            with k2:
                      st.metric(
                           label="Calls",
                           value=Calls_made

                      )

            with k3:
                      st.metric(
                           label="Website visitss",
                           value=Website_visitss
                      )  

            st.markdown("---")
            st.subheader("Segment Distribution")  

            segment_data=pd.DataFrame({
                      "segment":["High value","Medium value","Low value"],
                      "count":[45,35,20]
                 })

            fig=px.pie(
                      segment_data,
                      names="segment",
                      values="count",
                      title="Customer segment distribution"
                 )

            st.plotly_chart(fig,use_container_width=True)
            
            st.markdown("---")     
            st.subheader("Customer action plan")

            if segment[0]==0:
                       st.success("Retain customer with loyalty rewards")
                       st.success("Offer premium services")
                       st.success(" Prioritize customer support")
            elif segment[0]==2:
                      st.warning("Increase engagement")
                      st.warning("Personalized campaigns")
                      st.warning(" Upsell opportunities")
            else:
                      st.error("Re-engagement campaign")
                      st.error("Promotional discounts")
                      st.error("Increase communication frequency")        



  

    
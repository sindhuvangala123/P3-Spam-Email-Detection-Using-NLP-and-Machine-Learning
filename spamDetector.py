import streamlit as st
import pickle

model = pickle.load(open('spam123.pkl', 'rb')) 
cv = pickle.load(open('vec123.pkl', 'rb'))

def main():
    st.title("Email Spam Classification Application")
    st.write("This is a Machine Learning application to classify email as spam or ham")
    st.subheader("Classification")
    
    # Get user input
    user_input = st.text_area("Enter an email to classify", height=150)
    
    if st.button("Classify"):
        if user_input:
            data = [user_input]
            print(data)
            vec = cv.transform(data).toarray()  # Transform the input into vector form
            result = model.predict(vec)  # Make prediction using the model
            if result[0] == 0:
                st.success("This is Not A Spam Email")
            else:
                st.error("This is a Spam Email")
        else:
            st.write("Please enter an email to classify.")

# Run the application
main()

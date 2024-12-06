import streamlit as st
import pickle
model=pickle.load(open('spam123.pkl','rb'))
cv=pickle.load(open('vec123.pk1','rb'))
def main():
    st.title("Email Spam Classification Application")
    st.write("This is a machine Learning application to classify email as spam or ham.")
    st.subheader("Classification")
    user_input=st.text_area("Enter an email to classify",height=150)
    if st.button("Classify"):
        if user_input:
            data=[user_input]
            vec = cv.transform(data).toarray()  
            result = model.predict(vec) 
            vec=cv.transform(data).toarray()
            if result[0]==0:
                st.success("This is Not a Spam Email")
            else:
                st.error("This is A Spam Email")
        else:
            st.write("Please enter an email to clasify.")
if __name__ == "__main__":
    main()           
 

import streamlit as st
import pickle 
lin_model =pickle.load(open('lin_model.pkl', 'rb'))
log_model =pickle.load(open('log_model.pkl', 'rb'))
svm =pickle.load(open('svc_model.pkl', 'rb'))
# st.slider('Take your Input here', 0.0, 10.0)
def classify(num):
    if num<0.5:
        return 'Satosa'
    elif num<1.5:
        return 'Versicolor'
    else:
        return 'Verginica'
def main():
    st.title('Classification of Flowers')
    activities=['Linear Regression' , 'Logistic Regression', 'SVM']
    options=st.sidebar.selectbox('Which Model you want to select', activities)
    st.subheader(options)
    sl = st.slider('select Sepal Length ', 0.0, 10.0)
    sw = st.slider('select Sepal Width ', 0.0, 10.0)
    pl = st.slider('select Petal Length ', 0.0, 10.0)
    pw = st.slider('select Petal Width ', 0.0, 10.0)
    input=[[sl,sw,pl,pw]]
    if st.button('classify'):
        if options=='Linear Regression':
            st.success(classify(lin_model.predict(input)))
        elif options=='Logistic Regression':
             st.success(classify(log_model.predict(input)))
        else:
             st.success(classify(svm.predict(input)))  
if __name__ == '__main__':  
    main()                  
                
            
        
        

    
   
  
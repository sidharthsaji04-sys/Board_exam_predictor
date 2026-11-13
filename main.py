import streamlit as st
import sqlite3 as sql
import time as t

connect=sql.connect('user.db')
cursor=connect.cursor()

class Login:
    def signup(self):
        
        cursor.execute('CREATE TABLE IF NOT EXISTS user_data(name text,std integer,id text)')
        st.header('Hi, welcome')
        st.subheader('Sign up by entering your data')
        with st.form(key='sample'):
          name=st.text_input('Enter your name: ')
          std=st.number_input('Enter your standard: ',min_value=11,max_value=12)
          id=st.text_input("create a id: ",help='id must be less than 4 charcters',max_chars=4)
          st.caption('id must be less than 4 charcters')
          submit_button=st.form_submit_button(label='Submit')
          if submit_button:
             cursor.execute("SELECT 1 FROM user_data WHERE id=?",(id,))
             checker=cursor.fetchone()
             if checker:
                st.warning('id already exists. Try another')
             if not name:
                st.warning("Fill the name column")
             if not std:
                st.warning('Fill the standard column')
             else:
                cursor.execute("INSERT INTO user_data VALUES(?,?,?)",(name,std,id))
                connect.commit()
                st.warning('verifying.......🔍')
                t.sleep(2)
                st.session_state.page='home'
                st.rerun()
       
           
    def home(self):
       st.title('BOARD EXAM SCORE PREDICTOR📚')
       st.caption("Your success begins here")
       st.subheader('Welcome!!!')
       with st.form(key='sample'):
        id=st.text_input('Enter your id: ',max_chars=4)
        submit_button=st.form_submit_button(label='Submit')
        if submit_button:
              cursor.execute('SELECT 1 FROM user_data WHERE id=?',(id,))
              result=cursor.fetchone()
              if result:
                 st.warning('verifying.......🔍')
                 t.sleep(2)
                 st.session_state.page='home'
                 st.rerun()
              else:
                 st.warning('Wrong id. Check again')
       st.subheader('Are you New user, sign up below👇')
       if st.button('Sign up'):
          st.session_state.page='signup'
          st.rerun()

l=Login()

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page=='home':
      l.home()

elif st.session_state.page=='signup':
   l.signup()


#The login and sign up section is fine. Now build the main stuffs, gooooooooo
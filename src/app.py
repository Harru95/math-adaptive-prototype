import streamlit as st
import time
from puzzle_generator import puzzle_generator
from adaptive_engine import adaptive_engine
from Performance_tracker import Performance_Tracker, progress_summarize
st.title("Adaptive Learnig Prototype")
#Initializing
if "name" not in st.session_state:
    st.session_state.name=""
if "level" not in st.session_state:
    st.session_state.level="Medium"
if "attempts" not in st.session_state:
    st.session_state.attempts=[]
if "path" not in st.session_state:
    st.session_state.path=[]
if "question" not in st.session_state:
    st.session_state.question,st.session_state.res=puzzle_generator("Medium")
if "start_time" not in st.session_state:
    st.session_state.start_time=time.time()
if "finished" not in st.session_state:
    st.session_state.finished=False
if "total_q" not in st.session_state:
    st.session_state.total_q=None

name_input=st.text_input("Enter your name:",value=st.session_state.name)#Taking name as input
if name_input=="": st.stop()
st.session_state.name=name_input 
st.session_state.total_q=st.number_input("How many questions would you like to attempt?",min_value=1,max_value=50,value=10,step=1)#taking total questions user wants to attempt
if st.session_state.total_q is None: st.stop()

if len(st.session_state.attempts)>=st.session_state.total_q: #if attempts cross total questions then finish
    st.session_state.finished=True

if st.session_state.finished:#display summary if finished
    summary=progress_summarize(st.session_state.name,
        st.session_state.total_q,
        st.session_state.attempts,
        st.session_state.path,
        st.session_state.level)
    st.subheader("Session summary/report")
    st.write(summary)
    st.stop()

st.write(f"Current Difficulty: **{st.session_state.level}**")
st.write(f"### {st.session_state.question}")

curr_ans=st.text_input("Your answer:") #Answer is taken as input

if st.button("Submit"): #Submit button for each answer submisstion is defined
    try:
        curr_ans=float(curr_ans)
        correct=abs(curr_ans-st.session_state.res)<0.001
    except:
        correct=False

    end_time=time.time()
    #performance is analysed for increasing or decreasing the difficulty otherwise stays same,and then puzzle generator is called to generate new question.
    Performance_Tracker(st.session_state.attempts,correct,end_time-st.session_state.start_time)
    st.session_state.path.append(st.session_state.level)
    st.write("Correct!" if correct else f"Incorrect. Answer was: {st.session_state.res}")

    st.session_state.level=adaptive_engine(st.session_state.level,st.session_state.attempts)
    st.session_state.question,st.session_state.res=puzzle_generator(st.session_state.level)
    st.session_state.start_time=time.time()

    st.rerun()

import streamlit as st
import time

def check(passw):
    countspsimb = 0
    countnumb = 0
    countupen = 0
    countlowen = 0
    countupru = 0
    countlowru = 0
    for simbol in passw:
        if simbol in '!@#$%^&*()_-+={}[]"/\|><~:;':
            countspsimb += 1
        if simbol in '1234567890':
            countnumb += 1
        if simbol in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            countupen += 1
        if simbol in 'qwertyuiopasdfghjklzxcvbnm':
            countlowen += 1
        if simbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            countupru += 1
        if simbol in 'йцукенгшщзхъфывапролджэячсмитьбю':
            countlowru += 1
    if len(passw) < 10:
        st.markdown("<h1 style='text-align: center; color: pink;'>Too FEW numbers, bro((</h1>", unsafe_allow_html=True)
    elif len(passw) > 50:
        st.markdown("<h1 style='text-align: center; color: pink;'>Too MANY numbers, bro>(((9</h1>", unsafe_allow_html=True)
    elif '1' in passw:
        st.markdown("<h1 style='text-align: center; color: pink;'>Sooooooo basiiic, add other numbs</h1>", unsafe_allow_html=True)
    elif time.strftime("%B") not in passw:
        st.markdown("<h1 style='text-align: center; color: pink;'>Idk, try add month at the moment</h1>", unsafe_allow_html=True)
    elif '999' not in passw:
        st.markdown("<h1 style='text-align: center; color: pink;'>U DON`T HAVE 999 IN UR PASSWORD?? HOW SOOOO??(add it, pls)</h1>", unsafe_allow_html=True)
    elif countspsimb < 5:
        st.markdown("<h1 style='text-align: center; color: pink;'>U don` GET IT, bro, add MORE special simbols>((</h1>", unsafe_allow_html=True)
    elif countupru > 0 or countlowru > 0:
        st.markdown("<h1 style='text-align: center; color: pink;'>What, do u think u`r the smartest ONE HERE? Clean it up. Remove Russian language.</h1>", unsafe_allow_html=True)
    elif 'smwm' not in passw and 'SMWM' not in passw:
        st.markdown("<h1 style='text-align: center; color: pink;'>Yeah, it's a captcha, come on, attack</h1>",
                    unsafe_allow_html=True)
        st.image("Captcha.jpg")
    else:
        st.markdown("<h1 style='text-align: center; color: pink;'>Cool! U got it!</h1>", unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align: center; color: pink;'>WOW!1 U`r sOOOOOOOOOOOOOOOOOOOOOOOOOOO c000000000000000000l!!!1</h1>",
            unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: pink;'>PapapewaGemabodi, THIS IS A PASSWORD GAME!!!111</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: pink;'>Try to pass if u have enough nerves</h1>", unsafe_allow_html=True)

passw = st.text_input('Enter password, bro', max_chars=100)
check(passw)
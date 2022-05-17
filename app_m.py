# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:07:50 2022

@author: A2128383
"""
import os
import moviepy.editor as mp
import speech_recognition
import streamlit as st

def transcribe_file(fp, lang='日本語'):
    lang_code = {'英語': 'en-US', '日本語': 'ja-JP'}
    root, ext = os.path.splitext(fp)
    if ext != ".wav":
        out_file = str(root) + '.wav'
        clip = mp.VideoFileClip(fp)
        clip.audio.write_audiofile(out_file)
        clip.close()
    else:
        out_file = fp

    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(out_file) as source:
        audio = r.record(source)
    st.write(r.recognize_google(audio, language=lang_code[lang]))
    #print(r.recognize_google(audio, language='ja-JP'))

st.title('文字起こしアプリ')

upload_file = st.file_uploader('ファイルのアップロード', type=['mp3','mp4','wav','acc','m4a','wma'])
if upload_file is not None:
    content = upload_file.read()
    name = upload_file.name
    fp = 'Desktop/' + name
    st.subheader('ファイル詳細')
    file_details = {'filename':upload_file.name, 'filetype':
                    upload_file.type, 'filesize':upload_file.size}
    st.write(file_details)
    st.subheader('音声の再生')
    st.audio(content)
    st.subheader('言語選択')
    option = st.selectbox('言語を選択してください', {'日本語','英語'})
    st.write('選択中の言語：', option)
    st.subheader('文字起こし')
    if st.button('開始'):
        comment = st.empty()
        comment.write('文字起こしを開始します')
        transcribe_file(fp, lang=option)
        comment.write('完了しました')
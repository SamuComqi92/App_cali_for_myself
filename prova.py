#Importing the library
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import json

#Configurazione pagina e font size
st.markdown(f"""<style>.reportview-container .main .block-container{{padding-right: 10rem;padding-left: 10rem;}}</style>""",unsafe_allow_html=True,)
st.markdown("""<style> .big-font {font-size:50px !important;}</style>""", unsafe_allow_html=True)
st.markdown("""<style> .big-fonte {font-size:20px !important;}</style>""", unsafe_allow_html=True)
st.markdown("""<style> .big-fonte2 {font-size:35px !important;}</style>""", unsafe_allow_html=True)
st.markdown('<p class="big-font">CALISTHENICS TRAINING</p>', unsafe_allow_html=True)
st.markdown('<p class="big-fonte">Samuele Campitiello</p>', unsafe_allow_html=True)

#Array vari ed eventuali
Giorni_allenamento =  ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì','Sabato','Domenica']
Numero_esercizi = ['','1','2','3','4','5','6','7','8','9','10']
Esercizi_vari = ['','OAP: MAX rom','OAP: australian','PLANCHE: Isometria','PLANCHE: Isometria (verde)','PLANCHE: Isometria (giallo)','PLANCHE: Pushup','PLANCHE: HSPU','PLANCHE: Bent-arm','FRONT: Mezzi raises','FRONT: Ice_cream','FRONT: Isometria','FRONT: Pullup','BACK_LEVER: Pullup','BACK_LEVER: Pullup (+ iso)']

st.write(Esercizi_vari.sort())
def upload_last_session() :
    #Read last session json file
    f = open("settings.json")
    aa = json.load(f)

    if len(aa)==0:
        return
    else :
        #Applico i vari settings
        def upload_json_settings(file):
            for k in file.keys():
                st.session_state[k] = file[k]
            return

        #Pulsante last session
        button_apply_settings = st.button(label="Carica ultima sessione salvata",
                                            on_click = upload_json_settings,
                                            args=(aa,),
                                            help="Click to Apply the Settings of the Uploaded file.\\\n"
                                                    "Please start by uploading a Settings File below")


#Container per mettere tutti i parametri/settings
container_upload_settings_data = st.container()

#Giorni dell'allenamento
giorni = st.multiselect(
    "Giorni dell'allenamento",
    Giorni_allenamento,
    key=1)        

primo_giorno = st.selectbox(
    'Primo giorno di allenamento',
    giorni,
    key=100)

flag_step = 0
if giorni :
    a = np.array(giorni)
    position = np.where(a == primo_giorno)[0][0]
    part1 = a[position:]
    part2 = a[:position]
    Giorni_ordinati = np.concatenate([part1,part2],axis=0)
    flag_step = 1


if flag_step == 1 :
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("..................................................................................................")
    st.markdown('<p class="big-fonte2">Esercizi</p>', unsafe_allow_html=True)
    st.write("Seleziona il numero di esercizi, gli esercizi (in ordine), la propedeutica, il numero di serie e ripetizioni, e le pause")
    if len(Giorni_ordinati)>0 :
        k=0
        for i in Giorni_ordinati :
            if np.where(Giorni_ordinati == i)[0][0]>0 :
                st.text("")
                st.text("")
                st.text("")
            st.write(i)
            k = k+1
            N_esercizi = st.selectbox(
                "Numero di esercizi",
                Numero_esercizi,
                key = k+1)
            if N_esercizi != '' :
                for j in range(int(N_esercizi)) :
                    left_column, center_column1, center_column2, center_column3, center_column4, right_column = st.columns([2,2,1,1,1,1])
                    with left_column :
                        Esercizi = st.selectbox(
                        'Esercizi in ordine',
                        ['','OAP: MAX rom','OAP: australian','PLANCHE: Isometria','PLANCHE: Isometria (verde)','PLANCHE: Isometria (giallo)','PLANCHE: Pushup','PLANCHE: HSPU','PLANCHE: Bent-arm','FRONT: Mezzi raises','FRONT: Ice_cream','FRONT: Isometria','FRONT: Pullup','BACK_LEVER: Pullup','BACK_LEVER: Pullup (+ iso)'],
                        key=k+100)
                    with center_column1 :
                        Propedeutica = st.selectbox(
                        'Seleziona la propedeutica',
                        ['','Libero (OAP)', 'Pancia al muro (HSPU)', 'Tuck','Adv tuck', 'Adv Adv tuck','One leg', 'Adv One leg', 'Adv Adv One leg', 'HL one leg', 'HL','Straddle','Full'],
                        key=k+101)
                    with center_column2 :
                        Serie = st.selectbox(
                        'Serie',
                        ['','1','2','3','4','5','6','7','8','9','10'],
                        key=k+102)
                    with center_column3 :
                        Reps = st.selectbox(
                        'Reps',
                        ['','1','2','3','4','5','6','7','8','9','10'],
                        key=k+103)
                    with center_column4 :
                        Iso = st.selectbox(
                        'Iso',
                        ['','1"','2"','3"','4"','5"','6"','7"','8"','9"','10"'],
                        key=k+104)
                    with right_column :
                        Pausa = st.selectbox(
                        'Pausa/EMOM',
                        ['','1:00','1:30','1:45','2:00','2:30','2:45','3:00'],
                        key=k+105)

                    globals()[f"Allenamento_{i}_{j}"] = [i,N_esercizi, Esercizi, Propedeutica, Serie, Reps, Iso, Pausa]
                    k = k+106  


        
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("..................................................................................................")
    st.markdown('<p class="big-fonte2">Scheda</p>', unsafe_allow_html=True)

    m = 200
    if f"Allenamento_{primo_giorno}_{0}" in globals():
        exec(f"data_final = pd.DataFrame(np.array(Allenamento_{primo_giorno}_{0}).reshape(1,8), columns=['Giorno','N_esercizio','Esercizio','Propedeutica','Serie','Reps','Isometria','Pausa'])")
        for i in Giorni_ordinati :
            for j in range(6) :
                if f"Allenamento_{i}_{j}" in globals():
                    exec(f"data_final = pd.concat([data_final, pd.DataFrame(np.array(Allenamento_{i}_{j}).reshape(1,8),columns=['Giorno','N_esercizio','Esercizio','Propedeutica','Serie','Reps','Isometria','Pausa'])],axis=0)")
                    flag_step = 2
    
    #Rimuovo colonna che non mi serve e taglio il primo record duplicato      
    if flag_step == 2 :
        data_final.drop("N_esercizio",axis=1,inplace=True)
    
    #Mostrami la scheda completa
    if st.checkbox('Mostrami la scheda completa') and flag_step == 2:  
        st.write(data_final.iloc[1:,:].reset_index().drop("index",axis=1))

    #Seleziona il giorno
    st.text("")
    st.text("")
    Giorno_training = st.selectbox(
        "Seleziona il giorno dell'allenamento",
        Giorni_ordinati,
        key = 1457)

    if Giorno_training and flag_step == 2 :
        meh = data_final.iloc[1:,:].reset_index().drop("index",axis=1)
        st.write(meh[meh.Giorno == Giorno_training])
        cc1, cc2, cc3, cc4 = st.columns([1,1,1,1])
        with cc1 :
            week1 = st.checkbox("Check week 1", key=546)
        with cc2 :
            week2 = st.checkbox("Check week 2", key=547)
        with cc3 :
            week3 = st.checkbox("Check week 3", key=548)
        with cc4 :
            week4 = st.checkbox("Check week 4", key=549)
        
# Run the download_upload_settings function
with container_upload_settings_data:
    upload_last_session()

#Per salvare i nuovi cambiamenti
st.text("")
st.text("")
settings_to_download = {k: v for k, v in st.session_state.items()
                            if "button" not in k and "file_uploader" not in k}
Butt_salvataggio = st.button(label="Salva cambiamenti!")

if Butt_salvataggio :
    data = json.dumps(settings_to_download)
    file = open("settings.json", "w")
    file.write(data)
    file.close()

import streamlit as st

st.set_page_config(layout="wide")

if "kumpulan" not in st.session_state:
    st.session_state['kumpulan']={'latar':True, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False, 'pertemuan3':False,'pertemuan4':False}

#==========================
def kover():
     tulisan_html='''
    <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/geometriAnaitikCover.html' style='width:100%; height:1000px'></iframe>
    '''
     st.components.v1.html(tulisan_html,height=1500)

def referensi():
    menu = st.tabs(['RPS','Referensi'])
    with menu[0]:
        tulisan_html='''
        <iframe src='https://drive.google.com/file/d/1mOktHZulRzk4DdDYdxxM04y9NYZ2zU2h/preview' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        tulisan_html='''
        <iframe src='https://drive.google.com/file/d/1i00K7aG5thO-ciLo5rEn-ck9wVQLboO5/preview' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)

def pertemuan_1():
    tulisan_html='''
    <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/pertemuan1.html' style='width:100%; height:1000px'></iframe>
    '''
    st.components.v1.html(tulisan_html,height=1500)

def pertemuan_2():
    menu = st.tabs(['Modul','pembahasan'])
    with menu[0]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/pertemuan2.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        pass

def pertemuan_3():
    menu = st.tabs(['Modul','pembahasan'])
    with menu[0]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/Luas.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        pass

def pertemuan_4():
    menu = st.tabs(['Modul','Latihan HOTS','Latihan Mandiri','pembahasan'])
    with menu[0]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/pertemuan4.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/latihan4.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[2]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/mandiri4.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1000)
        st.write("Pengumpulan Tugas (dalam bentuk PDF)")
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/jawabanGrad.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[3]:
        pass

#==========================

if st.session_state['kumpulan']['latar']:
    kover()

if st.session_state['kumpulan']['rps']:
    referensi()

if st.session_state['kumpulan']['pertemuan1']:
    pertemuan_1()

if st.session_state['kumpulan']['pertemuan2']:
    pertemuan_2()

if st.session_state['kumpulan']['pertemuan3']:
    pertemuan_3()

if st.session_state['kumpulan']['pertemuan4']:
    pertemuan_4()

#============================

if st.sidebar.button("Bagian Depan"):
    st.session_state['kumpulan']={'latar':True, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False}
    st.rerun()

if st.sidebar.button("RPS dan Referensi"):
    st.session_state['kumpulan']={'latar':False, 'rps':True, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False}
    st.rerun()

if st.sidebar.button("Koordinat dan Polar"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':True,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False}
    st.rerun()

if st.sidebar.button("Rumus Jarak"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':True,'pertemuan3':False,'pertemuan4':False}
    st.rerun()

if st.sidebar.button("Rumus Luas Segitiga dan Luas Segi Empat"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':True,'pertemuan4':False}
    st.rerun()
if st.sidebar.button("Persamaan Garis dan Gradien"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':True}
    st.rerun()

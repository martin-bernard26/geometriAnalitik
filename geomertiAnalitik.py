import streamlit as st
import requests

st.set_page_config(layout="wide")

if "kumpulan" not in st.session_state:
    st.session_state['kumpulan']={'latar':True, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False, 'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False}

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

def pertemuan_5():
    menu = st.tabs(['Modul','Latihan HOTS','Latihan Mandiri','pembahasan'])
    with menu[0]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/pertemuan5.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/hots5.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1000)
        st.title("Masukan Mahasiswa")
        st.write("Data ini merupakan forum diskusi untuk memecahkan soal HOTS")
        alamat_url = 'https://diskusimatematika-7a30c-default-rtdb.firebaseio.com/pgl2.json'
        with st.form(key="Masukan_Mahasiswa",clear_on_submit=True):
            nama = st.text_input("Masukan Nama Anda")
            nim = st.text_input("Masukan NIM Anda")
            jawaban = st.text_input("Masukan Jawaban Anda")
            kirimkan = st.form_submit_button("Kirimkan Jawaban Anda")
        if kirimkan:
            if nama.strip()=='' or nim.strip()=='' or jawaban.strip()=='':
                st.error('Anda belum memasukan data Anda dengan lengkap')
            else:
                kumpulan = {'nama':nama,
                            'nim':nim,
                            'jawaban':jawaban}
                try:
                    response = requests.post(alamat_url,json=kumpulan)
                    if response.status_code==200:
                        st.success('Data Anda berhasil masuk')
                    else:
                        st.error('Data Anda Gagal terkirim')
                except Exceptions as e:
                    st.error('Ada kesalahan di sistem Anda')
    with menu[2]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/soal6.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1000)
        st.title("Memasukan Tugas Mandiri")
        st.write("Halaman untuk mengumpulkan tugas pada pertemuan 5")
        alamat_url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeWguhfL0HLrrXfO6OBRbnU9qLwPoJOghzB0ti1cPAD48-WQA/formResponse'
        with st.form(key='Mengumpulkan_tugas'):
            nama = st.text_input("Masukan Nama Lengkap Anda")
            nim = st.text_input("Masukan NIM Anda yang sesuai")
            alamat = st.text_area("Masukan Link tugas Anda melalui Drive Anda")
            tombol = st.form_submit_button("Kirimkan tugas Anda")
        if tombol:
            if nama.strip()=='' or nim.strip()=='' or alamat.strip()=='':
                st.error('Pengisian identitas Anda belum lengkap')
            else:
                kumpulan = {'entry.182217510':nama,
                            'entry.226042863':nim,
                            'entry.1999444945':alamat
                            }
                try:
                    response = requests.post(alamat_url,data=kumpulan,timeout=10)
                    if response.status_code==200:
                        st.success('Tugas Anda sudah berhasil terkirim')
                    else:
                        st.error('Tugas Anda gagal terkirim')
                except Exceptions as e:
                    st.error('Ada kesalahan di sistem silahkan menghubungi')
                
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

if st.session_state['kumpulan']['pertemuan5']:
    pertemuan_5()

#============================

if st.sidebar.button("Bagian Depan"):
    st.session_state['kumpulan']={'latar':True, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False}
    st.rerun()

if st.sidebar.button("RPS dan Referensi"):
    st.session_state['kumpulan']={'latar':False, 'rps':True, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False}
    st.rerun()

if st.sidebar.button("Koordinat dan Polar"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':True,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False}
    st.rerun()

if st.sidebar.button("Rumus Jarak"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':True,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False}
    st.rerun()

if st.sidebar.button("Rumus Luas Segitiga dan Luas Segi Empat"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':True,'pertemuan4':False,
                                  'pertemuan5':False}
    st.rerun()
if st.sidebar.button("Persamaan Garis dan Gradien"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':True,
                                  'pertemuan5':False}
    st.rerun()
if st.sidebar.button("Persamaan Garis Lurus yang Sejajar dan Tegak Lurus"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':True}
    st.rerun()

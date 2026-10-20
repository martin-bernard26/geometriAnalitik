import streamlit as st
import requests
import base64


st.set_page_config(layout="wide")

if "kumpulan" not in st.session_state:
    st.session_state['kumpulan']={'latar':True, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False, 'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}

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

def pertemuan_6():
    menu = st.tabs(['Modul','Video','Latihan Penguatan Dasar','Latihan HOTS','Bantuan Geogebra'])
    with menu[0]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/bagiberkas.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[1]:
        st.title("Persamaan Garis Bagi Sudut")
        st.video("https://youtu.be/LxSssUvOlTw")
        st.title("Persamaan Garis Berkas Garis")
        st.video("https://youtu.be/9RDMe-ZGcgI")
    with menu[2]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/latihan6.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1000)
        st.title("Masukan Mahasiswa menggunakan LaTeX")
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/diskusi6.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1500)
    with menu[3]:
        tulisan_html='''
        <iframe src='https://martin-bernard26.github.io/GeometriAnalitic/hots6.html' style='width:100%; height:1000px'></iframe>
        '''
        st.components.v1.html(tulisan_html,height=1000)
        st.title("Pengumpulan Mahasiswa")
        st.write("Silahkan isi identitas dan pengumpulan tugas")
        alamat_GS = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSf6Yt4N9B3QKM1GkrD05H3hbka6aIFMB7UT5KTJIuKOxvEFoA/formResponse'
        with st.form(key='Masukan tugas persamaan garis bagi sudut dan berkas garis',clear_on_submit=True):
            nama = st.text_input('Masukan Nama Anda',key='nama1')
            nim = st.text_input('Masukan NIM Anda',key='nim1')
            masukan = st.text_input('Masukan link drive di sini',key='masukan1')
            tombol1 = st.form_submit_button("Kirimkan Tugas")
        if tombol1:
            if nama.strip()=='' and nim.strip()=='' and masukan.strip()=='':
                st.error("Pengisian data kurang lengkap")
            else:
                data1 = {"entry.1403593665":nama,
                         "entry.1764365330":nim,
                         "entry.911238631":masukan}
                try:
                    respon = requests.post(alamat_GS,data=data1,timeout=10)
                    if respon.status_code==200:
                        st.success("Data Anda sudah di simpan")
                    else:
                        st.error("Data Anda gagal di simpan")
                except Exception as e:
                    st.error(f"Ada kesalahan sistem: {e}")
    with menu[4]:
        st.title("Kirim Gambar GeoGebra ke Firebase Realtime Database")
        DB_URL = "https://diskusimatematika-7a30c-default-rtdb.firebaseio.com".rstrip("/")
        NODE = "gambar_geogebra1"   # nama "folder" di Realtime Database
        app_name = "classic"      # graphing / geometry / classic
        jumlah = 9                 # jumlah gambar terbaru yang ditampilkan di galeri
 
        st.write("📐 Kirim Hasil GeoGebra ke Firebase")
        HTML = """
<div style="font-family:sans-serif">
  <div id="ggb"></div>
  <div style="margin-top:10px;display:flex;gap:8px;align-items:center;flex-wrap:wrap">
    <input id="nama" placeholder="Nama / NIM" style="padding:8px;border:1px solid #ccc;border-radius:6px;width:200px">
    <button id="kirim" style="padding:8px 16px;border:0;border-radius:6px;background:#1a73e8;color:#fff;cursor:pointer">
      📤 Kirim ke Firebase
    </button>
    <span id="status" style="font-size:14px"></span>
  </div>
</div>

<script src="https://www.geogebra.org/apps/deployggb.js"></script>
<script>
  const DB_URL = "__DB_URL__";
  const NODE   = "__NODE__";
  const statusEl = document.getElementById("status");

  const params = {
    appName: "__APP__",
    width: 800, height: 480,
    showToolBar: true, showAlgebraInput: true, showMenuBar: false,
    appletOnLoad: () => { statusEl.textContent = "GeoGebra siap ✅"; }
  };
  new GGBApplet(params, true).inject("ggb");

  document.getElementById("kirim").onclick = async () => {
    const nama = document.getElementById("nama").value.trim();
    if (!nama) { statusEl.textContent = "⚠️ Isi nama dulu."; return; }
    try {
      // getPNGBase64(skala, transparan, dpi) -> string base64 tanpa prefix
      const b64 = ggbApplet.getPNGBase64(1, false, 72);
      statusEl.textContent = "Mengirim...";
      const res = await fetch(DB_URL + "/" + NODE + ".json", {
        method: "POST",                       // POST = push, id unik dibuat otomatis
        body: JSON.stringify({
          nama: nama,
          waktu: new Date().toISOString(),
          gambar: b64
        })
      });
      if (!res.ok) throw new Error("HTTP " + res.status + " (cek Rules database)");
      statusEl.textContent = "✅ Terkirim! Klik 'Muat ulang galeri' di bawah.";
    } catch (e) {
      statusEl.textContent = "❌ Gagal: " + e.message;
    }
  };
</script>
"""
        st.components.v1.html(
            HTML.replace("__DB_URL__", DB_URL).replace("__NODE__", NODE).replace("__APP__", app_name),
            height=600,
            scrolling=True,
        )

        st.divider()
        st.subheader("🖼️ Galeri dari Firebase")
        st.button("🔄 Muat ulang galeri")  # klik = rerun halaman

        try:
            r = requests.get(
                f"{DB_URL}/{NODE}.json",
                params={"orderBy": '"$key"', "limitToLast": jumlah},
                timeout=15,
            )
            r.raise_for_status()
            data = r.json() or {}
        except requests.RequestException as e:
            st.error(f"Gagal membaca database: {e}")
            st.stop()

        if not data:
            st.caption("Belum ada gambar.")
        else:
            # key push Firebase terurut waktu -> balik agar yang terbaru di depan
            items = list(data.items())[::-1]
            kolom = st.columns(3)
            for i, (key, v) in enumerate(items):
                with kolom[i % 3]:
                    st.image(base64.b64decode(v["gambar"]), use_container_width=True)
                    st.caption(f"**{v.get('nama', '-')}** · {v.get('waktu', '')[:16].replace('T', ' ')}")

                    

def diskusi_GA():
    # Ganti dengan data akun Anda masing-masing
    CLOUD_NAME = "dfkw4ux0e" 
    UPLOAD_PRESET = "diskusi_geogebra" # Hasil dari Langkah 1
    CLOUDINARY_URL = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/image/upload"

    # Endpoint REST API resmi Cloudinary untuk Upload Gambar
    html_content = """
<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <script type="text/javascript" src="https://cdn.geogebra.org/apps/deployggb.js"></script>
        <style>
            body { margin: 0; padding: 0; font-family: sans-serif; background-color: #f8f9fa; text-align: center; }
            #ggb-element { width: 100%; height: 500px; border: 1px solid #ddd; border-radius: 8px; }
            .btn-container { margin-top: 15px; }
            .download-btn {
                background-color: #FF4B4B; color: white; border: none;
                padding: 12px 24px; font-size: 16px; font-weight: bold;
                border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .download-btn:hover { background-color: #E04040; }
        </style>
    </head>
    <body>

        <div id="ggb-element"></div>
        
        <div class="btn-container">
            <button class="download-btn" onclick="unduhGrafikGeoGebra()">💾 Selesai & Unduh Gambar Grafik</button>
        </div>

        <script type="text/javascript">
            // Inisialisasi parameter aplikasi GeoGebra
            var params = {
                "appName": "classic", 
                "width": 900, 
                "height": 500,
                "showToolBar": true, 
                "showAlgebraInput": true, 
                "showMenuBar": true
            };
            var applet = new GGBApplet(params, true);
            
            // Memastikan injeksi langsung tanpa menunggu event window.load yang sering tertunda
            setTimeout(function() {
                applet.inject('ggb-element');
            }, 300);

            // Fungsi mengunduh file PNG langsung ke komputer user (Aman dari CORS)
            function unduhGrafikGeoGebra() {
                if (typeof ggbApplet !== 'undefined') {
                    var base64Image = ggbApplet.getPNGBase64(1.5, false);
                    
                    var link = document.createElement('a');
                    link.href = "data:image/png;base64," + base64Image;
                    link.download = "hasil_diskusi_geogebra.png";
                    link.click();
                } else {
                    alert("Aplikasi GeoGebra belum siap.");
                }
            }
        </script>
    </body>
    </html>
"""

    st.components.v1.html(html_content, height=550, width=820)
    st.write("---")
    st.subheader("📤 Unggah Hasil Diskusi ke Cloudinary")
    st.info("Setelah menekan tombol **'Selesai & Unduh Gambar Grafik'** di atas, masukkan file gambar yang terunduh ke dalam kotak di bawah ini untuk disimpan secara permanen.")
    
    # Elemen file uploader bawaan Streamlit yang dijamin aman
    uploaded_file = st.file_uploader("Pilih file hasil_diskusi_geogebra.png Anda", type=["png"])

    if uploaded_file is not None:
        with st.spinner("Sedang memproses dan mengunggah gambar ke Cloudinary Anda..."):
            try:
                # Siapkan data untuk dikirim melalui library requests Python
                files = {"file": uploaded_file.getvalue()}
                data = {"upload_preset": UPLOAD_PRESET}
                
                # Eksekusi POST Request dari sisi server (Kebal terhadap CORS browser)
                response = requests.post(CLOUDINARY_URL, files=files, data=data)
                
                if response.status_code == 200:
                    cloudinary_url = response.json().get("secure_url")
                    
                    st.balloons()
                    st.success("🎉 Luar biasa! Hasil diskusi berhasil tersimpan secara permanen di Cloudinary.")
                    st.text_input("Tautan Gambar Publik Anda (Cloudinary URL):", value=cloudinary_url)
                    st.image(cloudinary_url, caption="Preview Hasil Gambar yang Tersimpan", use_container_width=True)
                else:
                    st.error(f"Cloudinary menolak berkas (Error {response.status_code}): {response.text}")
            except Exception as e:
                st.error(f"Terjadi kegagalan koneksi: {str(e)}")
    st.subheader("🖼️ Galeri Hasil Diskusi GeoGebra (Public Mode)")
    TAG_NAME = "diskusi_geogebra"
    PUBLIC_LIST_URL = f"https://res.cloudinary.com/ dfkw4ux0e/image/list/diskusi_geogebra.json"
    if st.button("🔄 Segarkan & Muat Semua Gambar Diskusi"):
        with st.spinner("Mengambil galeri gambar dari Cloudinary..."):
            try:
                # Mengambil file JSON publik dari server CDN Cloudinary
                response = requests.get(PUBLIC_LIST_URL)
                
                if response.status_code == 200:
                    data = response.json()
                    daftar_assets = data.get("resources", [])
                    
                    if not daftar_assets:
                        st.info("Belum ada gambar yang memiliki tag 'diskusi_geogebra'.")
                    else:
                        st.success(f"Berhasil memuat {len(daftar_assets)} gambar diskusi terbaru!")
                        
                        # Tampilkan gambar dalam susunan grid 3 kolom
                        kolom = st.columns(3)
                        
                        for indeks, asset in enumerate(daftar_assets):
                            # Menyusun URL gambar publik dari data JSON
                            public_id = asset.get("public_id")
                            format_file = asset.get("format")
                            versi = asset.get("version")
                            
                            # Struktur URL gambar publik Cloudinary
                            url_gambar = f"https://res.cloudinary.com/{CLOUD_NAME}/image/upload/v{versi}/{public_id}.{format_file}"
                            
                            with kolom[indeks % 3]:
                                st.image(url_gambar, use_container_width=True)
                                st.caption(f"🆔 ID: {public_id}")
                                st.write("---")
                                
                elif response.status_code == 404:
                    st.warning("Folder/Tag belum terbentuk. Pastikan Anda sudah mengunggah minimal satu gambar baru dari aplikasi.")
                else:
                    st.error("Gagal memuat galeri. Pastikan opsi 'Resource list' di menu Settings > Security Cloudinary Anda sudah di-uncheck.")
                    
            except Exception as e:
                st.error(f"Terjadi masalah koneksi: {str(e)}")


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

if st.session_state['kumpulan']['pertemuan6']:
    pertemuan_6()

if st.session_state['kumpulan']['diskusi']:
    diskusi_GA()

#============================

if st.sidebar.button("Bagian Depan"):
    st.session_state['kumpulan']={'latar':True, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}
    st.rerun()

if st.sidebar.button("RPS dan Referensi"):
    st.session_state['kumpulan']={'latar':False, 'rps':True, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}
    st.rerun()

if st.sidebar.button("Koordinat dan Polar"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':True,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}
    st.rerun()

if st.sidebar.button("Rumus Jarak"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':True,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}
    st.rerun()

if st.sidebar.button("Rumus Luas Segitiga dan Luas Segi Empat"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':True,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}
    st.rerun()
if st.sidebar.button("Persamaan Garis dan Gradien"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':True,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':False}
    st.rerun()
if st.sidebar.button("Persamaan Garis Lurus yang Sejajar dan Tegak Lurus"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':True,'pertemuan6':False,'diskusi':False}
    st.rerun()
if st.sidebar.button("Persamaan Garis Lurus (Bagi Sudut dan Berkas Garis)"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':True,'diskusi':False}
    st.rerun()
st.sidebar.markdown('---')
if st.sidebar.button("Diskusi"):
    st.session_state['kumpulan']={'latar':False, 'rps':False, 'pertemuan1':False,
                                  'pertemuan2':False,'pertemuan3':False,'pertemuan4':False,
                                  'pertemuan5':False,'pertemuan6':False,'diskusi':True}
    st.rerun()

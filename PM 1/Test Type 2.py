from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simulasi database tugas mahasiswa
database_tugas = {
    "Andi": ["Tugas Matematika", "Tugas Fisika"],
    "Budi": ["Tugas Kimia", "Tugas Biologi"],
    "Citra": ["Tugas Sejarah", "Tugas Geografi"]
}

@app.route('/')
def home():
    return render_template_string('''
        <h1>Selamat datang di SV IPB Class</h1>
        <form action="/cek_tugas" method="post">
            Nama: <input type="text" name="name"><br>
            Usia: <input type="number" name="age"><br>
            Kode Tugas: <input type="text" name="kode_tugas"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/cek_tugas', methods=['POST'])
def cek_tugas():
    name = request.form['name']
    age = int(request.form['age'])
    kode_tugas = request.form['kode_tugas']

    if age < 18:
        return "Anda masih di bawah umur, mohon maaf."

    if name in database_tugas:
        tugas_belum_dikerjakan = database_tugas[name]
        if tugas_belum_dikerjakan:
            tugas_list = ''.join([f'<li>{tugas}</li>' for tugas in tugas_belum_dikerjakan])
            return f'''
                <h1>Tugas yang belum dikerjakan oleh {name}:</h1>
                <ul>{tugas_list}</ul>
            '''
        else:
            return f"{name} tidak memiliki tugas yang belum dikerjakan. Selamat!"
    else:
        return f"Nama {name} tidak ditemukan dalam database."

if __name__ == '__main__':
    app.run(debug=True)


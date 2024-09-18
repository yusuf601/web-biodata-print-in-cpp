from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/generate-cpp', methods=['POST'])
def generate_cpp():
    nama = request.form['nama']
    nim = request.form['nim']

    # Template C++ yang akan dibuat
    cpp_template = f"""
    #include <iostream>

    int main() {{
        std::cout << "Nama: {nama}" << std::endl;
        std::cout << "NIM: {nim}" << std::endl;
        std::cout << "Jurusan :{jurusan} << std::endl;
        return 0;
    }}
    """

    with open(f"{nim}.cpp", "w") as cpp_file:
        cpp_file.write(cpp_template)

    return f"File {nim}.cpp berhasil dibuat!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pobieramy dane z formularza
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        
        # Zapisz dane do pliku tekstowego
        with open('data.txt', 'a') as file:
            file.write(f"Imie: {first_name}\nNazwisko: {last_name}\nEmail: {email}\n\n")
        
        # Możesz dodać komunikat po zapisaniu danych
        return 'Dane zostały zapisane!'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

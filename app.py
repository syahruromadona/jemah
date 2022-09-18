from flask import Flask, render_template, request, send_file
import aicontent
import config


app = Flask(__name__)
app.config.from_object(config.config['development'])


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Create multiple questions and answer from this paragraph.\n\nPepsin is an endopeptidase that breaks down proteins into smaller peptides. It is produced in\nthe stomach and is one of the main digestive enzymes. Pepsin's proenzyme, pepsinogen, is\nreleased by the chief cells in the stomach wall, and upon mixing with the hydrochloric acid of\nthe gastric juice, pepsinogen activates to become pepsin.{} \n\n- What is pepsin? Pepsin is an endopeptidase that breaks down proteins into smaller peptides.\n- What is the proenzyme of pepsin? Pepsin's proenzyme is pepsinogen.".format(submission)
        openAiAnswer = aicontent.openAiQuery(query)
        user = submission

        with open('people.csv', 'w') as out :
            openAiAnswer = openAiAnswer.replace("? ", "?,")
            lines = [line for line in openAiAnswer.split('-')]
            #setiap kali jumpa '-' kita akan split the string to multiple string
            openAiAnswer = '\n'.join(lines)
            #Kita akan join line2 tersebut dengan '\n', menyebabkan dia break line
            out.write(openAiAnswer)
        
    
    return render_template('product-description.html', **locals())

@app.route('/download')
def download():
    path = 'people.csv'
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.run(debug=True)
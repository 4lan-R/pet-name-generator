from flask import Flask, render_template, request
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


main = Flask(__name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/out', methods=['POST', 'GET'])
def out():
    if request.method == 'POST':
        animaltype = request.form.get('animal')
        petcolor = request.form.get('color')

        llm = OpenAI(openai_api_key="###### add api key here ######",temperature=0.7)

        prompt_templates = PromptTemplate(
            input_variables=['animaltype', 'petcolor'],
            template='suggest 5 cool names for my pet {animaltype} with colour {petcolor}'
        )

        name_generator = LLMChain(llm=llm, prompt=prompt_templates, output_key='output')
        pet_names = name_generator({'animaltype': animaltype, 'petcolor': petcolor})

        pet_names = pet_names['output']

        return render_template('out.html', pet_names=pet_names)
    else:
        return render_template('out.html')

if __name__ == '__main__':
    main.run(debug=True)

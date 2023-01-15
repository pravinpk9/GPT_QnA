
import openai
openai.api_key = "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"

# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def model_predict():
    try:
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt="what is acetaminophen  used for?\nA:",
          temperature=0,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          stop=["\n"]
        )
        return response
    except Exception as err:
        return str('error for: '+ str(err))

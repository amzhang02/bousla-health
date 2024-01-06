from openai import OpenAI

class OpenAIClassifier:
  def __init__(self, api_key):
    self.api_key = api_key

  def get_category(self, text):
    if text is None or text == "" or text.isspace():
      raise Exception("Inputted text is empty or of type None. Text is required to complete the request.")
    client = OpenAI(api_key=self.api_key)
    if client is None:
      raise Exception("Client is None. Either failed to connect with OpenAI or API key is invalid.")
    labels = ["sexHealth", "drug","alcohol" "cancer", "nutrition", "fitness", "prescriptions", "vaccine", "other"]
    try:
      message = f"Here is the post: \n {text} \n Your response should be just the label you think is most appropriate."
      response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "You are a very clever classifier. You will be given a post and asked to classify it under one of the labels in the following list: [sexHealth, drug, alcohol, cancer, nutrition, fitness, prescriptions, vaccine, other]."},
          {"role": "user", "content": message}
        ],
        temperature=0.5,
        max_tokens=256,
      )
      if response.choices[0].message.content not in labels:
        raise Exception("Response is not a valid label. Response: ", response.choices[0].message.content)
      return response.choices[0].message.content
    except Exception as e:
      raise Exception("Failed to complete request. Error: " + str(e))
    
# for testing:

# api_key = open("./env",'r').readlines()[0].strip("\n")
# myClassifier = OpenAIClassifier(api_key)
# response = myClassifier.get_category("How do we address the controversy and misinformation surrounding nutrition and diet trends?")
# print(response)

# worked. output: "Nutrition"
# from: ChatCompletion(id='chatcmpl-8Oy81o1yTi3cWT3UJHCmcrQELfMtT', choices=[Choice(finish_reason='stop', index=0, message=ChatCompletionMessage(content='Nutrition', role='assistant', function_call=None, tool_calls=None))], created=1700961697, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=2, prompt_tokens=98, total_tokens=100))
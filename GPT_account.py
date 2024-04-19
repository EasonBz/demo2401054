import openai
#openai.api_base = "https://openkey.cloud/v1"
openai.api_key = ""
class OfficialGPT:
    def call(self, query: str):
        try:
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": "You are a assistant."}, {"role": "user", "content": query}]
            )
            response_content = chat_completion.choices[0].message['content']
            return True, response_content
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return False, str(e)

GPT = OfficialGPT()

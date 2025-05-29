import litellm

def query_agent(prompt):
    response = litellm.completion(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    print(response.choices[0].message.content)

if __name__ == "__main__":
    query_agent("Hello, how are you?")
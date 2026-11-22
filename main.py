
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o-mini")

# Three different prompts
prompts = [
    "What is Generative AI? Explain in simple words.",
    
    "Explain how Python works with a simple example.",
    
    "Explain how LangChain and LangSmith work together in an AI application."
]

# Send prompts and print responses
for i, prompt in enumerate(prompts, start=1):
    print(f"\n========== RUN {i} ==========")
    print(f"Prompt: {prompt}")

    response = llm.invoke(prompt)

    print(f"Response: {response.content}")

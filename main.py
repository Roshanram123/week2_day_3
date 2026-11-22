
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load API keys and LangSmith settings from .env
load_dotenv()

# Initialize the ChatOpenAI model using LangChain
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Create a prompt template
prompt_template = PromptTemplate.from_template(
    "Answer the following question in simple English:\n\n{question}"
)

# Create a LangChain pipeline (LCEL)
chain = prompt_template | llm

# Three different prompts
prompts = [
    "What is Generative AI? Explain with simple examples.",
    "What is Python? Explain how it works with a practical example.",
    "How do LangChain and LangSmith work together in an AI application?"
]

# Execute all three prompts
for index, question in enumerate(prompts, start=1):

    print(f"\n========== RUN {index} ==========")
    print(f"\nPrompt: {question}")

    try:
        response = chain.invoke({
            "question": question
        })

        print("\nAI Response:")
        print(response.content)

        print("\n------------------------------")

    except Exception as error:
        print(f"\nError: {error}")

print("\nAll prompts have been processed!")

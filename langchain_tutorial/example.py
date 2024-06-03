import os
from dotenv import load_dotenv
from langchain_openai  import OpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    template = """Question: {question}"""

    prompt = PromptTemplate.from_template(template)

    llm = OpenAI(openai_api_key=OPENAI_API_KEY)

    llm_chain = prompt | llm

    question = "Quelles sont les technos les plus utilisé en tant que data enginer ?"

    print(llm_chain.invoke(question))


if __name__ == "__main__":
    main()

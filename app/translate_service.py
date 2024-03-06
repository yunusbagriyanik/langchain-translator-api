from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


def translate(text, target_language):
    load_dotenv()

    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    translator_prompt_template = PromptTemplate(
        input_variables=["text"], template=prompt
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=translator_prompt_template)
    res = chain.invoke(input={"text": text})
    return res

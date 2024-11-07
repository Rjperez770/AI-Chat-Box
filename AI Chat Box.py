from langchain_ollama import OllamaLLM
from langchain_core.promts import ChatPromptTemplate

template = """
Answer the question below. 

Here is the conversation history: {context} #embedding this variable

Question: {question}# and this one inside the prompt

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result= chain.invoke()

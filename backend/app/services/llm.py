from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from app.config import GROQ_API_KEY, GROQ_MODEL
from app.services.vectorstore import search

llm = None


def get_llm():
    global llm
    if llm is None:
        llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL)
    return llm


def get_answer(question):
    relevant_chunks = search(question)
    context = "\n\n".join([chunk.page_content for chunk in relevant_chunks])

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional assistant for Mukesh's personal chatbot. Respond in third person — refer to him as 'Mukesh' or 'he'. Keep responses natural, concise, and professional. On greetings, greet back briefly and let them know you can help with questions about Mukesh's experience, skills, or education. Only answer based on the provided context. If the answer is not in the context, say something like 'That information isn't available here, but you can reach out to Mukesh directly to discuss.'"),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ])

    chain = prompt | get_llm()
    response = chain.invoke({"context": context, "question": question})
    return response.content

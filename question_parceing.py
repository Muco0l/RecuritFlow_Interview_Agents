def get_questions(job_title,jd,company,level,interview_time):
    from langchain_google_genai import GoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate
    from dotenv import load_dotenv
    from langchain_core.output_parsers import StrOutputParser
    from PyPDF2 import PdfReader
    import docx
    load_dotenv()
    def extract_text_from_pdf(file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    def extract_text_from_docx(file_path):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    def extract_resume_text(file_path):
        if file_path.endswith(".pdf"):
            return extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            return extract_text_from_docx(file_path)
        else:
            raise ValueError("Unsupported file format")
    resume_text = extract_resume_text("mukul_resume_angle.pdf")
    model = GoogleGenerativeAI(model="gemini-2.0-flash")
    prompt_templet = ChatPromptTemplate(
        [
    ("system",f"You are an assistent of interviewer from {company}.Here is the Job Title:{job_title} Job Description:{jd}Here is the Candidates Resume:{resume_text}Your task is to make a short and concise instructions manual for the interviewer so that it can test how well this candidate fits the job.Start with easier, broader questions, and then go deeper based on gaps or strengths.provide the list of questions and the points the interview sholud focus on that the candidate can complete the interviwe in {interview_time} minutes. also add DSA question if time permits. Also provide the time required for each question. The interview should be conducted in a friendly manner and the interviewer should be polite and respectful to the candidate.do not introduce yourself and do not add any other input than string"),
        ]
    )
    chain = prompt_templet | model | StrOutputParser()
    result = chain.invoke({"job_title":job_title,"jd":jd,"company":company,"level":level,"resume":resume_text,"interview_time":interview_time})
    #
    return result
    #print(result)
#get_questions(job_title="python intern",jd="python intern",company="amazon",level=3,interview_time=10)

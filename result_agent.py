from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate   
from dotenv import load_dotenv          
from langchain_core.output_parsers import JsonOutputParser
import json
load_dotenv()

def get_result(transcript):


    model = GoogleGenerativeAI(model="gemini-2.0-flash")
    parser = JsonOutputParser()
    prompt = PromptTemplate(
        template="you are a expert interview analyzer so be honest and critical, and you are analyzing Transcript of a interview.\n{transcript}\n{format_instructions}\n\nPlease provide a detailed analysis of the interview including overall feedback, strengths, weaknesses, recommendations,and a finalScore out of 100 ,scoreJustification and tipsForTacklingTheInterview .  The output should be in JSON onlu use double Quote and every key under interviewAnalysis key\n",
        input_variables=["transcript"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
)
    chain = prompt | model | parser
    result = chain.invoke({"transcript":transcript})
    return result
# RecruitFlow-Agents

This repository contains the backend AI agents for **RecruitFlow-Interviews** — a live, intelligent interview simulation platform designed to replicate realistic interview experiences using real-time WebRTC and LLM-driven agents.

---

## 🧠 Overview

RecruitFlow-Agents is the AI core behind the interview experience. It consists of multiple intelligent agents built using LangChain and LLM APIs (Gemini 2.0 Flash + GPT-4o), which simulate:

- Resume parsing
- Job description understanding
- Dynamic question generation
- Live audio conversation with the candidate

---

## 🧩 System Architecture

```mermaid
graph TD
    A[Frontend UI (Nextjs)] -->|LiveKit Token + Room| B[LiveKit Cloud]
    B --> C[Candidate (via WebRTC)]
    B --> D[RecruitFlow-Agent (AI Interviewer)]
    D --> E[Google Gemini 2.0 Flash]
    D --> F[OpenAI GPT-4o (Streaming)]
    D --> G[LangChain Tools]
    D --> H[PDF Report Generator]
```
##🧑‍💻 Technologies Used
Python 3.10+

LangChain

Google Gemini 2.0 Flash API

OpenAI GPT-4o (streaming)

LiveKit Python SDK

Reportlab(Python) (for structured interview report generation)

React

NextJs


##🧠 Agents Overview
**ResumeParserAgent**: Extracts candidate details and email from uploaded resumes.(PyPDF)

**JDInterpreterAgent**: Reads job description to understand context.Crafts dynamic questions based on role, JD, and resume.(Gemini-2.0-Flash)
![interpretation](interpret.png)

**InterviewConductorAgent**: Connects via LiveKit and handles real-time interactions using GPT-4o.
![Console Interview](interview_console.png)

**Result and Report**: Makes a detailed PDF Report of The Responces.
![PDFreport](report.png)

##🔗 WebRTC Connection Flow (LiveKit Cloud)
Frontend initializes a new interview session via LiveKit API.

It shares room credentials (Room name, Token) with the backend via API or WebSocket.

The backend joins the same LiveKit room as a "virtual interviewer".

Backend listens to candidate's audio, streams responses via GPT-4o, and sends back audio in real-time.


#Connecting To the Client

**The Client side Frontend connects to this agent via WebRTC connection i.e. with LiveKit Cloud**
For the Frontend Client Please Visit my Repo: [frontend](https://github.com/Muco0l/RecuritFlow_interview_Client.git)

#The Final Product You get is:
![final](final.png)
**i.e. a perfect tool to practice and tackel any interview**

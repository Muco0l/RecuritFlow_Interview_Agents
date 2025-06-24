# 🎤 RecruitFlow – AI-Powered Real-Time Interview Simulator

RecruitFlow is an intelligent, real-time interview simulation platform built using advanced LLMs and WebRTC technologies. It mimics a live interviewer by generating dynamic, job-specific questions based on candidate resumes and job descriptions.

![banner](interview_demo.png)

---

## 🔍 Key Features

- 🤖 **AI Interviewer Agent**: Uses GPT-4o and Gemini 2.0 to ask personalized, role-based questions.
- 🎥 **Live Audio/Video Interaction**: Built using LiveKit + WebRTC for seamless real-time communication.
- 📄 **Context-Aware Question Flow**: Tailors follow-ups based on user answers and resume data.
- 📝 **Response Logging**: Logs Q&A in structured format (JSON) for post-interview review.
- 🕒 **Dynamic Duration Control**: Interview ends after 10 minutes or a set number of questions.
- 🧠 **LLM-Driven Evaluation** *(WIP)*: Potential to score responses or give feedback.

---

## ⚙️ Tech Stack

| Layer         | Tech                                 |
|---------------|--------------------------------------|
| AI/LLMs       | GPT-4o, Gemini 2.0 Flash             |
| Frameworks    | LangChain, Python                    |
| Real-Time     | LiveKit, WebRTC                      |
| Backend       | Supabase (auth & room logic), Flask  |
| Logging       | JSON, File-based logging             |
| Infra         | Livekit Clouse    |

---

## 🚀 How It Works

1. User enters a job title and optionally uploads a resume.
2. The AI interviewer (LLM agent) generates role-based questions.
3. Real-time communication happens via LiveKit and WebRTC.
4. Each question and user response is logged in real-time.
5. Interview auto-ends after 10 minutes or N questions.

---

## 📸 Demo Screenshots

*(Insert screenshots or video demo links here)*

---



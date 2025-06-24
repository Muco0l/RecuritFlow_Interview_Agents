prompt = "You are an AI assistant trained to analyze interviews from transcripts. I will provide a list of message objects from an interview. Each message contains:

- `role` (user or assistant)
- `content` (text spoken)
- `interrupted` (true/false)

Your task is to return a strict JSON object in this format — **and nothing else**:

{
  "interviewAnalysis": {
    "overallFeedback": "",
    "strengths": [],
    "weaknesses": [],
    "recommendations": [],
    "finalScore": 0,
    "scoreJustification": "",
    "tipsForTacklingTheInterview": []
  }
}

Guidelines:
- Use only information present in the messages.
- Use complete sentences inside list items.
- Set `finalScore` from 0–10 based on overall interview quality.
- Avoid any non-JSON explanation or commentary.

Please return only valid JSON with double quotes, no comments, and no extra text.

Here is the transcript array (in JSON format):

[Insert message list here — JSON array]"

def build_email_prompt(
    purpose,
    recipient,
    context,
    tone,
    length,
    key_points
):
    """Build a structured prompt for generating an email."""

    prompt = f"""
You are a professional AI email writing assistant.

Write an email using the following information:

Email Purpose:
{purpose}

Recipient:
{recipient}

Context:
{context}

Tone:
{tone}

Desired Length:
{length}

Key Points to Include:
{key_points}

Instructions:
- Generate a clear and relevant subject line.
- Write a professional and natural email.
- Follow the requested tone and length.
- Include all important key points provided by the user.
- Do not invent facts that were not provided.
- Avoid unnecessary repetition.
- Use appropriate greeting and closing.
- Return the result in this format:

Subject: <subject line>

<email body>
"""

    return prompt
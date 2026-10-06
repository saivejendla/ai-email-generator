def build_rewrite_prompt(email_text, rewrite_style):
    """Build a structured prompt for rewriting an existing email."""

    prompt = f"""
You are a professional AI email editing assistant.

Rewrite the email below.

Rewrite Style:
{rewrite_style}

Original Email:
{email_text}

Instructions:
- Preserve the original meaning.
- Do not invent new facts.
- Improve clarity and readability.
- Keep all important information from the original email.
- Follow the requested rewrite style.
- Use natural and professional language.
- Include a subject line if appropriate.
- Avoid unnecessary repetition.

Return the result in this format:

Subject: <subject line>

<rewritten email body>
"""

    return prompt
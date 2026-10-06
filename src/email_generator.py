import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


def generate_email(prompt):
    """Generate an email using Google Gemini."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gemini API key is not configured."
        )

    client = genai.Client(api_key=api_key)

    try:

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        return interaction.output_text

    except Exception as error:

        error_message = str(error).lower()

        # Gemini server temporarily unavailable
        if (
            "503" in error_message
            or "service_unavailable" in error_message
            or "high demand" in error_message
        ):
            raise RuntimeError(
                "Gemini is temporarily busy due to high demand. "
                "Please try again in a few minutes."
            )

        # API quota / rate limit
        if (
            "429" in error_message
            or "quota" in error_message
            or "rate limit" in error_message
        ):
            raise RuntimeError(
                "The Gemini API usage limit has been reached. "
                "Please try again later."
            )

        # Authentication problem
        if (
            "401" in error_message
            or "403" in error_message
            or "api key" in error_message
        ):
            raise RuntimeError(
                "Unable to authenticate with Gemini. "
                "Please check the API configuration."
            )

        # Other unexpected API errors
        raise RuntimeError(
            "The AI service is currently unavailable. "
            "Please try again later."
        )
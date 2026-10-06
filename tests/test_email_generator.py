from src.email_generator import generate_email
from src.prompt_builder import build_email_prompt


def test_email_generator():

    prompt = build_email_prompt(
        purpose="Job Application",
        recipient="Hiring Manager",
        context="Applying for an AI Engineer position",
        tone="Professional",
        length="Short",
        key_points=(
            "Experience with Python, Generative AI, "
            "machine learning, and building AI applications"
        )
    )

    email = generate_email(prompt)

    assert email
    assert len(email) > 20

    print("Email generation test passed!")
    print("\nGenerated Email:\n")
    print(email)


if __name__ == "__main__":
    test_email_generator()
from src.prompt_builder import build_email_prompt


def test_prompt_builder():
    prompt = build_email_prompt(
        purpose="Job Application",
        recipient="Hiring Manager",
        context="Applying for an AI Engineer position",
        tone="Professional",
        length="Short",
        key_points="Python, Generative AI, and machine learning experience"
    )

    assert "Job Application" in prompt
    assert "Hiring Manager" in prompt
    assert "Professional" in prompt
    assert "Python" in prompt

    print("Prompt builder test passed!")
    print("\nGenerated Prompt:\n")
    print(prompt)


if __name__ == "__main__":
    test_prompt_builder()
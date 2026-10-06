from src.rewrite_prompt import build_rewrite_prompt


def test_rewrite_prompt():
    prompt = build_rewrite_prompt(
        email_text=(
            "Hi, I need leave tomorrow. "
            "Please approve my request."
        ),
        rewrite_style="Make it Professional"
    )

    assert "Hi, I need leave tomorrow" in prompt
    assert "Make it Professional" in prompt
    assert "Preserve the original meaning" in prompt
    assert "Do not invent new facts" in prompt

    print("Rewrite prompt test passed!")
    print("\nGenerated Rewrite Prompt:\n")
    print(prompt)


if __name__ == "__main__":
    test_rewrite_prompt()
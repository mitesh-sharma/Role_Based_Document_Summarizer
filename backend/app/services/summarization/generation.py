from app.services.ai_client import client

def summarize(context: str, role_description: str, max_words: int) -> str:

    prompt = f"""
    You are generating a role-specific strategic interpretation of a document.

    First, internally determine:
    - What this role is accountable for
    - What decisions this role makes
    - What risks and outcomes this role is evaluated on

    Then, produce a summary of the document filtered strictly through those priorities.

    Instructions:
    - Include only information that materially affects this role's decisions, risks, performance, or responsibilities.
    - Exclude information that does not influence this role's actions.
    - Do NOT describe the role itself.
    - Do NOT use second-person narration.
    - Do NOT restate generic responsibilities.
    - Maintain an analytical, executive corporate tone.
    - Avoid bullet points.
    - Write approximately {max_words} words.

    Role:
    {role_description}

    Document Context:
    {context}
    """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt,
        config={
            "temperature": 0.3,
            "max_output_tokens": 3000,
        },
    )

    return response.text

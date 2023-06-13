# Prompts for OpenAI GPT language model

COMPLETE_PROMPT = "Complete: {sentence}"

PROOFREAD_PROMPT = """
    Imagine you are a world-renowned essay editor specializing in various academic disciplines.
    Your task is to provide explicit and structured feedback on the grammar, syntax, and
    overall flow of the sentences. Please provide suggestions or explanations, and focus
    equally on editing the given sentences to ensure clarity and coherence. Here's the
    initial sentence for editing: "{sentence}"
"""

REPHRASE_PROMPT = "Rephrase: {sentence}"

SUMMARIZE_PROMPT = "Summarize: {sentence}"

PROMPT_LIBRARY = {
    "complete": COMPLETE_PROMPT,
    "proofread": PROOFREAD_PROMPT,
    "rephrase": REPHRASE_PROMPT,
    "summarize": SUMMARIZE_PROMPT,
}

from typing import List, Optional, Union, Dict
from pydantic import BaseModel, Extra


# this is the default prompt template for qa
DEFAULT_QA_PROMPT_TEMPLATE = """
Use the following pieces of context to answer the question at the end. If you do not know the answer,
just say that you do not know, do not try to make up an answer.
Context: {context}
Question: {question}
Helpful Answer:"""

# this is the default prompt template for if the user wants to summarize the context before qa prompt
DEFAULT_SUMMARIZATION_PROMPT_TEMPLATE = """
Summarize the following texts for me:
{context}

When summarizing, please keep the following in mind the following question:
{question}
"""


class CompletionParameters(BaseModel):
    model: str  # The model to be used for the API call.
    prompt_template: Optional[str] = None  # Template for the prompt to be used.

    # Optional OpenAI params: see https://platform.openai.com/docs/api-reference/chat/create
    messages: List = []  # List of messages for conversation-based models.
    functions: List = []  # List of functions for advanced model operations.
    function_call: str = ""  # String to specify a particular function call, if needed.

    timeout: Optional[Union[float, int]] = None  # Timeout for the API request.
    temperature: Optional[float] = None  # Controls randomness: higher value means more random responses.
    top_p: Optional[float] = None  # Nucleus sampling: higher value means more diverse responses.
    n: Optional[int] = None  # Number of completions to generate for each prompt.
    stream: Optional[bool] = None  # Whether to stream responses or not.
    stop: Optional[str] = None  # Sequence at which the model should stop generating further tokens.
    max_tokens: Optional[float] = None  # Maximum number of tokens to generate in each completion.
    presence_penalty: Optional[float] = None  # Penalty for new tokens based on their existing presence in the text.
    frequency_penalty: Optional[float] = None  # Penalty for new tokens based on their frequency in the text.
    logit_bias: Optional[Dict] = None  # Adjusts the likelihood of specified tokens appearing in the completion.
    user: Optional[str] = None  # Identifier for the end-user, for usage tracking.

    # openai v1.0+ new params
    response_format: Optional[Dict] = None  # Format of the response, if specific formatting is required.
    seed: Optional[int] = None  # Random seed for deterministic completions.
    tools: Optional[List[str]] = None  # List of additional tools or features to be used.
    tool_choice: Optional[str] = None  # Specific tool to be used, if applicable.
    deployment_id: Optional[str] = None  # Identifier for the deployment.

    # set api_base, api_version, api_key
    base_url: Optional[str] = None  # Base URL of the API.
    api_version: Optional[str] = None  # Version of the API to be used.
    api_key: str  # API key for authentication.
    model_list: Optional[List] = None  # List of models, API bases, keys, etc., for dynamic selection.

    class Config:
        extra = Extra.forbid
        arbitrary_types_allowed = True
        use_enum_values = True

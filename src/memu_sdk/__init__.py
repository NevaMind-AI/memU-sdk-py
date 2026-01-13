"""
MemU Python SDK - Cloud API Client

This module provides a Python SDK for interacting with the MemU Cloud API,
enabling developers to programmatically manage structured, long-term memory
for AI agents.

Example:
    from memu_sdk import MemUClient

    # Initialize the client
    client = MemUClient(api_key="your_api_key")

    # Memorize a conversation
    result = await client.memorize(
        conversation_text="User: I love sci-fi novels.\\nAssistant: Noted, you prefer sci-fi.",
        user_id="user_123",
        agent_id="agent_123",
    )

    # Retrieve memories
    memories = await client.retrieve(
        query="What are the user's preferences?",
        user_id="user_123",
        agent_id="agent_123",
    )
"""

from memu_sdk.client import MemUClient
from memu_sdk.models import (
    MemorizeResult,
    MemoryCategory,
    MemoryItem,
    MemoryResource,
    RetrieveResult,
    TaskStatus,
)

__version__ = "1.0.0"

__all__ = [
    "MemUClient",
    "MemorizeResult",
    "MemoryCategory",
    "MemoryItem",
    "MemoryResource",
    "RetrieveResult",
    "TaskStatus",
    "__version__",
]

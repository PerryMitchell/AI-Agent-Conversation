# AI-Agent-Conversation

A Python-based tool that generates natural conversations between two AI agents on any given topic. The agents can use different language models (OpenAI, Groq, Anthropic, or Ollama) and automatically save conversations as both text and audio files.

## Features

Support for multiple AI providers:
- OpenAI (GPT models)
- Groq
- Anthropic (Claude models)
- Ollama (local deployment)

Core capabilities:
- Configurable conversation parameters
- Automatic conversation logging with timestamps
- Text-to-speech conversion
- Conversation export in both text and audio formats
- Dynamic agent personality assignment
- Flexible multi-API integration
- Environment variable support for API keys

## ⚠️ Proprietary Software - All Rights Reserved

This software is proprietary and confidential. All rights are reserved.

Copyright (c) 2024 Perry Mitchell

### Terms of Use:
- **Ownership**: This software and its source code are the exclusive property of Perry Mitchell. All rights, title, and interest in and to the Software remain with Perry Mitchell.

### Restrictions:
No part of this software may be:
- Copied
- Modified
- Merged
- Published
- Distributed
- Sublicensed
- Sold
- Used in any commercial environment
- Used in any private capacity without explicit written permission from Perry Mitchell.

**Permission Required**: Any use, modification, or distribution of this software requires explicit written consent from Perry Mitchell.

**No Warranty**: The software is provided "AS IS", without warranty of any kind, express or implied.

**Enforcement**: Any violation of these terms will be pursued to the fullest extent of the law.

For licensing inquiries and permissions, please contact: perry.mitchell@live.co.uk

## Requirements

- Python 3.x
- Required Python packages:
  - openai
  - requests
  - pyttsx3
  - anthropic
  - text_to_speech

## Environment Setup

The following environment variables need to be set:
```bash
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## Usage (Authorized Users Only)

Only users with explicit written permission may:

1. Configure conversation parameters:
```python
topic = "your topic here"
convo_length = 2  # Number of conversation exchanges
```

2. Initialize agents with specific providers:
```python
agentOne = AIAgent(api_to_use="anthropic", name="Shauna")
agentTwo = AIAgent(api_to_use="openai", name="Gretchin")
```

3. Run the script:
```bash
python conversation_generator.py
```

The script will automatically:
- Generate a conversation between the agents
- Save the conversation as a text file
- Convert the conversation to speech
- Save the audio version

## Output Files

- Text file: `conversations/{topic}_{agent1_details}_{agent2_details}.txt`
- Audio file: `conversations/{topic}_{agent1_details}_{agent2_details}.wav`

## Configuration

Authorized users can customize various parameters:

- Agent names and personalities
- AI models per provider:
  - OpenAI: Various GPT models
  - Groq: LLaMA and other models
  - Anthropic: Claude models
  - Ollama: Local models
- Conversation length and structure
- Speech rate and voice settings
- API endpoints and parameters
- Response formatting and logging

## Notice

This repository is public for demonstration purposes only. Viewing the code does not grant any rights to use, modify, or distribute the software. All usage requires explicit written permission from the copyright holder.

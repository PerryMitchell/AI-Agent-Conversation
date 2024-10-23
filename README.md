# AI-Agent-Conversation
AI Conversation Generator A Python-based tool that generates natural conversations between two AI agents on any given topic. The agents can use different language models (OpenAI, Groq, or Ollama) and automatically save conversations as both text and audio files.
A Python-based tool that generates natural conversations between two AI agents on any given topic. The agents can use different language models (OpenAI, Groq, or Ollama) and automatically save conversations as both text and audio files.

Features
Support for multiple AI providers:
OpenAI (GPT models)
Groq
Ollama
Configurable conversation parameters
Automatic conversation logging
Text-to-speech conversion
Conversation export in both text and audio formats
Dynamic agent personality assignment
Flexible API integration
⚠️ Proprietary Software - All Rights Reserved
This software is proprietary and confidential. All rights are reserved.

Copyright (c) 2024 Perry Mitchell

Terms of Use:
Ownership: This software and its source code are the exclusive property of Perry Mitchell. All rights, title, and interest in and to the Software remain with Perry Mitchell.

Restrictions: No part of this software may be:

Copied
Modified
Merged
Published
Distributed
Sublicensed
Sold
Used in any commercial environment
Used in any private capacity without explicit written permission from Perry Mitchell.
Permission Required: Any use, modification, or distribution of this software requires explicit written consent from Perry Mitchell.

No Warranty: The software is provided "AS IS", without warranty of any kind, express or implied.

Enforcement: Any violation of these terms will be pursued to the fullest extent of the law.

For licensing inquiries and permissions, please contact: perry.mitchell@live.co.uk
Requirements
Python 3.x
Required Python packages:
openai
requests
pyttsx3
text_to_speech
Usage (Authorized Users Only)
Only users with explicit written permission may:

Configure conversation parameters:
topic = "your topic here"
convo_length = 2  # Number of conversation exchanges
Run the script:
python conversation_generator.py
The script will generate a conversation and save it as both text and audio files in the conversations directory.

Output Files
Text file: conversations/{topic}_{agent1_details}_{agent2_details}.txt
Audio file: conversations/{topic}_{agent1_details}_{agent2_details}.wav
Configuration
Authorized users can customize various parameters:

Agent names
AI models
Conversation length
Speech rate and voice
API endpoints
Notice
This repository is public for demonstration purposes only. Viewing the code does not grant any rights to use, modify, or distribute the software. All usage requires explicit written permission from the copyright holder.

# Course AI Generator API

A FastAPI application that leverages Gemini AI to generate educational course content.

## Overview

This API service uses Google's Gemini AI model to automatically generate course materials, syllabi, and educational content. It packages the AI generation capabilities into a RESTful API built with FastAPI and served with Uvicorn.

## Features

- AI-powered course content generation
- Customizable content parameters
- RESTful API endpoints
- Fast performance with asynchronous support

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for serving the FastAPI application
- **Google Gemini AI**: Advanced language model for content generation
- **Python 3.8+**: Core programming language

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/course-gen-ai.git
cd course-gen-ai

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Start the API server:

```bash
uvicorn main:app --reload
```

## License

MIT

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

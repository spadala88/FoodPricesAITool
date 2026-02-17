# Food Prices AI Tool

An AI-powered tool for checking restaurant food prices using web scraping and natural language processing.

## Overview

This project provides an intelligent assistant that can answer questions about food prices from specific restaurants. It combines:

- **Large Language Models** (via Ollama) for natural language understanding
- **Model Context Protocol (MCP)** for tool integration
- **Web scraping** to fetch current menu prices
- **FastAPI backend** for API endpoints
- **Tkinter UI** for user interaction

## Features

- Query food prices using natural language (e.g., "What's the price of Chilli Gobi at Bawarchi Sunnyvale?")
- Supports multiple restaurants:
  - Bawarchi Indian Cuisine (Sunnyvale)
  - Bombay to Goa
- Real-time price fetching from restaurant websites
- Conversational AI interface

## Architecture

- **main.py**: FastAPI server with chat endpoint
- **agent.py**: Chat agent that orchestrates LLM and MCP tool calls
- **LocalMcpServer.py**: MCP server providing web scraping tools for restaurant menus
- **llm_ollama.py**: Integration with Ollama LLM
- **MainScreen.py**: Tkinter-based user interface
- **mcp_client.py**: Client for communicating with MCP server

## Requirements

- Python 3.8+
- Ollama with qwen2.5:7b-instruct model
- Required packages (see requirements.txt)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start Ollama server with the required model:
   ```bash
   ollama serve
   ollama pull qwen2.5:7b-instruct
   ```

3. Run the MCP server:
   ```bash
   python LocalMcpServer.py
   ```

4. Start the FastAPI backend:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 9001
   ```

5. Launch the UI:
   ```bash
   python MainScreen.py
   ```

## Usage

Enter queries like:
- "I want the price of Chilli Gobi at Bawarchi Sunnyvale"
- "What's the cost of Chicken Tikka at Goa restaurant"

The AI will scrape the relevant restaurant website and provide the current price information.

# 🤖 AIRA OS

AIRA OS is a modular, local-first Multi-Agent AI Operating System built with Python and Streamlit.

Unlike a traditional chatbot, AIRA OS plans tasks, assigns them to specialized AI agents, executes them through an orchestration engine, and maintains memory across interactions.

The project is designed to be scalable, allowing developers to add new AI agents with minimal changes.

---

# Features

- Local AI execution (privacy-first)
- Multi-Agent Architecture
- Intelligent Task Planning
- Agent Orchestration
- Persistent Memory
- Coding Assistant
- Research Assistant
- Chat Assistant
- Agent Registry
- Execution Engine
- Modular Architecture
- Modern Streamlit UI
- CSS-based custom interface
- Session management
- Extensible plugin-like agent system

---

# Current Agents

### Chat Agent

General conversations and user interactions.

### Research Agent

Research and information gathering.

### Coding Agent

Programming assistance, debugging, and code generation.

### Memory Agent

Stores and retrieves conversation memory.

### Critic Agent

Reviews responses and improves output quality.

### Planner

Breaks user requests into executable plans.

---

# Architecture

```
User
      │
      ▼
 Streamlit UI
      │
      ▼
 Orchestrator
      │
      ▼
 Planner
      │
      ▼
 Execution Engine
      │
      ▼
 Agent Registry
      │
      ├── Chat Agent
      ├── Research Agent
      ├── Coding Agent
      ├── Memory Agent
      └── Critic Agent
      │
      ▼
 Local Language Model
```

---

# Project Structure

```
AIRA-OS/
│
├── agents/
├── core/
├── memory/
├── models/
├── ui/
├── utils/
├── app.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/AIRA-OS.git
```

Move into the project.

```bash
cd AIRA-OS
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

# Technology Stack

- Python
- Streamlit
- Local LLM
- Modular AI Agents
- Object-Oriented Design

---

# Roadmap

- Voice Interface
- Vision Agent
- Web Search Agent
- PDF Agent
- File System Agent
- Email Agent
- Calendar Agent
- Tool Calling
- Long-Term Memory
- RAG Pipeline
- Autonomous Task Execution
- Multi-LLM Support
- Docker Deployment

---

# Why AIRA OS?

Most AI assistants are monolithic chatbots.

AIRA OS is designed as an operating system for AI agents where each agent has a dedicated responsibility coordinated by an orchestration engine.

This architecture makes the system modular, scalable, and suitable for future enterprise AI applications.

---

# License

MIT License

---

# Author

Khurshid

AI Engineer

Built with Python

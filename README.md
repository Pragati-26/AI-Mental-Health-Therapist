# 🧠 SafeSpace – AI Mental Health Therapist

SafeSpace is an intelligent mental health support application that combines AI-powered therapy with crisis detection and emergency helpline resources. Built with **LangChain**, **FastAPI**, and **Streamlit**, it provides empathetic, personalized mental health support through a conversational interface.

## ✨ Features

- **AI-Powered Therapy**: Uses the MedGemma model to provide empathetic, clinical-grade mental health responses
- **Crisis Detection**: Automatically detects crisis keywords and provides immediate crisis helpline information
- **Conversational UI**: Clean, user-friendly chat interface built with Streamlit
- **RESTful API**: FastAPI backend for scalable, production-ready endpoints
- **Emergency Resources**: Integrated Indian crisis helplines for immediate support
- **Session Management**: Maintains conversation history for coherent multi-turn dialogue

## 🏗️ Architecture

The application follows a modern client-server architecture:

```
SafeSpace AI Agent
├── Frontend (Streamlit)
│   └── Chat interface for users
├── Backend (FastAPI)
│   └── /ask endpoint for query processing
└── AI Agent
    ├── Crisis detection system
    ├── MedGemma LLM integration
    └── Mental health specialist tools
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [Ollama](https://ollama.ai) with MedGemma model installed
- pip or poetry

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SAFE_SPACE_AI_AGENT
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure MedGemma model is available**
   ```bash
   ollama pull alibayram/medgemma:4b
   ```

### Running the Application

**Option 1: Run Frontend + Backend Locally**

Terminal 1 - Start the backend:
```bash
python -m uvicorn backend.main:app --reload --port 8000
```

Terminal 2 - Start the frontend:
```bash
streamlit run frontend.py
```

The frontend will be available at `http://localhost:8501`

**Option 2: Run with Docker** (if applicable)
```bash
docker-compose up
```

## 📁 Project Structure

```
SAFE_SPACE_AI_AGENT/
├── frontend.py                 # Streamlit chat interface
├── main.py                     # Entry point
├── pyproject.toml              # Project metadata & dependencies
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── backend/
│   ├── main.py                 # FastAPI application & endpoints
│   ├── ai_agent.py             # Core AI agent logic
│   ├── tools.py                # MedGemma integration & tools
│   └── __pycache__/            # Python cache files
```

## 🔧 Configuration

### Backend URL
In `frontend.py`, update the `BACKEND_URL` to point to your backend deployment:

```python
BACKEND_URL = "https://ai-mental-health-therapist-3.onrender.com/ask"  # or your local/cloud URL
```

### Model Configuration
The MedGemma model parameters can be adjusted in `backend/tools.py`:

```python
options={
    "num_predict": 350,      # Max response length
    "temperature": 0.7,      # Creativity (0-1)
    "top_p": 0.9             # Diversity in responses
}
```

## 🛡️ Safety Features

### Crisis Detection
The system automatically detects crisis keywords including:
- `suicide`, `kill myself`, `end my life`
- `self harm`, `die`, `want to disappear`

When crisis is detected, the system immediately responds with:
- Empathetic acknowledgment
- Urgent help guidance
- **Indian Crisis Helplines**:
  - **Kiran**: 1800-599-0019
  - **iCALL**: +91 9152987821
  - **AASRA**: +91 9820466726

### AI Personality
The MedGemma model is fine-tuned with a clinical psychologist persona ("Dr. Emily Hartman") to provide:
- Emotional attunement
- Non-judgmental support
- Practical guidance
- Strength-focused responses

## 📦 Dependencies

Key dependencies:

| Package | Version | Purpose |
|---------|---------|---------|
| FastAPI | ≥0.129.0 | Backend API framework |
| Streamlit | ≥1.54.0 | Frontend UI framework |
| LangChain | ≥1.2.10 | LLM orchestration |
| Ollama | ≥0.6.1 | Local LLM inference |
| Pydantic | ≥2.12.5 | Data validation |
| Requests | ≥2.32.5 | HTTP client |
| Uvicorn | ≥0.41.0 | ASGI server |

See `pyproject.toml` for the complete dependency list.

## 🔌 API Endpoints

### POST `/ask`
Processes a user query and returns AI-generated response.

**Request:**
```json
{
  "message": "I've been feeling anxious lately"
}
```

**Response:**
```json
{
  "response": "I hear you. Anxiety is something many people experience...",
  "tool_called": "mental_health_specialist"
}
```

## 🛠️ Development

### Local Testing

1. Start backend: `python -m uvicorn backend.main:app --reload`
2. Test endpoint: `curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"message":"Hello"}'`

### Adding New Tools

Create new tools in `backend/tools.py`:

```python
def new_tool_function(user_input: str) -> str:
    # Implementation
    return response
```

Then integrate into `backend/ai_agent.py`:

```python
def handle_query(user_message: str):
    if is_crisis(user_message):
        return crisis_response()
    
    response = new_tool_function(user_message)
    return {
        "response": response,
        "tool_called": "tool_name"
    }
```

## 💡 Performance Optimization

- **Cold Start Optimization**: Frontend includes 60-second timeout for Render free tier
- **Response Limits**: MedGemma limited to 350 tokens for faster responses
- **Temperature Tuning**: Set to 0.7 for balance between consistency and creativity

## 📊 Deployment

### Render (Frontend + Backend)
1. Connect GitHub repository to Render
2. Create two services: one for FastAPI backend, one for Streamlit frontend
3. Set environment variables if needed
4. Deploy both services

### Environment Variables (if needed)
Create a `.env` file:
```env
OLLAMA_HOST=http://localhost:11434
BACKEND_URL=http://localhost:8000
```

## ⚠️ Important Notes

- **Ollama Requirement**: This application requires Ollama to be running locally or accessible remotely
- **MedGemma Model**: First run will download the ~4GB MedGemma model (you can customize with other models)
- **Privacy**: All conversations are processed locally; ensure compliance with data privacy regulations
- **Limitations**: AI responses should not replace professional mental health care

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional crisis keywords and responses
- Integration with professional help referral systems
- Multi-language support
- Enhanced conversation memory/context
- Response quality metrics

## 📄 License

[Add your license information here]

## ⚖️ Disclaimer

**SafeSpace is an AI support tool, not a replacement for professional mental health care.** If you or someone you know is in crisis, please contact emergency services or the crisis helplines listed above immediately.

## 📞 Support

For issues, questions, or feedback:
- Open an issue on GitHub
- Contact: [add contact information]

---

**Made with ❤️ for mental health support**
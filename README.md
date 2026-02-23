# 🚀 TalentPilot: AI-Powered Career Assistant

TalentPilot is a comprehensive, AI-driven platform designed to streamline the career development process. From deep-diving into resume analysis to providing interactive interview coaching, TalentPilot leverages state-of-the-art LLMs to help professionals navigate their career paths with confidence.

---

## ✨ Key Features

- 📄 **Advanced Resume Analysis**: Upload your resume as an image and get a detailed breakdown of strengths, weaknesses, and improvement areas.
- 🗺️ **Personalized Roadmaps**: Generate step-by-step career roadmaps tailored to your target roles and current skill gaps.
- 💬 **Interactive Interview Coach**: Practice with an AI-powered coach that provides realistic interview scenarios and constructive feedback.
- 💼 **Smart Job Recommendations**: Get job suggestions that match your specific skill set and career goals.
- 📰 **Curated Tech News**: Stay ahead of the curve with the latest industry trends and technology updates.
- 🛠️ **Seamless Resume Creation**: Build professional resumes using AI-guided templates and suggestions.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **AI Engine**: [Groq](https://groq.com/) (Llama-3 models)
- **Database**: [Supabase](https://supabase.com/)
- **Live Data**: NewsAPI for industry updates
- **Containerization**: [Docker](https://www.docker.com/)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker (optional, for containerized deployment)
- API Keys for Groq, Supabase, and NewsAPI

### Local Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MuhammadHamza123c/TalentPilot.git
   cd TalentPilot
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your credentials:
   ```env
   groq_api_key="your_groq_api_key"
   SUPABASE_PROJECT_URL="your_supabase_url"
   SUPABASE_API_KEY="your_supabase_key"
   news_api_key="your_news_api_key"
   ```

5. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```
   Access the API documentation at `http://127.0.0.1:8000/docs`.

### Running with Docker

1. **Build the image**:
   ```bash
   docker build -t talentpilot .
   ```

2. **Run the container**:
   ```bash
   docker run -p 7860:7860 --env-file .env talentpilot
   ```

---

## 📖 Usage

TalentPilot provides a clean REST API. Once running, you can explore the endpoints via the Swagger UI:

- **Resume Analysis**: `GET /TalentPilot/analyz_resume`
- **Dashboard**: `GET /TalentPilot/dashboard_`
- **Career Roadmap**: `POST /TalentPilot/road_map`
- **Interview Coach**: `POST /TalentPilot/interview`
- **Tech News**: `GET /TalentPilot/tech_news`

---

## 🛠️ Project Structure

```text
├── app/
│   ├── agents/      # AI logic and prompt engineering
│   ├── api/routes/  # FastAPI route definitions
│   ├── schema/      # Pydantic models for data validation
├── Resume/          # Sample resume images
├── main.py          # Application entry point
├── Dockerfile       # Containerization configuration
└── requirements.txt # Project dependencies
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any suggestions or bug reports.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

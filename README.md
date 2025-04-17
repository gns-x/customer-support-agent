# **AI-Powered Customer Support Automation Agent**  
**Dockerized AI Agent with n8n, OpenAI, and Slack Integration**  

![Project Architecture](https://i.imgur.com/placeholder.png) *Example architecture diagram*  

## **📌 Overview**  
This project automates customer support workflows using:  
- **n8n** for low-code workflow orchestration.  
- **OpenAI (GPT-3.5 Turbo)** to handle complex queries.  
- **Docker** for containerized deployment.  
- **Slack** for real-time notifications.  

Built for the **AY Automate AI Agent Developer Internship**, it demonstrates skills in:  
✅ AI agent development  
✅ Docker & microservices  
✅ API/webhook integrations  
✅ Business process automation  

---

## **🚀 Features**  
1. **Ticket Submission**: Web interface (Flask) to submit support requests.  
2. **AI Escalation**: Routes complex issues to OpenAI for resolution.  
3. **Slack Alerts**: Notifies a Slack channel for urgent tickets.  
4. **Database Logging**: Stores ticket history in PostgreSQL.  
5. **n8n Automation**: Handles routing, AI calls, and notifications.  

---

## **🛠️ Tech Stack**  
| Component       | Technology |  
|----------------|------------|  
| **Backend**    | FastAPI (Python) |  
| **Frontend**   | Flask (Python) |  
| **Workflows**  | n8n |  
| **AI**         | OpenAI GPT-3.5 Turbo |  
| **Database**   | PostgreSQL |  
| **Deployment** | Docker |  

---

## **⚙️ Setup & Installation**  

### **Prerequisites**  
- Docker & Docker Compose  
- OpenAI API key  
- Slack webhook URL (optional)  

### **1. Clone the Repository**  
```bash  
git clone https://github.com/yourusername/ay-automate-ai-agent.git  
cd ay-automate-ai-agent  
```  

### **2. Configure Environment Variables**  
Create a `.env` file:  
```plaintext  
OPENAI_API_KEY=your_openai_key_here  
SLACK_WEBHOOK_URL=https://hooks.slack.com/...  # Optional  
```  

### **3. Run with Docker Compose**  
```bash  
docker-compose up --build  
```  

### **4. Access Services**  
| Service       | URL |  
|--------------|-----|  
| **Frontend** | `http://localhost:5000` |  
| **n8n**      | `http://localhost:5678` |  
| **API Docs** | `http://localhost:8000/docs` |  

---

## **📂 Project Structure**  
```plaintext  
ay-automate-ai-agent/  
├── docker-compose.yml  
├── ai_backend/          # FastAPI + OpenAI  
├── frontend/            # Flask UI  
├── n8n/                 # Workflow configs  
├── db/                  # PostgreSQL setup  
└── docs/                # Architecture & setup guides  
```  

---

## **🔧 How It Works**  
1. **User submits a ticket** via the Flask frontend.  
2. **n8n workflow triggers**:  
   - Simple tickets → Logged in PostgreSQL.  
   - Complex tickets → Sent to OpenAI for resolution.  
3. **Slack notification** sent for urgent issues.  

![Workflow Diagram](https://i.imgur.com/placeholder.png)  

---

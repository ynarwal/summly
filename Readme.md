# **AI Summarizer - FastAPI**
A FastAPI-based AI-powered document summarization service that extracts text from uploaded PDF/DOCX files and provides structured summaries in four formats using OpenAI's GPT-4o-mini.

## **Features**
✅ Upload and extract text from **PDF** and **DOCX** files  
✅ AI-powered **document summarization**  
✅ Provides **four summary formats**:  
   - **Short Version** (30-50 words)  
   - **Detailed Version** (100-200 words)  
   - **Technical Version** (domain-specific)  
   - **Layman Version** (simplified explanation)  
✅ View **summary history**  
✅ Delete summaries  

---

## **Tech Stack**
| Component  | Technology |
|------------|------------|
| **Backend** | FastAPI (Python) |
| **AI API**  | OpenAI GPT-4o-mini |
| **Storage** | AWS S3 (for file uploads, optional) |
| **Database** | PostgreSQL / Firebase Firestore (future enhancement) |
| **Auth**     | Firebase Auth (future enhancement) |
| **Frontend** | React (planned integration) |

---

## **Installation & Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/ai-summarizer.git
cd ai-summarizer
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### **5. Run the FastAPI Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## **API Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/upload` | Upload a file (PDF/DOCX) and extract text |
| `POST` | `/summarize` | Get AI-generated summaries in four formats |
| `GET`  | `/history` | Retrieve previous summaries (mock data for now) |
| `DELETE` | `/delete` | Delete a summary (mock implementation) |

---

## **Example Usage**
### **1. Upload a File**
#### **Request**
```bash
curl -X 'POST' \
  'http://localhost:8000/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@example.pdf'
```
#### **Response**
```json
{
  "message": "File uploaded successfully",
  "text": "Extracted text content here..."
}
```

---

### **2. Get AI-Generated Summaries**
#### **Request**
```bash
curl -X 'POST' \
  'http://localhost:8000/summarize' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Your extracted text here"}'
```
#### **Response**
```json
{
  "short_version": "...",
  "detailed_version": "...",
  "technical_version": "...",
  "layman_version": "..."
}
```

---

## **Future Enhancements**
🚀 **User Authentication** (Google login, Firebase Auth)  
🚀 **Storage & History** (Save summaries in PostgreSQL/Firebase)  
🚀 **Payment Integration** (Stripe, PayPal for API access)  
🚀 **Frontend (React Integration)**  

---

## **License**
This project is licensed under the **MIT License**.


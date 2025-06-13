 🚀 terraform-gen-gemini

A **Streamlit-based Terraform configuration generator** powered by the **Google Gemini API**.  
The app dynamically generates Terraform HCL configurations from user infrastructure requests, optionally using relevant AWS documentation stored locally.

---

 📌 Features

- 🔍 Textbox to enter infrastructure requirements
- 📚 Searches local Terraform documentation in `./data/`
- ✨ Generates clean Terraform configuration using **Gemini 1.5 Flash**
- 💾 Saves generated config to `./output/` directory
- 🌐 Simple browser-based interface via **Streamlit**
- 🔐 API key securely managed through a `.env` file

---

 📦 Tech Stack

- **Python 3.13+**
- **Streamlit**
- **Google Gemini API**
- **dotenv**
- **Markdown document retrieval**

---

 📂 Project Structure

terraform_gen_gemini/
├── app.py
├── data/
│ └── aws_ec2.md
├── output/ (ignored via .gitignore)
├── .env (ignored via .gitignore)
├── requirements.txt
├── README.md
└── .gitignore

Install dependencies:
```bash
pip install -r requirements.txt


GOOGLE_API_KEY=your_gemini_api_key_here

streamlit run app.py





# 🚀 terraform-gen-gemini

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


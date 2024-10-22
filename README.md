
# Documentation

**LinkCraftAI** is a Python-based web application developed to generate enriched, AI-powered content suggestions for digital marketers. By providing relevant keywords and topics, the app leverages API integrations (like Google Gemini and Unsplash) to create and optimize content, making it easier for marketers to craft high-quality links and improve SEO strategies.

## 🚩 **Problem Statement**

In the fast-paced world of digital marketing, creating unique, optimized, and visually appealing content regularly can be time-consuming and challenging. Marketers often need to balance SEO best practices with creativity, but the constant demand for fresh content can lead to burnout. Additionally, integrating relevant visual elements adds another layer of complexity. 


## 🌟 **Objective**

The primary goal of LinkCraftAI is to simplify the process of generating AI-assisted content and imagery by utilizing advanced API services, making it a valuable tool for content creators, marketers, and SEO specialists.

**LinkCraftAI** addresses this problem by:
1. Suggesting content ideas based on user inputs (keywords/topics).
2. Using APIs like Google Gemini to generate enhanced content suggestions.
3. Pulling high-quality images from Unsplash to support the content.
4. Streamlining the link-building process with relevant suggestions.

## 🔄 **Workflow**

1. **Input Keywords**: The user provides specific keywords or topics related to their marketing campaign.
2. **AI-Driven Content Generation**: LinkCraftAI interacts with external APIs (e.g., Google Gemini) to generate AI-powered content recommendations.
3. **Image Integration**: The app fetches relevant images via the Unsplash API, which can be used alongside the generated content.
4. **Output**: The user receives a ready-made content suggestion enriched with SEO-friendly links and accompanying images, which can be customized as per the user's requirements.

## 🧑🏻‍💻 **Working**

<img src="Resources/working.gif">



## 🛠️ **Features**
- **AI-powered Content Suggestions**: Leveraging advanced natural language processing (NLP) models to generate optimized content ideas.
- **API Integrations**: Incorporates Google Gemini for content and Unsplash for relevant images.
- **User-Friendly Interface**: Built on Streamlit, making the application accessible and easy to use for non-technical users.
- **Cloud-Ready**: Hosted on Streamlit Community Cloud for easy accessibility and scalability.

## 🛠 **Setup Instructions**

To run the project locally, follow the steps below:

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Streamlit
- Required API keys (Google Gemini, Unsplash)

### 1. Clone the Repository

```bash
git clone https://github.com/mShubham18/LinkCraftAI.git
cd LinkCraftAI
```

### 2. Install Dependencies

Install the required packages by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

You'll need to add your API keys for **Google Gemini** and **Unsplash**. You can set these as environment variables by updating "`apikey.py`" with your api keys:

```python
# if running from streamlit
import os
google_gemini_api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')

# if running locally
google_gemini_api_key = "<YOUR_GOOGLE_GEMINI_API_KEY>"
UNSPLASH_ACCESS_KEY = '<YOUR_UNSPLASH_ACCESS_KEY>'
```

### 4. Run the Application

Start the Streamlit server:

```bash
streamlit run LinkCraftAI.py
```

### 5. Access the Application

Visit `http://localhost:8501` to view and interact with **LinkCraftAI**.

## 🚀 **Deployment**

LinkCraftAI is deployed using **Streamlit Cloud**. You can access the live version of the app here:

[LinkCraftAI on Streamlit](https://linkcraftai.streamlit.app/)

NOTE: Streamlit Community Cloud makes applications sleep during activity for 2 days, therefore, if shown,click on "`Yes, Get this app back up!`" Button 

## 🎯 **Future Enhancements**
- Integration with more content generation APIs for Image, Video Generation (e.g., OpenAI GPT, DeepAI).
- Allow users to save content drafts within the app.
- Add analytics to track content performance.

Happy Coding ;)

from lib.libraries import *
from apikey import google_gemini_api_key
#API_STUFF

genai.configure(api_key=google_gemini_api_key)

# Generating the Model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Setting up the Model
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
)


#APP stuff

st.set_page_config(layout="wide")
# Main configs
st.title("BlogBuddyAI: Your AI Blogging Companion")
st.text("Enter your topic, and let our AI do the heavy lifting in content creation")

#sidebar

with st.sidebar:
    st.title("Input your blog details")
    st.subheader("Enter details of the blog you want to generate")

    #blog Title
    blog_title=st.text_input("Blog title",placeholder="ex: power of AI")

    #keywords input
    keywords = st.text_area("Keywords",placeholder="ex : tech, trend")
    
    #Number of words
    num_words = st.slider("Size of Blog you'd like ? (in words)",min_value=100, max_value=1000, step=250)
    #Number of words
    num_images = st.number_input("Number of Images you'd like ?",min_value=1, max_value=5,step=1)

    #button
    submit_button = st.button("Generate")

    # Blog generation prompt
    prompt = (f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" "
          f"and keywords \"{keywords}\". The blog should be approximately {num_words} words in length. "
          f"Make sure to incorporate these keywords in the blog post. Also, include proper subheadings "
          f"like introduction and conclusion wherever required. Use data to emphasize the effect in the "
          f"real world, wherever necessary. The blog must be suitable for an online audience. Ensure the "
          f"content is original, informative, and maintains a consistent tone throughout.")

# Generate blog content when the submit button is pressed
if submit_button:
    response = model.generate_content([prompt])
    st.write(response.text)  # Assuming the response contains a 'text' field

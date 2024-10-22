from lib.libraries import *
from apikey import google_gemini_api_key, UNSPLASH_ACCESS_KEY
import requests
import json
from src.BlogBuddyAI.components.unsplash_fetch import fetch_unsplash_images
from src.BlogBuddyAI.components.gemini_fetch import generation_config,model


# API Setup
genai.configure(api_key=google_gemini_api_key)


# APP Configurations

st.set_page_config(layout="wide")
st.title("LinkCraftAI: Smart Content, Instant Results")
st.text("Enter your topic, and let our AI do the creation of your desired linkedin post")

# Sidebar
with st.sidebar:
    st.title("Input your post details")
    st.subheader("Enter details of the post you want to generate")

    # Blog Title
    post_title = st.text_input("post title", placeholder="ex: power of AI")

    # Keywords input
    keywords = st.text_area("keywords", placeholder="ex : tech, trend")

    # Number of words
    num_words = st.slider("Size of Blog you'd like? (in words)", min_value=100, max_value=1000, step=250)
    # Number of images
    num_images = st.number_input("Number of Images you'd like?", min_value=1, max_value=5, step=1)

    # Button
    submit_button = st.button("Generate")

    # Blog generation prompt
    prompt = (f"Generate a comprehensive, engaging blog post relevant to the given title \"{post_title}\" "
              f"and keywords \"{keywords}\". The blog should be approximately {num_words} words in length. "
              f"Make sure to incorporate these keywords in the blog post. Also, include proper subheadings "
              f"like introduction and conclusion wherever required. Use data to emphasize the effect in the "
              f"real world, wherever necessary. The blog must be suitable for an online audience. Ensure the "
              f"content is original, informative, and maintains a consistent tone throughout.")

# Generate blog content when the submit button is pressed
if submit_button:
    with st.spinner("Generating your post, please wait..."):
        # Simulating content generation delay
        time.sleep(2)  # Remove this or replace it with the actual generation code
        
        # Your actual blog content generation code
        response = model.generate_content([prompt])
        st.write(response.text)  # Assuming the response contains a 'text' field
        
        # Fetch images from Unsplash instead of LimeWire
        unsplash_response = fetch_unsplash_images(post_title, UNSPLASH_ACCESS_KEY, num_images)
        
        if 'error' in unsplash_response:
            st.error(unsplash_response['error'])
        else:
            if 'results' in unsplash_response:  # Check if images are returned
                for idx, img in enumerate(unsplash_response['results']):
                    st.image(img['urls']['small'], caption=f"Generated Image {idx + 1}")
            else:
                st.error("No images were returned.")
import streamlit as st
from duckduckgo_search import DDGS

def setup_page():
    """Sets up the Streamlit page configuration."""
    st.set_page_config(
        page_title="Chords Search",
        page_icon="🎵",
        layout="wide",
    )

    st.title("🎸 Truevis Chords Search")

def perform_search(query):
    """Performs a search using DuckDuckGo and returns the results."""
    search_query = f"{query} chords and lyrics"
    with DDGS() as ddgs:
        results = list(ddgs.text(search_query, backend="lite", max_results=10))
    return results

def display_results(results):
    """Displays the search results."""
    if not results:
        st.warning("No results found.")
        return

    for result in results:
        st.markdown(f"#### [{result['title']}]({result['href']})")
        st.write(result['body'])

def main():
    """Main function to run the Streamlit app."""
    setup_page()

    song_query = st.text_input(
        "Enter a song title or description to search for 'chords and lyrics':",
        placeholder="e.g., Drove my Chevy to the levee",
        key="song_input"
    )

    if song_query:
        with st.spinner(f"Searching for '{song_query}'..."):
            results = perform_search(song_query)
            display_results(results)
    st.markdown("---")
    st.markdown("Sponsored by [truevis.com](https://truevis.com) | Powered by [DuckDuckGo](https://duckduckgo.com)")

if __name__ == "__main__":
    main() 
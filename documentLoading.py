import os
import openai
import sys

from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


from langchain.document_loaders import PyPDFLoader


sys.path.append('../..')

openai.api_key  = os.environ['OPENAI_API_KEY']

loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()

len(pages)
page = pages[0]

print("Printing page content: ")
print(page.page_content[0:500])

print("Printing page metadata: ")
print(page.metadata) # page.metadata

# The use of `ffmpeg` is crucial for this section of the code where we leverage `yt-dlp` for downloading and processing media files. 
# `ffmpeg` is a versatile command-line tool that allows for converting audio and video formats, extracting media from download streams, 
# and performing various other media processing tasks. `yt-dlp`, a fork of youtube-dl, heavily relies on `ffmpeg` for postprocessing tasks 
# such as extracting audio from video files, converting media formats, and more. Ensuring `ffmpeg` is correctly installed and accessible 
# in the environment enables `yt-dlp` to utilize its full range of media handling capabilities. This setup is essential for the successful 
# execution of media download and transformation tasks in our project, providing a robust solution for managing media content effectively.

url="https://www.youtube.com/watch?v=jGwO_UgTS7I"
save_dir="docs/youtube/"
loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)
docs = loader.load()

print("Printing youtube content: ")
print(page.page_content[0:500])

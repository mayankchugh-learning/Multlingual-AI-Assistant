from setuptools import find_packages, setup

setup(
    name="multlingual assistant",
    version="0.0.1",
    author="Mayank",
    author_email="mayankchugh.learning@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]
)

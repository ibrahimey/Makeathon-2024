# Makeathon 2024

### How to Build

First you need to install the requirements.
```
pip install -r requirements.txt
```

We used Awan LLM's API in this project, so to be able to run it you need the API key in a .env file.
```python
AWANLLM_API_KEY="Your-API-key"
```

You can also modify model.py file to use another API or a local model.
Finally, you can just run the following command to access the chatbot.
```
streamlit run bot.py
```
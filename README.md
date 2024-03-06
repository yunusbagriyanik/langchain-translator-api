## LangChain Translator API

This project creates a text translation API using the LangChain framework and OpenAI's gpt-3.5 turbo language model.


1. Clone the repository
    ```bash
    git clone https://github.com/yunusbagriyanik/langchain-translator-api.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set Up OpenAI API Key

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```
Create a .env file in the project folder and add your OpenAI API key. The application will load this key using the load_dotenv() function at the beginning of the project.

### Run Application

   ```bash
    uvicorn main:app
   ```
## Usage
To translate text via the API, send a POST request to the following endpoint:

   ```
   POST http://127.0.0.1:8000/translate
   ```

Example JSON request:

```json
{
    "text": "What is a Large Language Model? A large language model (LLM) is a deep learning algorithm that can perform a variety of natural language processing (NLP) tasks.",
    "target_language": "fr"
}
```

Example JSON response:
```json
{
    "translation": "Qu'est-ce qu'un grand modèle de langue ? Un grand modèle de langue (LLM) est un algorithme d'apprentissage profond qui peut effectuer une variété de tâches de traitement du langage naturel (NLP)."
}
```

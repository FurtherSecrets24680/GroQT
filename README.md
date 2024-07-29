# GroQT

A standalone Python Qt6 application to chat with Groq AI by using various open-source models. An API key is required to chat.
![image](https://github.com/user-attachments/assets/77db8184-7d42-405e-b1da-659b7d384823) 

- Dark Mode

![image](https://github.com/user-attachments/assets/3b8fa93f-24da-42cb-97eb-6dbb27dc3df4)

- Light Mode

# Prerequisites

* Python (3.6 or higher)

  - PyQt6 Library
    ```
    pip install PyQt6
    ```
  - Markdown2 Library
    ```
    pip install markdown2
    ```

# Installation

Download directly from GitHub or by using the git command:
```
git clone https://github.com/FurtherSecrets24680/GroQT.git
```
Then, provide your Groq API key in the **config.py** folder, and run **main.py** to start chatting.

# Getting the API key

* Go to https://console.groq.com/keys and sign up or log in to your account.
* Click **Create API Key**, then enter a name for the key.

  ![image](https://github.com/user-attachments/assets/0db4aa2e-4a29-4e40-bfa1-bcd00303214a)

* Click **Submit** , copy he key, then put it in the **config.py** file.
(**MAKE SURE TO COPY THE KEY IMMEDIATELY, IT WONT SHOW IT AFTER CLOSING THE BOX.**)

  ![image](https://github.com/user-attachments/assets/d28e0275-70f6-4f6a-9dd3-f20d6dc2cf16)

# Features
- Model Selection Dropdown. Currently available models: 
  -  *Llama 3.1 405B **(NOT AVAILABLE IN THE GROQ API YET)**
  -  Llama 3.1 70B (Preview) by Meta
  -  Llama 3.1 8B (Preview) by Meta
  -  Llama 3 Groq 70B Tool Use (Preview) by Meta, refined by Groq
  -  Llama 3 Groq 8B Tool Use (Preview) by Meta, refined by Groq
  -  Meta Llama 3 70B (Default) by Meta
  -  Meta Llama 3 8B by Meta
  -  Mixtral 8x7B by Mistral AI
  -  Gemma 7B by Google
  -  Gemma 2 9B by Google
- Dark/Light mode switcher
- Chat area and input box obviously


# Planned
- Chat history
- Clear chat
- Ability to provide API key within the app

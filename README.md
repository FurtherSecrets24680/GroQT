# Overview

A standalone Python Qt6 application to chat with Groq AI by using various open-source models. An API key is required to chat, which is free. 
![image](https://github.com/user-attachments/assets/bb7d1656-9d27-42bf-b5dd-fde4fb752038)

- Dark Mode

![image](https://github.com/user-attachments/assets/2caf73bd-f222-45c3-a7b0-fe9370107f91)

- Light Mode

# Prerequisites

* Python (3.6 or higher)
  Use the commands below to install the following libraries: Groq, PyQt6, Markdown2
  - Groq Library
    ```
    pip install groq
    ```
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
- Configuring the "System Prompt" (from the config.py file)
- Markdown Support
- Chat area and input box obviously


# Planned
- [ ] Chat history - View/Delete/Export Chat history
- [ ] Clear chat
- [ ] Ability to provide API key within the app
- [ ] Ability to provide System Prompt within the app
- [ ] Custom bots with custom system prompts
- [ ] More UI improvements
and More...

# Known issues
- When asked to write poem or code, it tries to do it within one line/paragraph. Seems like a markdown issue.
  ![image](https://github.com/user-attachments/assets/b763fcd7-5e12-44ab-99d3-1cf919c813bb)

# Not So Frequently Asked Questions
- **Q: Why should I even use this?**
- **A:** It's your choice. If you like open-source AI models, too lazy to open a browser and don't have high end PC to run it locally, this application is just for you.
- **Q: Why isn't [Put a model name here] working? I have active internet connection and also provided an API key.**
- **A:** Maybe that specific model(s) got removed, or changed to a new name. Just go to the [Groq models documentation](https://console.groq.com/docs/models) to find the changes, then modify the code; or wait for me to update the app.
  
# Credits
- Inspired by **vn33**'s **PyQt6-Groq-Chatbot** - https://github.com/vn33/PyQt6-Groq-Chatbot

# References
- Groq API documentation - https://console.groq.com/docs
- Groq-python GitHub repo - https://github.com/groq/groq-python

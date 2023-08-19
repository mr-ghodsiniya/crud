# [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=550&size=30&duration=3500&color=ADBAC7&center=false&vCenter=true&repeat=true&width=700&lines=Simple+CRUD+with+FastAPI)](https://git.io/typing-svg)

# ⏳️ Installation

1. **clone the project**  
   ```  
   git@github.com:mr-ghodsiniya/crud.git
   ```

2. **create a python virtual environment**  
   ```
   python -m venv venv
   ```

3. **activate your venv**
  * on linux and mac
    ```
    source venv/bin/activate
    ```
  * on windows
    ```
    venv/Scripts/activate
    ```

4. **install dependencies**
   ```
   pip install -r requirements.txt
   ```

8. **migrate**
   ```
   alembic upgrade head
   ```

9. **run project**
   ```
   python main.py
   ```
   
# Testing APIs 💭

* **install [Postman](https://www.postman.com/)(recommended) or [Thunder Client](https://www.thunderclient.com) or [Swagger](https://swagger.io/)**  <br/>
To test API, you need to use postman app <br/>
**or** thunder client extension on VsCode **or** swagger.

* **Postman** <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a>

  * [install postman on Linux](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-linux)
  * [install postman on Windows](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-windows)
  * [install postman on Mac](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-postman-on-mac)
  > Use this [Guide](https://learning.postman.com/docs/sending-requests/requests/) on how to send request via **postman**. 
<br/>

* **Thunder Client** <br/>
  **Note**: You won't need this, if you've installed Postman.
       
  * Launch VsCode Extensions tab (Ctrl+Shift+X), search for _Thunder Client_ and install it.
  > Use this [Guide](https://developers.refinitiv.com/en/article-catalog/article/how-to-test-http-rest-api-easily-with-visual-studio-code---thund) on how to send request via **thunder client**.
<br/>

* **Swagger** <br/>
You can test APIs inside of project with the help of Google and localhost.
   ```
   http://127.0.0.1:8000/docs/
   ```
   **or**
   ```
   http://127.0.0.1:8000/redoc/
   ```

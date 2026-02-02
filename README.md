# backend-tasks
How to start the application:
1. Create and activate venv
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
MacOS/linux
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Configure environment variables
Create a .env file in the root directory by copying the sample file.
4. Run
```bash
uvicorn app.main:app --reload
```
How to Execute Tests:
1. Stop the server
2. Run test 
```Bash
pytest
```

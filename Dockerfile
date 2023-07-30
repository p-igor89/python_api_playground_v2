FROM python
WORKDIR /python_api_playground_v2/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=allure-results/ /python_api_playground_v2/tests/
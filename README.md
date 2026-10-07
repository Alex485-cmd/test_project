\# Test Project



Автотесты: API (requests) + Web (Selenium).



\## Запуск



1\. Активировать venv:

&#x20;  - Windows: `.venv\\Scripts\\activate`

&#x20;  - macOS/Linux: `source .venv/bin/activate`

2\. Установить зависимости: `pip install -r requirements.txt`

3\. Запустить все тесты: `pytest`

4\. Только API-тесты: `pytest api\_tests/`

5\. Только Selenium-тесты: `pytest selenium\_tests/`



\## Структура



\- `api\_tests/` — тесты API.

\- `selenium\_tests/fixtures/` — фикстуры pytest.

\- `selenium\_tests/locators/` — локаторы элементов.

\- `selenium\_tests/` — веб-тесты.


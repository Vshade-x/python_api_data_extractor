@echo off
cls
echo.
echo ======================================================
echo PYTHON API DATA EXTRACTOR (JSON to Excel)
echo ======================================================
echo.

set /p QUERY="Enter the search query (e.g., 'artificial intelligence'): "
echo.

REM Llama al script de Python, pasando la consulta como argumento
"C:/Program Files/Python311/python.exe" news_api_extractor.py --query "%QUERY%"

echo.
echo ======================================================
echo PROCESS FINISHED. Check the generated Excel file.
echo ======================================================

pause
FOR /F %%i IN ('python setup.py -V') DO set VERSION=%%i
scrapyd-deploy -v %VERSION%
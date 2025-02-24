FROM python:3.12.1-bookworm
WORKDIR /usr/share/app
COPY app/django_publicaciones .
RUN pip install --upgrade --no-cache-dir --break-system-packages --root-user-action=ignore pip && \
    pip install --no-cache-dir --break-system-packages --root-user-action=ignore -r requirements.txt && \
    pip install --no-cache-dir --break-system-packages --root-user-action=ignore mysqlclient

COPY dockerscript.sh /usr/local/bin/dockerscript.sh
RUN chmod +x /usr/local/bin/dockerscript.sh
EXPOSE 8084
CMD /usr/local/bin/dockerscript.sh

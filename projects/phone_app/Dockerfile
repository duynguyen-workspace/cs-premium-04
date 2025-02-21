FROM python

COPY . ./home/app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    x11-apps

WORKDIR /home/app/

RUN pip install customtkinter pylance pillow

CMD ["python", "app.py"]